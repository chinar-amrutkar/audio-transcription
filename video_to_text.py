import glob, os
import moviepy.editor as mp
import speech_recognition as sr





def lolol(file):
    import moviepy.editor as mp
    clip=mp.VideoFileClip(file)

    (clip.subclip(0,min(60,clip.duration))).audio.write_audiofile("chunk1.wav")

    if 59 < clip.duration:

        (clip.subclip(59,min(119,clip.duration))).audio.write_audiofile("chunk2.wav")

    if 118 < clip.duration:

        (clip.subclip(118, min(178,clip.duration))).audio.write_audiofile("chunk3.wav")





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



os.chdir(r"C:\Users\Shrutika.Parab\Documents\Visual Studio 2015\Projects\candidate\candidate\candidate videos")
for file in glob.glob("*.mp4"):
    print(file)
    lolol(file);
