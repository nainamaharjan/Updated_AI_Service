import streamlit as st
from ui.Homepage import sentiment_analysis

st.title("Sentiment Analysis")
text_input = st.text_area("Enter text: ", key="sentiment-analysis")

if st.button("Analyse"):
    try:
        with st.spinner("Analyzing..."):
           sentiment_analysis = sentiment_analysis(text_input)
           st.text(sentiment_analysis)
    except Exception as e:
        print(f"Error : {e}")
        st.error(e)
