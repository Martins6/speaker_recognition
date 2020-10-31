from scipy.io import wavfile
import winsound

filename = 'microphone-results.wav'
winsound.PlaySound(filename, winsound.SND_FILENAME)

filename1 = 'clean_microphone.wav'
winsound.PlaySound(filename1, winsound.SND_FILENAME)