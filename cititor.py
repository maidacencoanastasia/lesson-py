from tkinter import *
from tkinter import filedialog
import fitz
from gtts import gTTS
from playsound import playsound

window = Tk()
window.title("convert pdf to audiobook")
window.geometry("600x670")


def open_pdf():
    open_file = filedialog.askopenfilename(
        initialdir="/Users/swayam/Downloads/",
        title="Open PDF file",
        filetypes=(
            ("PDF Files", "*.pdf"),
            ("All Files", "*.*")
        )
    )

    if open_file:
        doc = fitz.Document(open_file)
        total_pages = doc.page_count
        for n in range(total_pages):
            page = doc.load_page(n)
            page_content = page.get_textpage()
            content = page_content.extractText()
            text_box.insert(END, content)

        text = text_box.get(1.0, END)
        tts = gTTS(text, lang='es')
        tts.save("audio.mp3")


text_box = Text(window, height=30, width=60)
text_box.pack(pady=10)


menu = Menu(window)
window.config(menu=menu)

file_menu = Menu(menu, tearoff=False)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_pdf)
file_menu.add_command(label="clear", command=lambda: text_box.delete(1.0, END))
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)

play_btn = Button(text="Play", command=lambda: playsound("audio.mp3"))
play_btn.pack(pady=20)

window.mainloop()
