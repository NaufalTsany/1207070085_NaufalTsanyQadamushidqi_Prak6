import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("image/messi.jfif")

img_height = img.shape[0]
img_width = img.shape[1]
img_channel = img.shape[2]

img_inversi = np.zeros(img.shape, dtype=np.uint8)

def inversi_grayscale(nilai):
    # Iterasi melalui setiap piksel dalam gambar
    for y in range(0, img_height):  # Iterasi baris
        for x in range(0, img_width):  # Iterasi kolom
            # Mendapatkan komponen warna merah, hijau, dan biru dari piksel
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            
            # Menghitung nilai grayscale sebagai rata-rata dari komponen warna
            gray = (int(red) + int(green) + int(blue)) / 3
            
            # Melakukan inversi dengan mengurangi nilai grayscale dari nilai yang diberikan
            gray = nilai - gray
            
            # Mengupdate nilai piksel dalam gambar inversi grayscale
            img_inversi[y][x] = (gray, gray, gray)

def inversi_rgb(nilai):
    # Iterasi melalui setiap piksel dalam gambar
    for y in range(0, img_height):  # Iterasi baris
        for x in range(0, img_width):  # Iterasi kolom
            # Mendapatkan komponen warna merah, hijau, dan biru dari piksel
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            
            # Melakukan inversi pada nilai komponen warna merah
            red = nilai - red
            
            # Melakukan inversi pada nilai komponen warna hijau
            green = nilai - green
            
            # Melakukan inversi pada nilai komponen warna biru
            blue = nilai - blue
            
            # Mengupdate nilai piksel dalam gambar inversi RGB
            img_inversi[y][x] = (red, green, blue)

def log(c):
    # Iterasi melalui setiap piksel dalam gambar
    for y in range(0, img_height):  # Iterasi baris
        for x in range(0, img_width):  # Iterasi kolom
            # Mendapatkan komponen warna merah, hijau, dan biru dari piksel
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            
            # Menghitung nilai grayscale sebagai rata-rata dari komponen warna
            gray = (int(red) + int(green) + int(blue)) / 3
            
            # Melakukan transformasi logaritmik dengan menggunakan parameter c
            gray = int(c * np.log(gray + 1))
            
            # Memastikan bahwa nilai grayscale berada dalam rentang 0-255
            if gray > 255:
                gray = 255
            if gray < 0:
                gray = 0
            
            # Mengupdate nilai piksel dalam gambar hasil transformasi logaritmik
            img_log[y][x] = (gray, gray, gray)

def inlog(c):
    # Iterasi melalui setiap piksel dalam gambar
    for y in range(0, img_height):  # Iterasi baris
        for x in range(0, img_width):  # Iterasi kolom
            # Mendapatkan komponen warna merah, hijau, dan biru dari piksel
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            
            # Menghitung nilai grayscale sebagai rata-rata dari komponen warna
            gray = (int(red) + int(green) + int(blue)) / 3
            
            # Melakukan transformasi logaritmik terbalik dengan menggunakan parameter c
            gray = int(c * np.log(255 - gray + 1))
            
            # Memastikan bahwa nilai grayscale berada dalam rentang 0-255
            if gray > 255:
                gray = 255
            if gray < 0:
                gray = 0
            
            # Mengupdate nilai piksel dalam gambar hasil transformasi logaritmik terbalik
            img_inlog[y][x] = (gray, gray, gray)

def nthpower(c, y):
    # Menghitung nilai ambang dan pangkat dalam skala 0-1
    thc = c / 100
    thy = y / 100
    
    # Iterasi melalui setiap piksel dalam gambar
    for y in range(0, img_height):  # Iterasi baris
        for x in range(0, img_width):  # Iterasi kolom
            # Mendapatkan komponen warna merah, hijau, dan biru dari piksel
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            
            # Menghitung nilai grayscale sebagai rata-rata dari komponen warna
            gray = (int(red) + int(green) + int(blue)) / 3
            
            # Melakukan transformasi pangkat dengan menggunakan parameter c dan y
            gray = int(thc * pow(gray, thy))
            
            # Memastikan bahwa nilai grayscale berada dalam rentang 0-255
            if gray > 255:
                gray = 255
            if gray < 0:
                gray = 0
            
            # Mengupdate nilai piksel dalam gambar hasil transformasi pangkat
            img_nthpower[y][x] = (gray, gray, gray)

def nthrootpower(c, y):
    # Menghitung nilai ambang dan akar pangkat dalam skala 0-1
    thc = c / 100
    thy = y / 100
    
    # Iterasi melalui setiap piksel dalam gambar
    for y in range(0, img_height):  # Iterasi baris
        for x in range(0, img_width):  # Iterasi kolom
            # Mendapatkan komponen warna merah, hijau, dan biru dari piksel
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            
            # Menghitung nilai grayscale sebagai rata-rata dari komponen warna
            gray = (int(red) + int(green) + int(blue)) / 3
            
            # Melakukan transformasi akar pangkat dengan menggunakan parameter c dan y
            gray = int(thc * pow(gray, 1./thy))
            
            # Memastikan bahwa nilai grayscale berada dalam rentang 0-255
            if gray > 255:
                gray = 255
            if gray < 0:
                gray = 0
            
            # Mengupdate nilai piksel dalam gambar hasil transformasi akar pangkat
            img_nthpower[y][x] = (gray, gray, gray)

img_log = np.zeros(img.shape, dtype=np.uint8)
img_inlog = np.zeros(img.shape, dtype=np.uint8)
img_nthpower = np.zeros(img.shape, dtype=np.uint8)
img_nthrootpower = np.zeros(img.shape, dtype=np.uint8)

# Menjalankan fungsi inversi_grayscale dengan parameter nilai 255 untuk melakukan inversi grayscale pada gambar
inversi_grayscale(255)
plt.imshow(img_inversi)
plt.title("Inversi Grayscale")
plt.show()

# Menjalankan fungsi inversi_rgb dengan parameter nilai 255 untuk melakukan inversi RGB pada gambar
inversi_rgb(255)
plt.imshow(img_inversi)
plt.title("Inversi RGB")
plt.show()

# Menampilkan log
log(30)
plt.imshow(img_log)
plt.title("Log")
plt.show()

# Menampilkan inLog
inlog(30)
plt.imshow(img_inlog)
plt.title("Inversi & Log")
plt.show()

# Menampilkan nthpower
nthpower(50, 100)
plt.imshow(img_nthpower)
plt.title("Nth Power")
plt.show()

# Menampilkan nthrootpower
nthrootpower(50, 100)
plt.imshow(img_nthrootpower)
plt.title("Nth Root Power")
plt.show()