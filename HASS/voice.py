import sounddevice as sd
import numpy as np

def sp(indata, outdata, frames, time, status):
    global volume
    volume = np.linalg.norm(indata)*10
    if volume >= 70:
        print("volume too high")


with sd.Stream(callback=sp):
    
    sd.sleep(1000000000)
    

