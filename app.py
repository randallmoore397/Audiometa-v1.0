import tkinter as tk 
from tkinter import ttk, PhotoImage,filedialog
from pathlib import Path
from tkinter import messagebox
from turtle import color
# from ttkthemes import ThemedTk
from tkcalendar import Calendar,DateEntry
import audio_metadata
from datetime import datetime
from Writing import Metadata

#? Master frame for the entire application ( As class)
class App(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        # self.master.configure(bd=0,border=0,padx=0,pady=0)
        self.pack()
        
        self.master.title("AudioMeta")
        self.master.geometry("800x510")
        self.master.resizable(width=False,height=False)

        #Get the current working directory (absolute path)
        curr_dir = Path.cwd()
        self.master.iconbitmap(f"{curr_dir}\logo.ico")
        
        #************ CREATING MENU AND SUBMENU HERE ************
        self.menu_bar = tk.Menu(master,background="#FFF",relief="flat") #background="#2187f4"
        master.config(menu=self.menu_bar)
        self.file_sub_menu = tk.Menu(self.menu_bar,tearoff=0,background="#FFF",activebackground="#1e63ef")
        self.edit_sub_menu = tk.Menu(self.menu_bar,tearoff=0)
        self.setting_sub_menu = tk.Menu(self.menu_bar,tearoff=0)
        self.help_sub_menu = tk.Menu(self.menu_bar,tearoff=0)
        
        #******* FILE SUBMENUS CREATED HERE 
        self.menu_bar.add_cascade(label='File',menu=self.file_sub_menu,background="#FFF")
        self.file_sub_menu.add_command(label='Open Project')
        self.file_sub_menu.add_command(label='Close Project')
        self.file_sub_menu.add_command(label='Save Project')
        self.file_sub_menu.add_command(label='Exit')
        
        #******* EDIT SUBMENUS CREATED HERE 
        self.menu_bar.add_cascade(label='Edit',menu=self.edit_sub_menu)
        self.edit_sub_menu.add_command(label='Open it')
        
        #******* SETTINGS SUBMENUS CREATED HERE 
        self.menu_bar.add_cascade(label='Settings',menu=self.setting_sub_menu)
        self.setting_sub_menu.add_command(label='Open it')
        
        #******* HELP SUBMENUS CREATED HERE 
        self.menu_bar.add_cascade(label='About',menu=self.help_sub_menu)
        self.help_sub_menu.add_command(label='Open it')
        
        
        
        #**************** THE MAIN FRAME TO HOLE THE CAPTION TEXT AND NOTEBOOOK **********
        main_frame = tk.Frame(width="400",height="505",background="#3a5998")
        main_frame.pack()
        
        caption = ttk.Label(main_frame, text="Audiometa v1.0",font="Calibri 26 bold",background="#3a5998",foreground="white",borderwidth=2)
        caption.pack()
        
        #************************ CREATING THE NOTEBOOX HERE ****************************
        self.noteBookTab = ttk.Notebook(main_frame) # ttk.Notebook(master)
        # self.noteBookTab.configure(cursor="")
        self.noteBookTab.pack(side="left",expand=1,ipady=10,fill="both")
        
        win_weight = self.winfo_screenwidth()
        win_height = self.winfo_screenheight()
        
        self.single_file = tk.Frame(self.noteBookTab,height=win_height,width=win_weight,padx=10,background="#fff")
        self.multiple_file = ttk.Frame(self.noteBookTab,height=win_height,width=win_weight)


        self.noteBookTab.add(self.single_file,text="Single File",compound="left")
        self.noteBookTab.add(self.multiple_file,text="Multiple File",compound="left")
        
        self.loaded_audio = ""
        # Handle the filedialog for selecting audio file
        def select_audio():  

            self.filename1 = filedialog.askopenfilename(initialdir = "/",title="Choose Audio File",filetype=(("All Files", "*.*"),("audio",".mp3"),("audio",".wave")))
            print(f"self.filename1 :{self.filename1}")
            #? Clear all Entry widgets first before writing new metadata
            clear_meta()
            
            self.import_audio_entry.insert(0,self.filename1)
            metadata = audio_metadata.load(self.filename1)

            print(metadata)

            #******** ARTIST *******
            try:
                self.artist_entry.insert(0,metadata.tags.artist[0])
            except AttributeError as e:
                return e
            except ValueError as e:
                return e
            except KeyError as e:
                print("There is Artist key Error")
                return e
            
            
            #******** ALBUM *******
            try:
                self.album_entry.insert(0,metadata.tags.album[0])
            except AttributeError:
                pass
            except ValueError:
                pass
            except KeyError:
                print("There is a Album key Error")
            
            
            #******** TITLE *******
            try:
                title = str(metadata.tags.title[0])
                # title.replace("[","")
                # title.replace("$","")
                self.title_entry.insert(0,title)
            except AttributeError:
                pass
            except ValueError:
                pass
            except KeyError:
                print("There is a Album key Error")
            
            #******** GENERE *******
            try:
                self.genere_entry.insert(0,metadata.tags.genre[0])
            except AttributeError:
                pass
            except ValueError:
                pass
            except KeyError:
                print("There is a Album key Error")
                
           
            #******** DATE *******
            try:
                self.date_entry.set_date(metadata.tags.date[0])
            except AttributeError:
                pass
            except ValueError:
                pass
            except KeyError:
                print("There is a Date key Error")     
                
            #******** TRACK NO *******
            try:
                self.track_no_entry.insert(0,metadata.tags.tracknumber[0])
            except AttributeError:
                pass
            except ValueError:
                pass
            except KeyError:
                print("There is a Track No. key Error")   
            
            
            #******** FILE SIZE *******
            try:
                
                size = (int(metadata['filesize']) /1000)/1050
                size_formatted = "{:.2f}".format(size)
                size_str = f"{size_formatted} MB"
                print("File Size 2: ",metadata.filesize)
                self.file_size_entry.insert(0,size_str)
                # file_size_entry.configure(state=tk.DISABLED,background="#fff")
            except AttributeError:
                pass
            except ValueError:
                pass
            except KeyError:
                print("There is a file size_entry. key Error") 
                
                
            #******** DURATION *******
            try:
                self.duration_entry.insert(0,metadata.streaminfo.duration)
                # duration_entry.configure(state=tk.DISABLED,background="#fff")
            except AttributeError:
                pass
            except ValueError:
                pass
            except KeyError:
                print("There is a DURATION key Error")       
                
            #************ Copyright **************
            try:
                self.copyright_entry.insert(0,metadata.tags.copyright[0])
                # duration_entry.configure(state=tk.DISABLED,background="#fff")
            except AttributeError:
                pass
            except ValueError:
                pass
            except KeyError:
                print("There is a Copyright key Error") 
            
            #************ Protected *************
            try:
                if metadata.streaminfo.protected == 0:
                    self.protected_entry.insert(0,"False")
                else:
                    self.protected_entry.insert(0,"True")
                # duration_entry.configure(state=tk.DISABLED,background="#fff")
            except AttributeError:
                pass
            except ValueError:
                pass
            except KeyError:
                print("There is a PROTECTED key Error") 
            
            #************ Sample Rate ***********
            try:
                sample_str = f"{(metadata.streaminfo.sample_rate/1000)} KHz"
                self.sample_rate_entry.insert(0,sample_str)
                # duration_entry.configure(state=tk.DISABLED,background="#fff")
            except AttributeError:
                pass
            except ValueError:
                pass
            except KeyError:
                print("There is a SAMPLE RATE key Error") 
            
            #*********** Bite Rate *************
            try:
                bite_str = f"{(metadata.streaminfo.bitrate/1000)} Kbps"
                self.biterate_entry.insert(0,bite_str)
                # duration_entry.configure(state=tk.DISABLED,background="#fff")
            except AttributeError:
                pass
            except ValueError:
                pass
            except KeyError:
                print("There is a BIERATE key Error") 
                
            
            print("Picture :", metadata.pictures[0])
            if metadata.pictures[0] :
                mime_type = metadata.pictures[0].mime_type
                if metadata.pictures[0].height:
                    height = metadata.pictures[0].height
                if   metadata.pictures[0].width:
                    width = metadata.pictures[0].width
                if  metadata.pictures[0].data:
                    data = metadata.pictures[0].data
                    
                    picture_str = f"{height}x{width}-{mime_type}"
                    print("picture_str :",picture_str)
                    self.album_cover_entry.delete(0, 'end')
                    self.album_cover_entry.insert(0,picture_str)   
                

            
        # Handle the filedialog for selecting audio file
        def select_output_folder():  
            self.filename2 = filedialog.askdirectory(initialdir = "/",title="Select Outout Folder",mustexist=True)
            self.output_folder_entry.delete(0, 'end')
            self.output_folder_entry.insert(0,"")
            self.output_folder_entry.insert(0,self.filename2)
            
            
        # Handle the filedialog for selecting CAlbum over Image
        def select_cover_image():  
            self.filename3 = filedialog.askopenfilename(initialdir = "/",title="Select Album Cover",filetype=(("All Files", "*.*"),("PDF",".png"),("Shortcut",".jog")))
            self.album_cover_entry.delete(0, 'end')
            self.album_cover_entry.insert(0,"")
            self.album_cover_entry.insert(0,self.filename3)
            
        def read_audio_metadata(path):
            metadata = audio_metadata.load(path)
            print(metadata)
        
                #Define a function to clear the Entry Widget Content
        def clear_meta():
                self.import_audio_entry.delete(0, 'end')
                self.artist_entry.delete(0, 'end')
                self.album_entry.delete(0, 'end')
                self.title_entry.delete(0, 'end')
                self.genere_entry.delete(0, 'end')
                self.biterate_entry.delete(0, 'end')
                self.duration_entry.delete(0, 'end')
                self.track_no_entry.delete(0, 'end')
                self.copyright_entry.delete(0, 'end')
                self.sample_rate_entry.delete(0, 'end')
                self.file_size_entry.delete(0, 'end')
                self.protected_entry.delete(0, 'end')
                self.album_cover_entry.delete(0, 'end')
                
        #Define a function to clear the Entry Widget Content
        def clear_text():
                self.import_audio_entry.delete(0, 'end')
                self.artist_entry.delete(0, 'end')
                self.album_entry.delete(0, 'end')
                self.title_entry.delete(0, 'end')
                self.genere_entry.delete(0, 'end')
                self.biterate_entry.delete(0, 'end')
                self.duration_entry.delete(0, 'end')
                self.track_no_entry.delete(0, 'end')
                self.copyright_entry.delete(0, 'end')
                self.sample_rate_entry.delete(0, 'end')
                self.output_folder_entry.delete(0, 'end')
                self.file_size_entry.delete(0, 'end')
                self.protected_entry.delete(0, 'end')
                self.album_cover_entry.delete(0, 'end')

        
        def show_finish_message():
            messagebox.showinfo(title="Metadata added",message="New Metadata was added successfully",detail="These are some special details here", icon='info')
        
        
        def show_fail_message():
            messagebox.showinfo(title="Metadata added",message="Operation Failed !!!",detail="Could not write metadata to audio file", icon='error')
        
        def show_select_audio_message():
            messagebox.showinfo(title="Metadata added",message="File Error",detail="Please select an audio file to proceed !", icon='error')
        
        
        
        #? Call the write Audio metadata function here
        def startWriting():
            import_audio_entry_data = self.import_audio_entry.get()
            if import_audio_entry_data:
                pass
            else:
                show_select_audio_message()
                # clear_meta()
                # clear_text()
                
            output_folder_entry_data = self.output_folder_entry.get()
            print(f"OUTPUT FOLDER: {output_folder_entry_data}")
            artist_entry_data = self.artist_entry.get()
            album_entry_data = self.album_entry.get()
            title_entry_data = self.title_entry.get()
            genere_entry_data = self.genere_entry.get()
            date_entry_data = self.date_entry.get()
            track_no_entry_data = self.track_no_entry.get()
            file_size_entry_data = self.file_size_entry.get()
            duration_entry_data = self.duration_entry.get()
            copyright_entry_data = self.copyright_entry.get()
            protected_entry_data = self.protected_entry.get()
            sample_rate_entry_data = self.sample_rate_entry.get()
            biterate_entry_data = self.biterate_entry.get()
            album_cover_entry_data = self.album_cover_entry.get()
            
            single_audio = Metadata(music_file=import_audio_entry_data,album_art=album_cover_entry_data,artist=artist_entry_data,album=album_entry_data,date=date_entry_data, genre=genere_entry_data, title=title_entry_data, track_no=track_no_entry_data,bitrate=biterate_entry_data)
            status = single_audio.writeMeta(saving_path=output_folder_entry_data,file_format='mp3')
            if status == True:
                show_finish_message()
            else:
                show_fail_message()
        

        # For Radio Button
        def check_selected():
            choice = v.get()
            print('choice :',choice)
            if choice == True:
                self.is_compress2 = False
                return 'YES'
            elif choice == False:
                self.is_compress1 = False
                return 'NO'
        
        
        
        curr_dir = Path.cwd()
        
        #? Save audio button
        self.image1 = PhotoImage(file=f"{curr_dir}" + "./048-magic-wand.png")
        self.save_img = self.image1.subsample(29,29).zoom(1)
        
        #? Choose image button
        self.image2 = PhotoImage(file=f"{curr_dir}" + "./040-image.png")
        self.choose_image = self.image2.subsample(29,29).zoom(1)#
        
        #? Import Image button
        self.image3 = PhotoImage(file=f"{curr_dir}" + "./009-video-editing.png")
        self.choose_song = self.image3.subsample(29,29).zoom(1)#
        
        #? Output Folder button
        self.image4 = PhotoImage(file=f"{curr_dir}" + "./044-folder.png")
        self.folder_img = self.image4.subsample(29,29).zoom(1)#
        
        #? Clear All button
        self.image5 = PhotoImage(file=f"{curr_dir}" + "./012-color-circle.png")
        self.clear = self.image5.subsample(29,29).zoom(1)#
        
        

        self.import_audio_entry = ttk.Entry(self.single_file,width=110,foreground="#000")
        self.import_audio_entry.place(x=0,y=9)
        
        self.import_browse_btn = ttk.Button(self.single_file,text="Choose Audio",command=select_audio,width=16)
        self.import_browse_btn.place(x=670,y=7)
        
        # self.import_browse_btn.config(image=self.choose_song,compound='right')
    
        
        group_controls = tk.LabelFrame(self.single_file,text="Audio Metadata",font="Calibri 12", width=776,height=240,foreground="#000")
        group_controls.place(x=0,y=40)
        
        execute_controls = tk.Frame(self.single_file, width=776,height=120)
        execute_controls.place(x=0,y=290)
        
            
        current_year = datetime.today().year
        self.artist_lbl = ttk.Label(group_controls,text="Artist :")
        self.artist_entry = ttk.Entry(group_controls,width=55,foreground="#1e63ef") 
        self.album_lbl = ttk.Label(group_controls,text="Album :")
        self.album_entry = ttk.Entry(group_controls,width=53,foreground="#1e63ef")
        self.title_lbl = ttk.Label(group_controls,text="Title :")
        self.title_entry = ttk.Entry(group_controls,width=55,foreground="#1e63ef")
        self.genere_lbl = ttk.Label(group_controls,text="Genere :")
        self.genere_entry = ttk.Entry(group_controls,width=53,foreground="#1e63ef")
        self.date_lbl = ttk.Label(group_controls,text="Date :")
        self.date_entry = DateEntry(group_controls,width=30,bg="darkblue",fg="#1e63ef",year=current_year )
        self.file_size_lbl = ttk.Label(group_controls,text="Size :")
        self.file_size_entry = ttk.Entry(group_controls,width=15,foreground="#1e63ef")
        self.track_no_lbl = ttk.Label(group_controls,text="Track No. :")
        self.track_no_entry =  ttk.Spinbox(group_controls, to=100,width=18,foreground="#1e63ef")
        self.duration_lbl = ttk.Label(group_controls,text="Duration: ")
        self.duration_entry = ttk.Entry(group_controls,width=18,foreground="#1e63ef")
        self.album_cover_lbl = ttk.Label(group_controls,text="Album Cover :")
        self.album_cover_entry = ttk.Entry(group_controls,width=90,foreground="#1e63ef")
        self.album_cover_button = ttk.Button(group_controls,width=19,text="Choose Image",command=select_cover_image)
        # self.album_cover_button.configure(image=self.choose_image,compound='right')
        
        self.is_compress_lbl = ttk.Label(execute_controls,text="Compress Audio:")
        # self.is_compress = ttk.Combobox(group_controls,values=("YES","NO"),width=13,state="Hello",foreground="#1e63ef")
        v = tk.IntVar()
        v.set(0)  # initializing the choice, i.e. Python
        
        # languages = [
   	    #  ("Perl", 1),
    	#      ("Java", 2),
        #      ("C++", 3),
        #      ("C", 4)]
        
        # for language, val in languages:
        #     f"{ttk.Radiobutton},{val}"(root, 
        #             text=language, 
        #             variable=v, 
        #             command=check_selected,
        #             value=val).pack(anchor=tk.W)
        # self.is_compress1 = ttk.Radiobutton(execute_controls,text="YES",command=check_selected,variable=v)
        # self.is_compress2 = ttk.Radiobutton(execute_controls,text="NO",command=check_selected,variable=v)
        
        self.save_as_lbl = ttk.Label(execute_controls,text="Save as:")
        self.save_as = ttk.Combobox(execute_controls,values=(".WAVE",".MP3",".AVI"),width=13,foreground="#000")
        
        self.execute_info_text = ttk.Label(execute_controls,text="Save Audio Metadata : ID3v2")
        self.execute_file_type = ttk.Label(execute_controls,text="File Type : .mp3")
        self.progress_text = ttk.Label(execute_controls,text="Progress : 0%")
        self.progress_bar = ttk.Progressbar(execute_controls,length=755,orient="horizontal",maximum=100,value=0,mode="determinate",phase=3)
        
        self.output_folder_entry = ttk.Entry(execute_controls, width=57,foreground="#000")
        self.output_folder_button = ttk.Button(execute_controls,text="Output Folder",command=select_output_folder,width=16)
        
        # self.output_folder_button.config(image=self.folder_img,compound='right')
        
        self.generate_audio = ttk.Button(execute_controls,text="Save Audio",width=22,command=startWriting)
        # self.generate_audio.config(image=self.save_img,compound='right')
        
        self.clear_all = ttk.Button(execute_controls,text="Clear All",width=22,command=clear_text)
        # self.clear_all.config(image=self.clear,compound='right')
        
        self.protected_lbl = ttk.Label(group_controls,text="Protected :")
        self.protected_entry = ttk.Entry(group_controls,width=13,foreground="#1e63ef")
        self.sample_rate_lbl = ttk.Label(group_controls,text="Sample rate: ")
        self.sample_rate_entry = ttk.Entry(group_controls,width=13,foreground="#1e63ef")
        self.copyright_lbl = ttk.Label(group_controls,text="Copyright :")
        self.copyright_entry = ttk.Entry(group_controls,width=34,foreground="#1e63ef")
        self.biterate_lbl = ttk.Label(group_controls,text="Biterate :")
        self.biterate_entry = ttk.Entry(group_controls,width=13,foreground="#1e63ef")
        
        
        self.artist_lbl.place(x=5,y=10)
        self.artist_entry.place(x=46,y=10)
        
        self.album_lbl.place(x=390,y=10)
        self.album_entry.place(x=440,y=10)
        
        self.title_lbl.place(x=5, y=50)
        self.title_entry.place(x=46, y=50)
        
        self.genere_lbl.place(x=390, y=50)
        self.genere_entry.place(x=440, y=50) 
        
        self.date_lbl.place(x=5,y=90)
        self.date_entry.place(x=46,y=90)
        self.file_size_lbl.place(x=250,y=90)
        self.file_size_entry.place(x=286,y=90)
      
        self.track_no_lbl.place(x=390, y=90)
        self.track_no_entry.place(x=455, y=90) 
    
        self.duration_lbl.place(x=590, y=90)
        self.duration_entry.place(x=650, y=90)

        self.album_cover_lbl.place(x=5, y=175)
        self.album_cover_entry.place(x=89, y=175)
        self.album_cover_button.place(x=640, y=172)

        self.protected_lbl.place(x=5,y=130)
        self.protected_entry.place(x=70,y=130)
        self.sample_rate_lbl.place(x=160,y=130)
        self.sample_rate_entry.place(x=235,y=130)
        self.copyright_lbl.place(x=333,y=130)
        self.copyright_entry.place(x=405,y=130)
        self.biterate_lbl.place(x=620,y=130)
        self.biterate_entry.place(x=677,y=130)

        self.execute_info_text.place(x=10,y=14)
        self.execute_file_type.place(x=190,y=14)
        self.progress_text.place(x=300,y=14)
        self.progress_bar.place(x=10,y=45)
        
        self.is_compress_lbl.place(x=390, y=14)
        # self.is_compress1.place(x=490, y=14)
        # self.is_compress2.place(x=540, y=14)
        self.save_as_lbl.place(x=605, y=14)
        self.save_as.place(x=660, y=14)

        self.output_folder_entry.place(x=125,y=83)
        self.output_folder_button.place(x=10,y=80)
        self.generate_audio.place(x=480,y=81)
        self.clear_all.place(x=625,y=81)

        

if __name__ == '__main__':
    root = tk.Tk()
    # root = ThemedTk(theme="plastik")
    app = App(root)
    style = ttk.Style()
    
    # style.configure('TButton',side='center')

    # style.theme_use('alt')
    # style.configure('TButton', background = 'blue', foreground = 'white')
    # style.map('TButton', background=[('active','red')])
        
    app.mainloop()