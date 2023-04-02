import os
import shutil
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog
from tkinter import messagebox

root = tk.Tk()

#Tite
root.title('File Organizer')

#Fixed Size for tkinter window 
root.resizable(0,0)

#Disabling the close button of tkinter window
def donothing():
    pass
root.protocol('WM_DELETE_WINDOW',donothing)

#logo
logo = Image.open('BG.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row =0)

#icon
root.wm_iconbitmap(default='icon1.ico')

def file_org():
    try:
        
    # Directory
        current_dir = filedialog.askdirectory(initialdir="/")

        for f in os.listdir(current_dir):
            filename, file_ext = os.path.splitext(f)
            try:
                if not file_ext:
                    pass

                elif file_ext in ('.py'):
                    if 'PYTHON' not in os.listdir(current_dir):
                        path = os.path.join(current_dir,"PYTHON")
                        os.mkdir(path)
                    shutil.move(
                        os.path.join(current_dir, f'{filename}{file_ext}'),
                        os.path.join(current_dir, 'PYTHON', f'{filename}{file_ext}'))

                elif file_ext in (".jpeg", ".jpg", ".tiff", ".gif", ".JPG", ".PNG", ".bmp", ".png", ".bpg", "svg",".heif", ".psd"):
                    if 'IMAGES' not in os.listdir(current_dir):
                        path = os.path.join(current_dir,"IMAGES")
                        os.mkdir(path)
                    shutil.move(
                        os.path.join(current_dir, f'{filename}{file_ext}'),
                        os.path.join(current_dir, 'IMAGES', f'{filename}{file_ext}'))

                elif file_ext in (".oxps", ".pages", ".docx", ".doc", ".fdf", ".ods",".odt",
                                  ".pwi", ".xsn", ".xps", ".dotx", ".docm",
                                  ".dox",".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",".pptx"):
                    if 'DOCUMENTS' not in os.listdir(current_dir):
                        path = os.path.join(current_dir,"DOCUMENTS")
                        os.mkdir(path)
                    shutil.move(
                        os.path.join(current_dir, f'{filename}{file_ext}'),
                        os.path.join(current_dir, 'DOCUMENTS', f'{filename}{file_ext}'))    
                
                elif file_ext in (".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",".qt", ".mpg", ".mpeg", ".3gp"):
                    if 'VIDEOS' not in os.listdir(current_dir):
                        path = os.path.join(current_dir,"VIDEOS")
                        os.mkdir(path)
                    shutil.move(
                            os.path.join(current_dir, f'{filename}{file_ext}'),
                            os.path.join(current_dir, 'VIDEOS', f'{filename}{file_ext}'))
                
                elif file_ext in (".html5", ".html", ".htm", ".xhtml"):
                    if 'HTML' not in os.listdir(current_dir):
                        path = os.path.join(current_dir,"HTML")
                        os.mkdir(path)
                    shutil.move(
                            os.path.join(current_dir, f'{filename}{file_ext}'),
                            os.path.join(current_dir, 'HTML', f'{filename}{file_ext}'))
                
                elif file_ext in (".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",".dmg", ".rar", ".xar", ".zip"):
                    if 'ARCHIVES' not in os.listdir(current_dir):
                        path = os.path.join(current_dir,"ARCHIVES")
                        os.mkdir(path)
                    shutil.move(
                            os.path.join(current_dir, f'{filename}{file_ext}'),
                            os.path.join(current_dir, 'ARCHIVES', f'{filename}{file_ext}'))

                elif file_ext in (".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"):
                    if 'AUDIO' not in os.listdir(current_dir):
                        path = os.path.join(current_dir,"AUDIO")
                        os.mkdir(path)
                    shutil.move(
                            os.path.join(current_dir, f'{filename}{file_ext}'),
                            os.path.join(current_dir, 'AUDIO', f'{filename}{file_ext}'))
                
                elif file_ext in (".txt", ".in", ".out"):
                    if 'TEXT' not in os.listdir(current_dir):
                        path = os.path.join(current_dir,"TEXT")
                        os.mkdir(path)
                    shutil.move(
                            os.path.join(current_dir, f'{filename}{file_ext}'),
                            os.path.join(current_dir, 'TEXT', f'{filename}{file_ext}'))
                
                elif file_ext in (".pdf"):
                    if 'PDF' not in os.listdir(current_dir):
                        path = os.path.join(current_dir,"PDF")
                        os.mkdir(path)
                    shutil.move(
                            os.path.join(current_dir, f'{filename}{file_ext}'),
                            os.path.join(current_dir, 'PDF', f'{filename}{file_ext}'))
                    
                elif file_ext in (".epub", ".ePub", ".EPUB"):
                    if 'BOOKS' not in os.listdir(current_dir):
                        path = os.path.join(current_dir,"BOOKS")
                        os.mkdir(path)
                    shutil.move(
                            os.path.join(current_dir, f'{filename}{file_ext}'),
                            os.path.join(current_dir, 'BOOKS', f'{filename}{file_ext}'))    
                
                elif file_ext in (".xml"):
                    if 'XML' not in os.listdir(current_dir):
                        path = os.path.join(current_dir,"XML")
                        os.mkdir(path)
                    shutil.move(
                            os.path.join(current_dir, f'{filename}{file_ext}'),
                            os.path.join(current_dir, 'XML', f'{filename}{file_ext}'))
                
                elif file_ext in (".exe"):
                    if 'EXE' not in os.listdir(current_dir):
                        path = os.path.join(current_dir,"EXE")
                        os.mkdir(path)
                    shutil.move(
                            os.path.join(current_dir, f'{filename}{file_ext}'),
                            os.path.join(current_dir, 'EXE', f'{filename}{file_ext}'))
                
                elif file_ext in (".sh"):
                    if 'SHELL' not in os.listdir(current_dir):
                        path = os.path.join(current_dir,"SHELL")
                        os.mkdir(path)
                    shutil.move(
                            os.path.join(current_dir, f'{filename}{file_ext}'),
                            os.path.join(current_dir, 'SHELL', f'{filename}{file_ext}'))
                
                else:
                    if 'Other files' not in os.listdir(current_dir):
                        path = os.path.join(current_dir,"Other files")
                        os.mkdir(path)
                    shutil.move(
                        os.path.join(current_dir, f'{filename}{file_ext}'),
                        os.path.join(current_dir, 'Other files', f'{filename}{file_ext}'))                 

            except (FileNotFoundError, PermissionError):
                pass
        messagebox.showinfo("File Organiser","Your files are organized successfully")
        answer = messagebox.askyesno("File Organizer","Do you want to organise another folder?")
        return answer
        
    except:
        messagebox.showinfo("File Organiser","You haven't selected any folder")

while True:
    x = file_org()
    if x:
        continue
    else:
        break
root.destroy()
root.mainloop()
