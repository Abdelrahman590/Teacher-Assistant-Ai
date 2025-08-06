# teacher_analyzer_app.py
import streamlit as st
import os
import tempfile
from transformers import pipeline
from PyPDF2 import PdfReader
import pytesseract
from PIL import Image
import io

st.set_page_config(page_title="مساعد المعلمة الذكي", layout="centered")
st.title("📚 مساعد المعلمة لتحليل المحتوى وتوليد الأسئلة")

uploaded_file = st.file_uploader("📎 حمّلي ملف الدرس (PDF, صورة)", type=["pdf", "jpg", "png"])

# ---------- استخراج النص ----------
def extract_text_from_pdf(file):
    reader = PdfReader(file)
    return "\n".join(page.extract_text() for page in reader.pages if page.extract_text())

def extract_text_from_image(image_file):
    image = Image.open(image_file)
    return pytesseract.image_to_string(image, lang='ara')

# ---------- توليد الأسئلة ----------
def generate_questions(text):
    qa_pipeline = pipeline("text2text-generation", model="google/flan-t5-base")
    # تقسيم النص إلى فقرات أو جمل طويلة وتوليد أكثر من سؤال لكل جزء
    chunks = [text[i:i+500] for i in range(0, len(text), 500)]
    all_questions = []

    for chunk in chunks:
        prompt = (
            f"Generate 2 to 3 different comprehension questions in English from the following lesson text. "
            f"Do not include answers, and separate questions by newline:\n\n{chunk}"
        )
        result = qa_pipeline(prompt, max_new_tokens=200)[0]['generated_text']
        questions = [q.strip("-• \n") for q in result.split("\n") if len(q.strip()) > 8]
        all_questions.extend(questions)

    return all_questions

if uploaded_file:
    with st.spinner("🔍 جاري تحليل المحتوى..."):
        ext = uploaded_file.name.split(".")[-1].lower()

        if ext == "pdf":
            content_text = extract_text_from_pdf(uploaded_file)
        elif ext in ["jpg", "png"]:
            content_text = extract_text_from_image(uploaded_file)
        else:
            content_text = "صيغة غير مدعومة."

        if content_text.strip():
            st.success("✅ تم استخراج النص بنجاح!")
            st.text_area("📖 النص المستخرج:", content_text, height=200)

            if st.button("✏️ توليد أسئلة بناءً على المحتوى"):
                with st.spinner("✍️ جاري توليد الأسئلة..."):
                    questions = generate_questions(content_text)
                    st.subheader("📌 الأسئلة:")

                    for idx, question in enumerate(questions, 1):
                        st.markdown(f"**{idx}. {question}**")

                    # خيار تحميل الأسئلة كملف نصي
                    st.download_button(
                        label="📥 تحميل الأسئلة كملف نصي",
                        data="\n".join(f"{i+1}. {q}" for i, q in enumerate(questions)),
                        file_name="generated_questions.txt",
                        mime="text/plain"
                    )
        else:
            st.error("❌ لم يتم استخراج أي نص من الملف.")
