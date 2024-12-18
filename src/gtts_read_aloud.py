from gtts import gTTS
from io import BytesIO
import time
from pydub import AudioSegment
from pydub.playback import play

from queue import Queue
from threading import Thread

first_clip = False

def play_audio(q:Queue):
    global end_time, first_clip
    while not q.empty():
        mp3_fp = BytesIO()
        buff = q.get()
        mp3_fp.write(buff)
        mp3_fp.seek(0)
        song = AudioSegment.from_file(mp3_fp, format="mp3")
        if not first_clip:  
            end_time = time.time()
            first_clip = True
        play(song)

def stream_stt(text):
    q = Queue(maxsize = 20)
    thread1 = Thread(target=play_audio, args =[q])
    st_time = time.time()
    print('Started converting')
    for i, buff in enumerate(gTTS(text, lang = 'en', tld= 'co.uk').stream()):
        q.put(buff)
        if i == 0:
            # end_time = time.time()
            # print(end_time - st_time)
            thread1.start()
    thread1.join()
    return end_time - st_time
    
def process_sequential(text):
    print('Started converting')
    mp3_fp = BytesIO()
    st_time = time.time()
    ttsa = gTTS(text)
    ttsa.write_to_fp(mp3_fp)
    mp3_fp.seek(0)
    song = AudioSegment.from_file(mp3_fp, format="mp3")
    end_time = time.time()
    play(song)
    return end_time-st_time
    
def save_audio(text):
    print('Started converting')
    st_time = time.time()
    ttsa = gTTS(text)
    ttsa.save('assistant.mp3')
    end_time = time.time()
    return end_time - st_time


def play_audio(q:Queue):
    while not q.empty():
        print('Removing item for processing')
        mp3_fp = BytesIO()
        buff = q.get()
        mp3_fp.write(buff)
        mp3_fp.seek(0)
        song = AudioSegment.from_file(mp3_fp, format="mp3")
        play(song)
