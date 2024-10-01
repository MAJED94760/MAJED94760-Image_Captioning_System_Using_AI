# استيراد المكتبات
from transformers import BlipProcessor, BlipForConditionalGeneration, MarianMTModel, MarianTokenizer
import gradio as gr
from PIL import Image

# تحميل نموذج BLIP ومعالج البيانات
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# تحميل نموذج الترجمة
tokenizer = MarianTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-ar")
model_mt = MarianMTModel.from_pretrained("Helsinki-NLP/opus-mt-en-ar")

# دالة لترجمة التوصيفات إلى العربية
def translate_to_arabic(text):
    inputs = tokenizer(text, return_tensors="pt", padding=True)
    translated = model_mt.generate(**inputs)
    translated_text = [tokenizer.decode(t, skip_special_tokens=True) for t in translated]
    return translated_text[0]

# دالة لتوليد التوصيفات
def generate_caption(image, language):
    # معالجة الصورة
    inputs = processor(images=image, return_tensors="pt")
    # توليد التوصيف
    outputs = model.generate(**inputs)
    caption = processor.decode(outputs[0], skip_special_tokens=True)
    
    # ترجمة التوصيف إلى العربية إذا تم اختيارها
    if language == "Arabic":
        caption = translate_to_arabic(caption)
    
    return caption

# إعداد واجهة Gradio
iface = gr.Interface(
    fn=generate_caption,
    inputs=[gr.Image(type="pil"), gr.Dropdown(choices=["English", "Arabic"], label="Select Language")],
    outputs="text",
    title="Image Captioning System",
    description="Upload an image and choose the language for caption generation."
)

# تشغيل واجهة Gradio
iface.launch()
    

