#import library yng digunakan
import numpy as np
import imageio
import matplotlib.pyplot as plt

#membaca gambar menggunakan imageio
img = imageio.imread("image/img-doc2.png")


img_height = img.shape[0] # digunakan untuk mendapatkan tinggi (jumlah baris) dari gambar.
img_width = img.shape[1] # digunakan untuk mendapatkan lebar (jumlah kolom) dari gambar.
img_channel = img.shape[2] # digunakan untuk mendapatkan jumlah kanal warna (misalnya 3 untuk gambar RGB).
img_type = img.dtype # digunakan untuk mendapatkan tipe data dari piksel gambar (misalnya uint8 untuk representasi nilai 0-255).

# membuat matriks kosong untuk flip horizontal & vertical
img_flip_horizontal = np.zeros(img.shape, img_type)
img_flip_vertical = np.zeros(img.shape, img_type)

#untuk melakukan flip horizontal dan flip vertical, daripada menggunakan loop for. Fungsi ini akan membuat kode lebih ringkas dan efisien.
for y in range(0, img_height):
    for x in range(0, img_width):
        for c in range(0, img_channel):
            img_flip_horizontal[y][x][c] = img[y][img_width-1-x][c]
    
for y in range(0, img_height):
    for x in range(0, img_width):
        for c in range(0, img_channel):
            img_flip_vertical[y][x][c] = img[img_height-1-y][x][c]

# menampilkan plot
plt.imshow(img_flip_horizontal)
plt.title("Flip Horizontal")
plt.show()
plt.imshow(img_flip_vertical)
plt.title("Flip Vertical")
plt.show()