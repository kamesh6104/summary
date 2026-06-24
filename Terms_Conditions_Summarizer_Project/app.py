import streamlit as st
import PyPDF2
from summarizer import summarize_text

st.title("📄 Terms & Conditions Summarizer")

uploaded_file = st.file_uploader(
    "Upload Terms & Conditions PDF",
    type=["pdf"]
)

if uploaded_file:
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = ""

    for page in pdf_reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text

    st.subheader("Original Text")
    st.text_area("", text[:3000], height=200)

    if st.button("Generate Summary"):
        with st.spinner("Summarizing..."):
            summary = summarize_text(text)

        st.subheader("Summary")
        st.success(summary)
