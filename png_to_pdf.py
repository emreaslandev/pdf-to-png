import os
from PIL import Image

def pngleri_pdfye_cevir(klasor_yolu):
    for dosya in os.listdir(klasor_yolu):
        if dosya.lower().endswith('.png'):
            png_yolu = os.path.join(klasor_yolu, dosya)
            pdf_adi = f"{os.path.splitext(dosya)[0]}.pdf"
            pdf_yolu = os.path.join(klasor_yolu, pdf_adi)
            with Image.open(png_yolu) as img:
                img = img.convert('RGB')
                img.save(pdf_yolu, 'PDF')
            print(f"{dosya} dönüştürüldü.")

if __name__ == "__main__":
    klasor = input("PNG dosyalarının bulunduğu klasörün yolunu girin: ")
    pngleri_pdfye_cevir(klasor)