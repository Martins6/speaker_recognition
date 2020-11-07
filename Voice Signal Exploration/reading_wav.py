from scipy.io import wavfile
# if you're on Windows
import winsound

filename = 'Data/microphone-results.wav'
winsound.PlaySound(filename, winsound.SND_FILENAME)

filename1 = 'Data/clean_microphone.wav'
winsound.PlaySound(filename1, winsound.SND_FILENAME)