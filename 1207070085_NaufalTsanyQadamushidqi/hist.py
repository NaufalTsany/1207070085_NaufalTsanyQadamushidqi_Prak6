import numpy as np
import cv2
import matplotlib.pyplot as plt

# Membaca gambar menggunakan OpenCV
img = cv2.imread("image/img-doc2.png")

img_height = img.shape[0] # Tinggi gambar
img_width = img.shape[1] # Lebar gambar
img_channel = img.shape[2] # Channel RGB

# Membuat matriks kosong untuk variable baru
img_grayscale = np.zeros(img.shape, dtype=np.uint8)

# Mengonversi gambar menjadi citra grayscale
for y in range(0, img_height):  # Iterasi baris
    for x in range(0, img_width):  # Iterasi kolom
        red = img[y][x][0]  # Komponen warna merah piksel
        green = img[y][x][1]  # Komponen warna hijau piksel
        blue = img[y][x][2]  # Komponen warna biru piksel
        gray = (int(red) + int(green) + int(blue)) / 3  # Menghitung rata-rata nilai komponen warna
        img_grayscale[y][x] = (gray, gray, gray)  # Menetapkan nilai grayscale ke piksel yang sesuai

# Menampilkan citra grayscale
plt.imshow(img_grayscale)
plt.title("Grayscale")
plt.show()

# Membuat variabel untuk menyimpan data gambar
hg = np.zeros((256))

# Mengisi setiap nilai dalam array hg dengan 0
for x in range(0, 256):
    hg[x] = 0

# Menghitung nilai dari gambar
for y in range(0, img_height):
    for x in range(0, img_width):
        gray = img_grayscale[y][x][0]
        hg[gray] += 1

# Menampilkan Histogram
bins = np.linspace(0, 256, 100)
plt.hist(hg, bins, color="black", alpha=0.5)
plt.title("Histogram")
plt.show()

# Membuat variabel untuk menyimpan data gamba
hgr = np.zeros((256))
hgg = np.zeros((256))
hgb = np.zeros((256))
hgrgb = np.zeros((768))

# Mengisi setiap nilai dalam array hg dengan 0
for x in range(0, 256):
    hgr[x] = 0
    hgg[x] = 0
    hgb[x] = 0

for x in range(0, 768):
    hgrgb[x] = 0

for x in range(0, 256):
    hgr[x] = 0
    hgg[x] = 0
    hgb[x] = 0
    
for x in range(0, 768):
    hgrgb[x] = 0

# th = int(256/64)
temp = [0]
# Menghitung histogram komponen warna (red, green, blue)
for y in range(0, img.shape[0]):  # Iterasi baris
    for x in range(0, img.shape[1]):  # Iterasi kolom
        red = int(img[y][x][0])  # Komponen warna merah
        green = int(img[y][x][1])  # Komponen warna hijau
        blue = int(img[y][x][2])  # Komponen warna biru
        green = green + 256  # Menyesuaikan indeks untuk komponen warna hijau dalam hgrgb
        blue = blue + 512  # Menyesuaikan indeks untuk komponen warna biru dalam hgrgb
        hgrgb[red] += 1  # Menghitung kemunculan nilai piksel merah dalam hgrgb
        hgrgb[green] += 1  # Menghitung kemunculan nilai piksel hijau dalam hgrgb
        hgrgb[blue] += 1  # Menghitung kemunculan nilai piksel biru dalam hgrgb

# Menampilkan histogram RGB
binsrgb = np.linspace(0, 768, 100)
plt.hist(hgrgb, binsrgb, color="black", alpha=0.5)
# plt.plot(hgrgb)
plt.title("Histogram Red Green Blue")
plt.show()

for y in range(0, img_height):
    for x in range(0, img_width):
        red = img[y][x][0] # Komponen warna merah
        green = img[y][x][1] # Komponen warna hijau
        blue = img[y][x][2] # Komponen warna bire
        hgr[red] += 1 # Menghitung kemunculan nilai piksel merah
        hgg[green] += 1 # Menghitung kemunculan nilai piksel hijau
        hgb[blue] += 1 # Menghitung kemunculan nilai piksel biru

