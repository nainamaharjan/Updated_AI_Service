import streamlit as st
from ui.Homepage import keyword_extraction

st.title("Keyword Extraction")
text_input = st.text_area("Enter text: ", key="keyword_extraction")

if st.button("Extract"):
    try:
        with st.spinner("Extracting..."):
            extracted_keywords = keyword_extraction(text_input)
            st.text(extracted_keywords)
    except Exception as e:
        print(f"Error : {e}")
        st.error("Extraction failed")