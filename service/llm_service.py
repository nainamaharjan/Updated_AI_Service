"""
   Created by: Naina Maharjan
   Created on: 2024-02-08
"""
import guidance
from guidance import models, system, user, gen, assistant
from entities.ai_entities import  TaskType
import torch
import gc
from settings import MODEL


class LlmService:
    def __init__(self, device: str = "auto", **kwargs):
        self.device = device
        self.llm = models.LlamaCppChat(
            model=MODEL,
            n_ctx=4096, n_gpu_layers=-1)

    def inference_stream(self, input_text: str = None, clear_cache: bool = True):
        if clear_cache:
            torch.cuda.empty_cache()
            gc.collect()
        reply_text = ""
        try:
            for output in self.llm.stream() + get_lm_for_ai_assistant(input_text=input_text):
                output = str(output).split("[/INST]")[-1]
                reply_text = output
        except:
            return reply_text
        return reply_text

    @torch.inference_mode()
    def inference(self, input_text: str = None, task_type: TaskType = None) -> str:
        print("Performing %s via Guidance for input %s" % (task_type, input_text))
        reply = ""
        try:
            if task_type == TaskType.GRAMMAR_CHECK:
                for out in self.llm.stream() + get_lm_check_grammar(input_text=input_text):
                    reply = str(out)
            elif task_type == TaskType.PROFESSIONAL:
                for out in self.llm.stream() + get_lm_professional(input_text=input_text):
                    reply = str(out)
            elif task_type == TaskType.CASUAL:
                for out in self.llm.stream() + get_lm_casual(input_text=input_text):
                    reply = str(out)
            elif task_type == TaskType.SHORTEN:
                for out in self.llm.stream() + get_lm_summary(input_text=input_text):
                    reply = str(out)
            elif task_type == TaskType.ELABORATE:
                for out in self.llm.stream() + get_lm_elaboration(input_text=input_text):
                    reply = str(out)
            elif task_type == TaskType.KEYWORD_EXTRACTION:
                for out in self.llm.stream() + get_lm_keyword_extraction(input_text=input_text):
                    reply = str(out)
            elif task_type == TaskType.SENTIMENT_ANALYSIS:
                for out in self.llm.stream() + get_lm_sentiment_analysis(input_text=input_text):
                    reply = str(out)
        except Exception as e:
            print(f"Error: {e}")
            print(reply)
        return self._post_process_response(reply, task_type)


    def _post_process_response(self, response: str, task_type: TaskType) -> str:
        import json

        # Clean up the response string
        response = response.split("[/INST]")[-1]
        response = response.strip().replace(":'", ":\"").replace("'}", "\"}").replace("{'", "{\"").replace("':", "\":")

        # Load the response as JSON
        try:
            response_json = json.loads(response)
        except json.JSONDecodeError as e:
            print(f"JSON decode error: {e}")
            return response

        # Extract the appropriate field based on task type
        if task_type == TaskType.GRAMMAR_CHECK:
            return response_json.get("corrected_text", response)
        elif task_type == TaskType.PROFESSIONAL:
            return response_json.get("professional", response)
        elif task_type == TaskType.CASUAL:
            return response_json.get("casual", response)
        elif task_type == TaskType.SHORTEN:
            return response_json.get("summary", response)
        elif task_type == TaskType.ELABORATE:
            return response_json.get("elaboration", response)
        else:
            return response

    # def _post_process_generative_response(self, response):


@guidance
def get_lm_for_ai_assistant(lm, input_text):
    with system():
        lm = lm + "You are a helpful ai assistant that answers user query in friendly and polite manner."
    with user():
        lm += input_text
    with assistant():
        lm += gen("response", max_tokens=200, stop="<<< [SYS] >>")
    return lm["response"]


@guidance
def get_lm_check_grammar(lm, input_text):
    with system():
        lm = lm + (
            "You are a grammar correcting agent. You correct errors in grammar and spellings of the user's input."
            "Just return the corrected sentence and nothing else.")
    with user():
        lm += "Please correct the grammar for the following sentence. Please respond with {'corrected_text':'your response here' }" + input_text
    with assistant():
        lm += gen("corrected_text", stop=["SYS", "[/INST]", "[INST]"], max_tokens=200)
    return lm["corrected_text"]


@guidance
def get_lm_professional(lm, input_text):
    with system():
        lm = lm + (
            "You are an agent that converts user's input to make them sound more professional. Make the user sound very professional.")
    with user():
        lm += "Please make my sentence more professional. Please respond in  {'professional':'your response here' }\n" + input_text
    with assistant():
        lm += gen("professional_response", stop=["SYS", "[/INST]", "[INST]"], max_tokens=200)
    return lm["professional_response"]

@guidance
def get_lm_summary(lm, input_text):
    with system():
        lm = lm + (
            "You are an agent that converts user's input into a concise summary. Summarize the content effectively.")
    with user():
        lm += "Please summarize the following text. Please respond in  {'summary':'your response here' }\n" + input_text
    with assistant():
        lm += gen("summary_response", stop=["SYS", "[/INST]", "[INST]"], max_tokens=200)
    return lm["summary_response"]

@guidance
def get_lm_elaboration(lm, input_text):
    with system():
        lm = lm + (
            "You are an agent that expands on the user's input to provide a more detailed and elaborate explanation. Elaborate on the content effectively.")
    with user():
        lm += "Please elaborate on the following text. Please respond in  {'elaboration':'your response here' }\n" + input_text
    with assistant():
        lm += gen("elaboration_response", stop=["SYS", "[/INST]", "[INST]"], max_tokens=200)
    return lm["elaboration_response"]


@guidance
def get_lm_casual(lm, input_text):
    with system():
        lm = lm + (
            "You are an agent that converts user's input to make them sound more casual. Make the user sound casual.")
    with user():
        lm += "Please make my sentence more casual. Please respond in  {'casual':'your response here' }\n" + input_text
    with assistant():
        lm += gen("casual_response", stop=["SYS", "[/INST]", "[INST]"], max_tokens=200)
    return lm["casual_response"]

@guidance
def get_lm_keyword_extraction(lm, input_text):
    with system():
        lm = lm + (
            "You are an agent that extracts keywords from the user's input. Identify the most important words or phrases effectively.")
    with user():
        lm += "Please extract keywords  {'keyword':'your response here' }\n" + input_text
    with assistant():
        lm += gen("keyword_response", stop=["SYS", "[/INST]", "[INST]"], max_tokens=200)
    return lm["keyword_response"]

@guidance
def get_lm_sentiment_analysis(lm, input_text):
    with system():
        lm = lm + ("You are an agent that analyzes sentiment. Analyze the sentiment of the user's input.")
    with user():
        lm += "Please extract sentiments. Please respond in {'sentiment':'your response here' }\n" + input_text
    with assistant():
        lm += gen("keyword_sentiment", stop=["SYS", "[/INST]", "[INST]"], max_tokens=200)
    return  lm["keyword_sentiment"]