# Menampilkan histogram Red
bins = np.linspace(0, 256, 100)
plt.hist(hgr, bins, color="red", alpha=0.5)
plt.title("Histogram Red")
plt.show()

# Menampilkan histogram Green
plt.hist(hgg, bins, color="green", alpha=0.5)
plt.title("Histogram Green")
plt.show()

# Menampilkan histogram Blue
plt.hist(hgb, bins, color="blue", alpha=0.5)
plt.title("Histogram Blue")
plt.show()

# Membuat Matriks kosong
hgk = np.zeros((256))
c = np.zeros((256))

# Inisialisasi array hgk dan c dengan nilai 0
for x in range(0, 256):
    hgk[x] = 0
    c[x] = 0

# Menghitung histogram grayscale
for y in range(0, img_height):  # Iterasi baris
    for x in range(0, img_width):  # Iterasi kolom
        gray = img_grayscale[y][x][0]  # Nilai grayscale piksel
        hgk[gray] += 1  # Menghitung kemunculan nilai piksel grayscale

# Menghitung fungsi kumulatif
c[0] = hgk[0]
for x in range(1, 256):
    c[x] = c[x-1] + hgk[x]  # Menghitung jumlah kumulatif untuk setiap nilai piksel

hmaxk = c[255]  # Nilai maksimum dari fungsi kumulatif

# Normalisasi fungsi kumulatif dalam rentang 0-190
for x in range(0, 256):
    c[x] = 190 * c[x] / hmaxk

# Menampilkan histogram grayscale kumulatif
plt.hist(c, bins, color="black", alpha=0.5)
plt.title("Histogram Grayscale Kumulatif")
plt.show()

# Membuat Matriks kosong baru
hgh = np.zeros((256))
h = np.zeros((256))
c = np.zeros((256))

# Inisialisasi array hgh, h, dan c dengan nilai 0
for x in range(0, 256):
    hgh[x] = 0
    h[x] = 0
    c[x] = 0

# Menghitung histogram grayscale
for y in range(0, img_height):  # Iterasi baris
    for x in range(0, img_width):  # Iterasi kolom
        gray = img_grayscale[y][x][0]  # Nilai grayscale piksel
        hgh[gray] += 1  # Menghitung kemunculan nilai piksel grayscale

# Menghitung fungsi kumulatif
h[0] = hgh[0]
for x in range(1, 256):
    h[x] = h[x-1] + hgh[x]  # Menghitung jumlah kumulatif untuk setiap nilai piksel

# Normalisasi fungsi kumulatif menjadi probabilitas
for x in range(0, 256):
    h[x] = h[x] / (img_height * img_width)

# Menghapus nilai-nilai sebelumnya
for x in range(0, 256):
    hgh[x] = 0

# Melakukan ekualisasi histogram
for y in range(0, img_height):  # Iterasi baris
    for x in range(0, img_width):  # Iterasi kolom
        gray = img_grayscale[y][x][0]  # Nilai grayscale piksel
        gray = h[gray] * 255  # Melakukan ekualisasi pada nilai grayscale
        hgh[int(gray)] += 1  # Menghitung kemunculan nilai piksel grayscale yang telah diekualisasi

# Menghitung fungsi kumulatif ekualisasi histogram
c[0] = hgh[0]
for x in range(1, 256):
     c[x] = c[x-1] + hgh[x]  # Menghitung jumlah kumulatif untuk setiap nilai piksel

hmaxk = c[255]  # Nilai maksimum dari fungsi kumulatif

# Normalisasi fungsi kumulatif ekualisasi histogram dalam rentang 0-190
for x in range(0, 256):
    c[x] = 190 * c[x] / hmaxk

# Menampilkan histogram grayscale hasil ekualisasi
plt.hist(c, bins, color="black", alpha=0.5)
plt.title("Histogram Grayscale Hequalisasi")
plt.show()