import os
from google.cloud import vision
import io

# Google Vision API için hizmet hesabı dosyasını ayarla
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ""

    #Google Vision API kullanarak el yazısı OCR işlemini gerçekleştirir.
def perform_handwritten_ocr(image_path, lang='eng+tur'):

    try:
        client = vision.ImageAnnotatorClient()

        # Görüntüyü yükle
        with io.open(image_path, 'rb') as image_file:
            content = image_file.read()

        image = vision.Image(content=content)

        # Dil ipuçları ile el yazısı OCR işlemi
        image_context = vision.ImageContext(language_hints=lang.split("+"))
        response = client.document_text_detection(image=image, image_context=image_context)

        # OCR sonucunu döndür
        if response.error.message:
            raise Exception(f"API Hatası: {response.error.message}")

        return response.full_text_annotation.text if response.full_text_annotation else "Hiçbir metin algılanamadı."
    except Exception as e:
        return f"Hata oluştu: {e}"
