import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QRadioButton, QPushButton, QFileDialog
from PyQt5.QtCore import Qt
from printedOcr import perform_ocr  # Printed OCR için Tesseract fonksiyonu
from handwrittenOcr import perform_handwritten_ocr  # Handwritten OCR için Google Vision API fonksiyonu

class OCRApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Pencere ayarları
        self.setWindowTitle("OCR Application")
        self.setGeometry(300, 300, 400, 300)

        # CSS ile tasarım
        self.setStyleSheet("""
            QWidget {
                background-color: #800080; /* Arka plan mor */
                font-family: Arial;
                color: white; /* Yazılar beyaz */
                font-weight: bold;
            }
            QRadioButton {
                font-size: 16px;
                padding: 5px;
            }
            QRadioButton::indicator {
                width: 18px;
                height: 18px;
                border: 2px solid white;
                background-color: transparent;
            }
            QRadioButton::indicator:checked {
                background-color: rgb(75, 0, 75);
            }
            QPushButton {
                background-color: rgb(75, 0, 75);
                color: white;
                font-size: 14px;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #f0f0f0;
                color: #800080;
            }
        """)

        # Layout
        layout = QVBoxLayout()

        # Başlık
        title_label = QLabel("OCR Application")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 20px; font-weight: bold;")
        layout.addWidget(title_label)

        # Radio Buttonlar
        self.handwritten_radio = QRadioButton("Handwritten text OCR")
        self.printed_radio = QRadioButton("Printed text OCR")
        layout.addWidget(self.handwritten_radio)
        layout.addWidget(self.printed_radio)

        # Dosya Seçme Butonu
        self.file_button = QPushButton("Select Image")
        self.file_button.clicked.connect(self.select_file)
        layout.addWidget(self.file_button)

        # Layout'u uygula
        self.setLayout(layout)

    def select_file(self):
        # Dosya seçme penceresi
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp)")
        if not file_path:
            return  # Dosya seçilmediyse işlemi sonlandır

        # OCR modu ve dil parametresi
        try:
            if self.handwritten_radio.isChecked():
                extracted_text = perform_handwritten_ocr(file_path, lang="eng+tur")
            elif self.printed_radio.isChecked():
                extracted_text = perform_ocr(file_path, lang="eng+tur")
            else:
                print("Lütfen bir OCR modu seçin.")
                return

            # OCR sonucu .txt dosyasına kaydediliyor
            output_path = "C:/Users/forra/APROGRAMMING/goruntuis/Outputs/OCR_Result.txt"
            self.save_to_txt(extracted_text, output_path)
            print(f"OCR sonucu başarıyla kaydedildi: {output_path}")
        except Exception as e:
            print(f"OCR işlemi sırasında hata oluştu: {e}")

    #OCR sonucunu bir .txt dosyasına kaydeder.
    def save_to_txt(self, text, output_path):

        try:
            with open(output_path, "w", encoding="utf-8") as file:
                file.write(text)
        except Exception as e:
            print(f".txt dosyasına yazarken hata oluştu: {e}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ocr_app = OCRApp()
    ocr_app.show()
    sys.exit(app.exec_())
