
import os
# from PIL import Image, ImageSequence
# from werkzeug.utils import secure_filename
import audio_metadata
from pathlib import Path
# import audiometadata

# from pydub import AudioSegment
# Importing Mutagen for processing song album art
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, error
from mutagen.easyid3 import EasyID3

# AudioSegment.converter = r"C:\\ffmpeg\bin\\ffmpeg.exe"
# AudioSegment.ffprobe   = r"C:\\ffmpeg\bin\\ffprobe.exe"


class Metadata:
    
    def __init__(self,music_file:str,album_art:str,artist:str,album:str,date:str, genre:str, title:str, track_no:int,bitrate:str):
        self.music_file = music_file
        self.album_art = album_art
        self.artist = artist
        self.album = album
        self.date = date
        self.genre = genre
        self.title = title
        self.track_no = track_no
        self.bitrate = bitrate
    
    
    def addAlbumArt(self):  
        # Passing the audio path and album art (image) path
        audio_path = audio_path
        picture_path = art_path
        audio = MP3(self.music_file, ID3=ID3)
        # adding ID3 tag if it is not present
        try:
            audio.add_tags()
        except error:
            pass
            
        audio.tags.add(APIC(mime='image/jpeg',type=3,desc=u'Cover',data=open(self.album_art,'rb').read()))
        # edit ID3 tags to open and read the picture from the path specified and assign it
        
        try:
            audio.save()  # save the current changes
            return True
        except:
            return False
        
        
    
    # Save Music to file system
    def writeMeta(self,saving_path,file_format):
        print(f"MUSIC FILE: {self.music_file}")
        
        metadata = audio_metadata.load(self.music_file)

        # Update metadata using mutagen
        audio = EasyID3(self.music_file)

        encodedby = "Audiometa v1.0"
        file_format = "mp3"
        
        if saving_path:
            # Modify the metadata
            audio['artist'] = self.artist
            audio['album'] =  self.album
            audio['date'] = self.date
            audio['genre'] = self.genre
            audio['title'] = self.title
            # audio['track'] = self.track_no
            # audio['encodersettings'] = encodedby
            # audio['comments'] = 'Default Comment written by Audiometa v1.0'
            
            # Save changes
            audio.save()

            metadata['streaminfo'].bitrate = self.bitrate
            metadata.save()


        else:
            print("Audio File not available")
        
        if self.album:
            album_art = self.album_art #* Which is the path to cover album
            albumArt_result = self.addAlbumArt(save_path,album_art)
            
            if(albumArt_result == True):
                print('Album Art added to song successfully... :)')
            else:
                print('Failed adding Album Art... :(')
        else:
            print("Album Art not available")
            
        return True
        # except:
        #     print("Error: Fail to write metadata to audio")
        #     return False
        
