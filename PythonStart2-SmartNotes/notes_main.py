from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QListWidget, QLabel


application = QApplication([])
window = QWidget()
window.setWindowTitle("Smart Note Buatanku")
window.resize(1200, 900)

list_notes = QListWidget()
list_note_label = QLabel("Daftar Tulisan")

layout_utama = QHBoxLayout()

layout_vertikal = QVBoxLayout()
layout_vertikal.addWidget(list_note_label)
layout_vertikal.addWidget(list_notes)

layout_utama.addLayout(layout_vertikal)
window.setLayout(layout_utama)


window.show()
application.exec()