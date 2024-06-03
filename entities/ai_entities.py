"""
   Created by: Naina Maharjan
   Created on: 2024-05-15
"""
from pydantic import BaseModel
from enum import Enum





class TaskType(str,Enum):
    GRAMMAR_CHECK = "GRAMMAR_CHECK"
    PROFESSIONAL = "PROFESSIONAL"
    CASUAL = "CASUAL"
    SHORTEN = "SHORTEN"
    ELABORATE = "ELABORATE"
    KEYWORD_EXTRACTION = "KEYWORD_EXTRACTION"
    SENTIMENT_ANALYSIS = "SENTIMENT_ANALYSIS"

class Prompt(BaseModel):
    system_prompt: str = None
    system_instruction: str = None
    response: str = None
    task_type:TaskType = None