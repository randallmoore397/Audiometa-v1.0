from tkinter import filedialog

class Controller:
    def __init__(self) -> None:
        pass
    
    def select_audio(self,):  
        self.filename2 = filedialog.askopenfilename(initialdir = "/",title="Select Program 2",filetype=(("All Files", "*.*"),("PDF",".pdf"),("Shortcut",".lnk"),("MS Word",".docx")))
        self.program_two_label.insert(0,self.filename2)