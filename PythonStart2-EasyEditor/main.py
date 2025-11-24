from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, \
                            QHBoxLayout, QVBoxLayout, QListWidget,\
                            QLabel, QFileDialog
import os

def filter(file):
    extentions = ["jpg", "jpeg", "png"]
    filename, extention = file.split(".")
    if extention.lower() in extentions:
        daftar_file.addItem(file)
    return file 

def getImagesFolder():
    workdir = QFileDialog.getExistingDirectory()
    files_in_folder = os.listdir(workdir)
    for file in files_in_folder:
        filter(file)

# Konfigurasi untuk jendela Aplikasi-nya
app = QApplication([])
window = QWidget()
window.resize(700, 400)
window.setWindowTitle('Easy Editor')

# Kode di bawah ini untuk menambilkan beberapa widget
tombol_folder = QPushButton("Folder")
tombol_left = QPushButton("Left")
tombol_right = QPushButton("Right")
tombol_mirror = QPushButton("Mirror")
tombol_sharpness = QPushButton("Sharpness")
tombol_bnw = QPushButton("B/W")
daftar_file = QListWidget()

label_image = QLabel("Gambar nanti ditaruh disini!")

# Bikin baris utama
baris_utama = QHBoxLayout()
# Bikin kolom 1
kolom1 = QVBoxLayout()
kolom1.addWidget(tombol_folder)
kolom1.addWidget(daftar_file)

baris_utama.addLayout(kolom1)
kolom2 = QVBoxLayout()
kolom2.addWidget(label_image)

baris_kolom2 = QHBoxLayout()
baris_kolom2.addWidget(tombol_left)
baris_kolom2.addWidget(tombol_right)
baris_kolom2.addWidget(tombol_mirror)
baris_kolom2.addWidget(tombol_sharpness)
baris_kolom2.addWidget(tombol_bnw)

kolom2.addLayout(baris_kolom2)
baris_utama.addLayout(kolom2, stretch=3)

window.setLayout(baris_utama)

tombol_folder.clicked.connect(getImagesFolder)


window.show()
app.exec()


