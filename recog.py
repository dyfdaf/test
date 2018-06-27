from aip import AipSpeech
import wave
from pyaudio import PyAudio,paInt16
APP_ID = '11136502'
API_KEY = 'dPeG4ubYHR0mhwjANj5xcn1YZjahStUF'
SECRET_KEY = 'BpFVkeP4PMkf2XVHnoaP8yNIe2kujrP7'

client = AipSpeech(APP_ID,API_KEY,SECRET_KEY)

def get_file(filepath):
    with open(filepath, 'rb') as fp:
        return fp.read()

framerate=8000
NUM_SAMPLES=2000
channels=1
sampwidth=2
TIME=1
def save_wave_file(filename,data):
    '''save the date to the wavfile'''
    wf=wave.open(filename,'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(sampwidth)
    wf.setframerate(framerate)
    wf.writeframes(b"".join(data))
    wf.close()

def my_record():
    pa=PyAudio()
    stream=pa.open(format = paInt16,channels=1,
                   rate=framerate,input=True,
                   frames_per_buffer=NUM_SAMPLES)
    my_buf=[]
    count=0
    while count<TIME*20:#控制录音时间
        string_audio_data = stream.read(NUM_SAMPLES)
        my_buf.append(string_audio_data)
        count+=1
        print('.')
    save_wave_file('01.pcm',my_buf)
    stream.close()

chunk=2014
def play():
    wf=wave.open(r"01.wav",'rb')
    p=PyAudio()
    stream=p.open(format=p.get_format_from_width(wf.getsampwidth()),channels=
    wf.getnchannels(),rate=wf.getframerate(),output=True)
    while True:
        data=wf.readframes(chunk)
        if data=="":break
        stream.write(data)
    stream.close()
    p.terminate()

if __name__ == '__main__':
    my_record()
    print('Over!')
 #   play()
    print(client.asr(get_file('01.pcm'), 'pcm', 16000, {'dev_pid': 1536 }))



#print(client.asr(get_file('/home/dyfdaf/baiduAI/sample/asrDemo2/pcm/0.pcm'),'pcm',16000,{'dev_pid':1536,}))
#print(client.asr(get_file('/home/dyfdaf/zn.wav'),'wav',16000,{'dev_pid':1536,}))
