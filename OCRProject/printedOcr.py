# ocr_engine.py
import cv2
import pytesseract

# Tesseract OCR motorunun yolu
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Görüntüde OCR işlemini gerçekleştirir.
def perform_ocr(image_path, lang='eng+tur'):
    
    try:
        # Görüntüyü yükle
        image = cv2.imread(image_path)
        if image is None:
            return "Hata: Görüntü yüklenemedi. Dosya yolunu kontrol edin."

        # Görüntüyü grileştir ve threshold uygula(daha iyi sonuçlar için)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, thresh_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        # OCR işlemi
        text = pytesseract.image_to_string(thresh_image, lang=lang)
        return text if text.strip() else "Görüntüde herhangi bir metin bulunamadı."
    except Exception as e:
        return f"Hata oluştu: {e}"
