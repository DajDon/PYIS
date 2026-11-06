import customtkinter as ctk
import webbrowser
from pathlib import Path

root = ctk.CTk()
root.title("PYIS")
root.geometry("350x550")
root.config(background="#16191d")
root.resizable(False, False)
root.iconbitmap(Path(__file__).parent / "assets" / "logo.ico")

def openDajdon():
    webbrowser.open("https://dajdon.hu")

def generateScript():
    fileName = fileNameEntry.get().strip()
    logo = logoEntry.get().strip()
    folders = foldersEntry.get().strip()

    script = "python -m PyInstaller --clean --noconfirm --onefile --windowed"

    if logo:
        script += f" --icon={logo}"

    if folders:
        for folder in folders.split(";"):
            folder = folder.strip()

            if folder:
                script += f' --add-data "{folder};{folder}"'

    script += f" {fileName}"

    generatedScript.delete("1.0", "end")
    generatedScript.insert("1.0", script)

def copyScript():
    text = generatedScript.get("1.0", "end-1c")
    root.clipboard_clear()
    root.clipboard_append(text)
    root.update()


fileNameLabel = ctk.CTkLabel(
    root,
    text=("File Name"),
    font=("Arial", 20),
    text_color="white",
    bg_color="#16191d"
)
fileNameLabel.place(relx=0.2, rely=0.12, anchor="center")

fileNameEntry = ctk.CTkEntry(
    root,
    font=("Arial", 15),
    text_color="white",
    bg_color="#1d1f23",
    width=300,
    placeholder_text="test.pyw"
)
fileNameEntry.place(relx=0.5, rely=0.19, anchor="center")



logoEntryLabel = ctk.CTkLabel(
    root,
    text=("Logo"),
    font=("Arial", 20),
    text_color="white",
    bg_color="#16191d"
) 
logoEntryLabel.place(relx=0.15, rely=0.28, anchor="center")

logoEntry = ctk.CTkEntry(
    root,
    font=("Arial", 15),
    text_color="white",
    bg_color="#1d1f23",
    width=300,
    placeholder_text="assets/logo.ico"
)
logoEntry.place(relx=0.5, rely=0.35, anchor="center")



foldersEntryLabel = ctk.CTkLabel(
    root,
    text=("Folders"),
    font=("Arial", 20),
    text_color="white",
    bg_color="#16191d"
)
foldersEntryLabel.place(relx=0.18, rely=0.45, anchor="center")

foldersEntry = ctk.CTkEntry(
    root,
    font=("Arial", 15),
    text_color="white",
    bg_color="#1d1f23",
    width=300,
    placeholder_text="scripts"
)
foldersEntry.place(relx=0.5, rely=0.52, anchor="center")



generatedScript = ctk.CTkTextbox(
    root,
    width=240,
    height=100,
    fg_color="#1d1f23",
    bg_color="#16191d",

)
generatedScript.place(relx=0.41, rely=0.675, anchor="center")



generatedScriptCopyButton = ctk.CTkButton(
    root,
    width=10,
    height=98,
    bg_color="#1d1f23",
    text="Copy",
    command=copyScript
)
generatedScriptCopyButton.place(relx=0.855, rely=0.675, anchor="center")



generateButton = ctk.CTkButton(
    root,
    font=("Arial", 15),
    text_color="white",
    bg_color="#1d1f23",
    text="Generate",
    width=200,
    height=40,
    command=generateScript
)
generateButton.place(relx=0.5, rely=0.85, anchor="center")



dajdonButton = ctk.CTkButton(
    root,
    font=("Arial", 10),
    text=("dajdon.hu"),
    fg_color="#16191d",
    hover_color="#16191d",
    bg_color="#16191d",
    width=1,
    height=1,
    command=openDajdon
)
dajdonButton.place(relx=0.5, rely=0.96, anchor="center")

root.mainloop()