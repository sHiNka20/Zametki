import tkinter as tk
from tkinter import messagebox

notes_file = "notes.txt"
notes = {}


def save_notes_to_file():
    with open(notes_file, "w") as file:
        for title, note in notes.items():
            file.write(f"{title}:\n{note}\n---\n")
    messagebox.showinfo("Сохранено", "Заметки сохранены в файл!")


def load_notes_from_file():
    try:
        with open(notes_file, "r") as file:
            lines = file.readlines()
            note_title = ""
            note_text = ""
            for line in lines:
                if line.strip() == "---":
                    if note_title and note_text:
                        notes[note_title] = note_text
                    note_title = ""
                    note_text = ""
                elif note_title == "":
                    note_title = line.strip().replace(":", "")
                else:
                    note_text += line
    except FileNotFoundError:
        messagebox.showerror("Ошибка", "Файл заметок не найден. Создан новый файл, перезапустите программу.")
        open(notes_file, "x")

def save_note():
    note_title = title_entry.get()
    note_text = text.get(1.0, tk.END)

    notes[note_title] = note_text
    save_notes_to_file()


def load_notes():
    note_list.delete(0, tk.END)

    for title in notes:
        note_list.insert(tk.END, title)


def load_note():
    selected_title = note_list.get(tk.ACTIVE)
    selected_note = notes[selected_title]

    title_entry.delete(0, tk.END)
    title_entry.insert(tk.END, selected_title)

    text.delete(1.0, tk.END)
    text.insert(tk.END, selected_note)


def delete_note():
    selected_title = note_list.get(tk.ACTIVE)
    del notes[selected_title]
    save_notes_to_file()
    load_notes()


root = tk.Tk()
root.title("Заметки")

title_label = tk.Label(root, text="Заголовок:")
title_label.pack()

title_entry = tk.Entry(root)
title_entry.pack()

text = tk.Text(root)
text.pack()

save_button = tk.Button(root, text="Сохранить заметку", command=save_note)
save_button.pack()

note_list = tk.Listbox(root)
note_list.pack()

load_notes_from_file()
load_notes()

load_notes_button = tk.Button(root, text="Загрузить заметки", command=load_notes)
load_notes_button.pack()

load_button = tk.Button(root, text="Загрузить заметку", command=load_note)
load_button.pack()

delete_button = tk.Button(root, text="Удалить заметку", command=delete_note)
delete_button.pack()

root.mainloop()