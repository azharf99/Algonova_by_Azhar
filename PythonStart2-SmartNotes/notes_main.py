from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QHBoxLayout, \
                            QListWidget, QLabel, QVBoxLayout, QPushButton, QInputDialog
application = QApplication([])
window = QWidget()
window.setWindowTitle("Aplikasi Smart Note Azhar")
window.resize(900, 600)


notes = []

text_editor = QTextEdit()
list_of_notes = QListWidget()
list_of_notes_label = QLabel("List of notes")
create_note_button = QPushButton("Create note")
delete_note_button = QPushButton("Delete note")
save_note_button = QPushButton("Save note")

list_of_tags = QListWidget()
list_of_tags_label = QLabel("List of tags")

search_bar = QTextEdit('')
search_bar.setPlaceholderText("Search tag")
search_bar.setFixedHeight(30)
add_tag_button = QPushButton("Add to note")
delete_tag_button = QPushButton("Untag from note")
search_note_button = QPushButton("Search note by tag")

layout_utama = QHBoxLayout()
layout_vertical_1 = QVBoxLayout()
layout_vertical_1.addWidget(text_editor)
layout_vertical_2 = QVBoxLayout()
layout_vertical_2.addWidget(list_of_notes_label)
layout_vertical_2.addWidget(list_of_notes)

row_button_create_detele = QHBoxLayout()
row_button_create_detele.addWidget(create_note_button)
row_button_create_detele.addWidget(delete_note_button)

row_button_save = QHBoxLayout()
row_button_save.addWidget(save_note_button)

layout_vertical_2.addLayout(row_button_create_detele)
layout_vertical_2.addLayout(row_button_save)

layout_vertical_2.addWidget(list_of_tags_label)
layout_vertical_2.addWidget(list_of_tags)
layout_vertical_2.addWidget(search_bar)

row_button_add_delete_tag = QHBoxLayout()
row_button_add_delete_tag.addWidget(add_tag_button)
row_button_add_delete_tag.addWidget(delete_tag_button)

row_search_note = QHBoxLayout()
row_search_note.addWidget(search_note_button)

layout_vertical_2.addLayout(row_button_add_delete_tag)
layout_vertical_2.addLayout(row_search_note)

layout_utama.addLayout(layout_vertical_1, stretch=2)
layout_utama.addLayout(layout_vertical_2, stretch=1)

window.setLayout(layout_utama)

def show_note():
    key = list_of_notes.selectedItems()[0].text()
    print(key)
    for note in notes:
        if note[0] == key:
            text_editor.setText(note[1])
            list_of_tags.clear()
            list_of_tags.addItems(note[2])


def add_note():
    note_name, ok = QInputDialog.getText(window, "Add note", "Note name: ")
    if ok and note_name != "":
        note = list()
        note = [note_name, '', []]
        notes.append(note)
        list_of_notes.addItem(note[0])
        list_of_tags.addItems(note[2])
        print(notes)
        with open(str(len(notes)-1)+".txt", "w") as file:
            file.write(note[0]+'\n')


def save_note():
    if list_of_notes.selectedItems():
        key = list_of_notes.selectedItems()[0].text()
        index = 0
        for note in notes:
            if note[0] == key:
                note[1] = text_editor.toPlainText()
                with open(str(index)+".txt", "w") as file:
                    file.write(note[0]+'\n')
                    file.write(note[1]+'\n')
                    for tag in note[2]:
                        file.write(tag+' ')
                    file.write('\n')
            index += 1
        print(notes)
    else:
        print("Note to save is not selected!")


#event handling
list_of_notes.itemClicked.connect(show_note)
create_note_button.clicked.connect(add_note)
save_note_button.clicked.connect(save_note)


#app startup 
window.show()


name = 0
note = []
while True:
    filename = str(name)+".txt"
    try:
        with open(filename, "r", encoding='utf-8') as file:
            for line in file:
                line = line.replace('\n', '')
                note.append(line)
        tags = note[2].split(' ')
        note[2] = tags
        
        notes.append(note)
        note = []
        name += 1


    except IOError:
        break


print(notes)
for note in notes:
    list_of_notes.addItem(note[0])

application.exec()