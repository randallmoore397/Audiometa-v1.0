# 8 -*-
# # Copyright (c) Juliette Monsel 2018
# # For license see LICENSE
# from ttkwidgets import ScaleEntry
# import tkinter as tk
# window = tk.Tk()
# scaleentry = ScaleEntry(window, scalewidth=200, entrywidth=3, from_=0, to=20)
# scaleentry.config_entry(justify='center')
# scaleentry.pack()
# window.mainloop()


try:
    data=open("C:/Users/afro/Music/Audio/Dansaki.mp3",'rb').name.split('/')
    print(data[-1])
except:
    print("Error Splitting audio filename")