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

if __name__ == "__main__":
    text = '''
    Good morning sir. The main updates today are as follows:
    News:.
        1;   Latest in the Middle East as US secretary of state meets with leaders in region.
        2;   Meet the kids struggling to breathe in India’s choked capital.
        3;   Buckingham Palace maid arrested after drunken brawl at work Christmas party.
        4;   Indian Gukesh Dommaraju, 18, becomes the youngest ever chess world champion after Ding Liren blunder.
        5;   Oldest human DNA reveals lost branch of the human family tree. 
        6;   The game that means everything: Army and Navy get ready to clash for the 125th time in college football’s most unique rivalry. 
        7;   South Korea’s parliament votes to impeach president.
    The weather:
        ; 33 degrees centigrade. 
        ; Air Quality Index of 157 which is "Poor".
        ; The humidity is 42% and .
        ; The windspeed is 7 km/h.

    So what can I do for you today?
    '''
    print('Playing sequential output......')
    taken_time = process_sequential(text)
    print(f'Sentence of {len(text)} characters transcribed and read. First text was processed in {taken_time} seconds\n\n\n')

    print('Streaming output.....')
    taken_time = stream_stt(text)
    print(f'Sentence of {len(text)} characters transcribed and read. First text was processed in {taken_time} seconds\n\n\n')

    print('Creating audio file to save...')
    taken_time = save_audio(text)
    print(f'Sentence of {len(text)} characters transcribed and read. File was processed and saved in {taken_time} seconds')
