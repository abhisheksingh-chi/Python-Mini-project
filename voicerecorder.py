import sounddevice as sd
import wavio as wv
# Sampling frequency in Hz
freq = 44100
# Recording duration in seconds
print("Enter the Duration of Voice recorder in Seconds")
dur_seconds = int(input())
# Start recorder with the given values
recording = sd.rec(int(dur_seconds*freq),samplerate=freq,channels=1 )

sd.wait()

# Converting Numpy array into .wav file with 16 bits per sample
wv.write("recording1.wav", recording, freq,sampwidth=2)

