import glob, os

import csv

import moviepy.editor as mp

import speech_recognition as sr

import pandas as pd

 


 


 

def lolol(file):

 

    clip=mp.VideoFileClip(file)

 

    

 

     #Extracting audio from the video

    (clip.subclip(0,min(60,clip.duration))).audio.write_audiofile("chunk1.wav") 

    if 59 < clip.duration:

        (clip.subclip(59,min(119,clip.duration))).audio.write_audiofile("chunk2.wav") 

    if 118 < clip.duration:

        (clip.subclip(118, min(178,clip.duration))).audio.write_audiofile("chunk3.wav") 

 


 

    print("\nGrabbing text from the audio")

 

    for aud in glob.glob("*.wav"):

        AUDIO_FILE = aud

 

        r = sr.Recognizer()

 

        with sr.AudioFile(AUDIO_FILE) as source:

            audio = r.record(source)  # read the entire audio file

    

        fh=open(file[:-4]+".txt", "a") 

        rll = r.recognize_google(audio)

        fh.write(rll + "lolololololol\n")

        os.remove(aud)

    

    fh.close()

    print("\nText grab is complete")

    

 

    return

 


 


 

os.chdir(r"C:\Users\rameez.mulla\Desktop\faceemo\Video")


def top_of_csv():
    with open('to_read.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
            return row


#file = top_of_csv()

df = pd.read_csv('to_read.csv', index_col=0)
file = df.values.tolist()

print("\n" + str(file[0]) + " is being processed")
lolol(str(file[0]));

    

print("\nAll videos are processed.")

