# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
import numpy as np
import pandas as pd
from plotnine import *
from scipy.io import wavfile

samplerate, data = wavfile.read('Data/microphone-results.wav')

n = np.arange(len(data))

df = pd.DataFrame({
    'data': data,
    'n':n
})

def add_fft(df, target_col, samplerate):
    """ Add all the 'fft package' to a dataframe.

    Returns: pandas.DataFrame
    """
    N = len(df.n)
    
    res = pd.DataFrame()
    # Fast Fourier Transform
    res['fft'] = np.fft.fft(df[target_col], N)
    # Power Spectrum Density
    res['PSD'] = res.fft * np.conj(res.fft) / N
    res = res.astype({"PSD": float})
    # Frequency Axis
    res['freq'] = (samplerate/N) * df.n

    return(res)


df_fft = add_fft(df, 'data', samplerate)

def human_voice_only(df):
    df = df.query('freq < 250 & freq >= 85')
    return(df)

df_fft = human_voice_only(df_fft)


