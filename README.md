# Canny Kenar Dedektörü

INF605 Görüntü İşleme dersi, Grup 10 projesi.

Bu projede John Canny'nin 1986'da yayımladığı kenar bulma yöntemini Python ile yazıyoruz. Algoritmayı adım adım kurup sonuçlarımızı OpenCV'deki `cv2.Canny` ile karşılaştıracağız.

Makale: J. Canny, "A computational approach to edge detection," IEEE TPAMI, vol. PAMI-8, no. 6, pp. 679-698, 1986. [doi:10.1109/TPAMI.1986.4767851](https://doi.org/10.1109/TPAMI.1986.4767851)

## Yöntemin adımları

| # | Adım | Ne yapar? |
|---|------|-----------|
| 1 | Gauss yumuşatma | Gürültüyü bastırır, sahte kenarları azaltır |
| 2 | Gradyan hesabı | Her pikselde kenarın şiddetini ve yönünü bulur |
| 3 | Non-maximum suppression | Kalın kenarları tek piksel genişliğe inceltir |
| 4 | Histerezis eşikleme | İki eşikle güçlü kenarları tutar, zayıfları bağlantıya göre ekler |

## Klasörler

```
src/               Algoritma modülleri (gaussian.py, ...)
notebooks/         Ana Jupyter notebook (canny.ipynb)
images/            Test görüntüleri (cameraman, coins: skimage.data)
requirements.txt   Gerekli paketler
```

## Çalıştırma

```bash
pip install -r requirements.txt
jupyter notebook notebooks/
```

## Ekip

| Üye | GitHub |
|-----|--------|
| Emre Kayabaşı | [emrekayabs](https://github.com/emrekayabs) |
| Celal Gürlek | [celalgurlek0](https://github.com/celalgurlek0) |
| Ahmet Efe Kazıcı | [Aefe46](https://github.com/Aefe46) |
| Mücahid Eren Koç | [Eren1511](https://github.com/Eren1511) |
| Kayra Görgeç | [kyr234](https://github.com/kyr234) |

MIT lisansı altındadır, ayrıntılar için [LICENSE](LICENSE) dosyasına bakın.
