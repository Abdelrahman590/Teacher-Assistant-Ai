# teacher_analyzer_app.py
import streamlit as st
import os
import tempfile
from transformers import pipeline
from PyPDF2 import PdfReader
import pytesseract
from PIL import Image
#import moviepy.editor as mp
import speech_recognition as sr
#import imageio_ffmpeg
#print(imageio_ffmpeg.get_ffmpeg_exe())


st.set_page_config(page_title="مساعد المعلمة الذكي", layout="centered")
st.title("📚 مساعد المعلمة لتحليل المحتوى وتوليد الأسئلة")

uploaded_file = st.file_uploader("📎 حمّلي ملف الدرس (PDF, صورة, فيديو)", type=["pdf", "jpg", "png", "mp4"])

# ---------- استخراج النص ----------
def extract_text_from_pdf(file):
    reader = PdfReader(file)
    return "\n".join(page.extract_text() for page in reader.pages if page.extract_text())

def extract_text_from_image(image_file):
    image = Image.open(image_file)
    return pytesseract.image_to_string(image, lang='ara')

#def extract_text_from_video(video_file):
    #with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as tmp:
    #    tmp.write(video_file.read())
    #    tmp_path = tmp.name

    #clip = mp.VideoFileClip(tmp_path)
    #audio_path = tmp_path.replace(".mp4", ".wav")
    #clip.audio.write_audiofile(audio_path)

    #recognizer = sr.Recognizer()
    #with sr.AudioFile(audio_path) as source:
    #    audio = recognizer.record(source)
    #try:
    #    return recognizer.recognize_google(audio, language='ar')
    #except:
    #    return "لم يتم التعرف على الكلام."

# ---------- توليد الأسئلة ----------
def generate_questions(text):
    qa_pipeline = pipeline("text2text-generation", model="aubmindlab/aragpt2-base")
    prompt = f"اسأل 3 أسئلة لفهم النص التالي:\n{text}"
    return qa_pipeline(prompt, max_new_tokens=150)[0]['generated_text']

if uploaded_file:
    with st.spinner("🔍 جاري تحليل المحتوى..."):
        ext = uploaded_file.name.split(".")[-1].lower()

        if ext == "pdf":
            content_text = extract_text_from_pdf(uploaded_file)
        elif ext in ["jpg", "png"]:
            content_text = extract_text_from_image(uploaded_file)
        #elif ext == "mp4":
        #    content_text = extract_text_from_video(uploaded_file)
        else:
            content_text = "صيغة غير مدعومة."

        if content_text.strip():
            st.success("✅ تم استخراج النص بنجاح!")
            st.text_area("📖 النص المستخرج:", content_text, height=200)

            if st.button("✏️ توليد أسئلة بناءً على المحتوى"):
                with st.spinner("✍️ جاري توليد الأسئلة..."):
                    result = generate_questions(content_text[:600])  # Limit for processing
                    st.subheader("📌 أسئلة مقترحة:")
                    for q in result.split("\n"):
                        if q.strip():
                            st.markdown(f"- {q.strip()}")
        else:
            st.error("❌ لم يتم استخراج أي نص من الملف.")
