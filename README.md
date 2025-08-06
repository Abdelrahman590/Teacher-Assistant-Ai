# Teacher-Assistant-Ai
ملف README احترافي لمشروع "مساعد المعلمة لتحليل الدروس وتوليد الأسئلة":

# 📚 Teacher Content Analyzer & Question Generator

تطبيق ويب مطور باستخدام الذكاء الاصطناعي لمساعدة المعلمين والمعلمات في **تحليل محتوى الدروس** وتوليد **أسئلة فهم أو اختيار من متعدد** بشكل تلقائي وسريع من الملفات النصية أو الصور (وأحيانًا الفيديو).

## ⚡️ المميزات الرئيسية

- **رفع ملفات الدروس**: يدعم ملفات PDF، الصور (jpg, png)، ويمكن تطويره مستقبلاً لدعم الفيديو.
- **استخراج النصوص تلقائيًا**: يعتمد على تقنية OCR للصور ومكتبات PDF لاستخراج النصوص العربية أو الإنجليزية.
- **توليد أسئلة ذكية**: يستخدم نماذج متقدمة من الذكاء الاصطناعي (مثل T5 أو AraGPT2 وFlan-T5) لتوليد أسئلة متنوعة من نص الدرس بدون تدخل بشري.
- **دعم للغتين العربية والإنجليزية**
- **واجهة سهلة الاستخدام**: المبنية بـStreamlit لتبسيط تجربة المستخدم.
- **تصدير النتائج**: إمكانية تحميل الأسئلة الناتجة كملف نصي.

## 🏗️ كيفية الاستخدام

1. **رفع ملف الدرس** (PDF أو صورة) من خلال الواجهة.
2. **انتظر استخراج النص** تلقائيًا وعرضه في مربع النص.
3. **اضغط زر "توليد أسئلة"** للبدء في إنشاء أسئلة فهم مبنية على محتوى الدرس.
4. **معاينة أو تحميل الأسئلة** الناتجة لاستخدامها في الاختبارات أو الأنشطة الصفية.

## 💻 التقنيات والأدوات المستخدمة

| التقنية          | الاستخدام                                        |
|------------------|-------------------------------------------------|
| Streamlit        | بناء واجهة المستخدم                             |
| transformers     | توليد الأسئلة بالذكاء الاصطناعي                  |
| PyPDF2           | استخراج نصوص من ملفات PDF                       |
| Pytesseract      | التعرف الضوئي على الحروف (OCR)                  |
| Pillow           | معالجة الصور                                    |
| SpeechRecognition| (اختياري) استخراج نص من ملفات صوت أو فيديو       |

## ⚙️ كيف تثبت المشروع وتعمل عليه

```bash
git clone https://github.com/USERNAME/REPO_NAME.git
cd REPO_NAME
pip install -r requirements.txt
streamlit run teach_analysis.py
```
*استبدل `USERNAME` و`REPO_NAME` ببياناتك الفعلية.*

## 🔄 دعم النماذج واللغات

- **النموذج العربي:** يستخدم `aubmindlab/aragpt2-base`
- **النموذج الإنجليزي:** يستخدم `google/flan-t5-base`
- يمكنك تخصيص النماذج بسهولة عبر تغيير اسم النموذج في الكود (`pipeline`).

## 📁 هيكل الملفات

| الملف                | الوصف                          |
|----------------------|-------------------------------|
| teach_analysis.py    | التطبيق للغة العربية           |
| analysis_en.py       | التطبيق للغة الإنجليزية         |
| requirements.txt     | قائمة الحزم اللازمة للتشغيل     |

## 🙏 مساهماتك

- أي اقتراح أو تعديل مرحب به!
- افتح Issue أو Pull Request حسب الحاجة.

## 📞 الدعم

لو عندك أي استفسار أو واجهتك مشكلة، راسلني عبر GitHub أو في Issues الريبو، وهرد عليك في أسرع وقت.

**برمجة: [اسمك أو حسابك على جيتهب]**

موجه خصيصًا لدعم العملية التعليمية وتوفير وقت ومجهود المعلمين والمعلمات ❤️

[1] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/78692958/c9908502-25ea-40fb-abce-95f536e9149a/teach_analysis.py
[2] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/78692958/596764d0-d10b-4ace-89ea-8c6f7fe80d77/analysis_en.py
[3] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/78692958/e22ab1e7-d263-4a29-8f4b-5536dd62af9d/generated_questions-1.txt
[4] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/78692958/642f2aaa-893d-4037-b076-618dc24c8b52/generated_questions-2.txt
[5] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/78692958/ee7253bb-0b65-488d-8e0b-ac03b4010f2c/generated_questions.txt
[6] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/78692958/6ffc560a-1287-4653-ae38-d0847d0861e1/NLP_lec_1_quistions.txt
