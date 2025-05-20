import os
from pdf2image import convert_from_path

def pdfleri_pngye_cevir(klasor_yolu):
    for dosya in os.listdir(klasor_yolu):
        if dosya.lower().endswith('.pdf'):
            pdf_yolu = os.path.join(klasor_yolu, dosya)
            sayfalar = convert_from_path(pdf_yolu)
            for i, sayfa in enumerate(sayfalar):
                png_adi = f"{os.path.splitext(dosya)[0]}.png"
                png_yolu = os.path.join(klasor_yolu, png_adi)
                sayfa.save(png_yolu, 'PNG')
            print(f"{dosya} dönüştürüldü.")

if __name__ == "__main__":
    klasor = input("PDF dosyalarının bulunduğu klasörün yolunu girin: ")
    pdfleri_pngye_cevir(klasor)