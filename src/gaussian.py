# Canny'nin 1. adımı: görüntüyü okuma ve Gauss ile yumuşatma

import cv2
import numpy as np


def goruntu_yukle(dosya_yolu):
    img = cv2.imread(str(dosya_yolu))

    if img is None:
        raise FileNotFoundError("Görüntü bulunamadı: " + str(dosya_yolu))

    # renkliyse gri tonlamaya çevir
    if len(img.shape) == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    return img


def gauss_kernel(sigma):
    if sigma <= 0:
        raise ValueError("sigma pozitif olmalı")

    r = int(np.ceil(3 * sigma))
    boyut = 2 * r + 1

    kernel = np.zeros((boyut, boyut))

    for i in range(boyut):
        for j in range(boyut):
            x = j - r
            y = i - r
            kernel[i, j] = np.exp(-(x * x + y * y) / (2 * sigma * sigma))

    # toplam 1 olsun ki parlaklık değişmesin
    kernel = kernel / np.sum(kernel)

    return kernel


def gauss_yumusat(img, sigma):
    if len(img.shape) != 2:
        raise ValueError("gri tonlamalı görüntü bekleniyor")

    kernel = gauss_kernel(sigma)
    img_float = img.astype(np.float64)

    # kenarlarda görüntüyü aynalıyoruz, böylece boyut değişmiyor
    sonuc = cv2.filter2D(img_float, -1, kernel, borderType=cv2.BORDER_REFLECT_101)

    return sonuc
