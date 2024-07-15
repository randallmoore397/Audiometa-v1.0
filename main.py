import tkinter as tk
from tkinter import ttk
from app import App



def main():
    root = tk.Tk()
    # root = ThemedTk(theme="plastik")
    app = App(root)
    style = ttk.Style()
    
    # style.configure('TButton',side='center')

    # style.theme_use('alt')
    # style.configure('TButton', background = 'blue', foreground = 'white')
    # style.map('TButton', background=[('active','red')])
        
    app.mainloop()


if __name__ == '__main__':
    main()


