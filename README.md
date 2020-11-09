# Voice Recognition

Project to recognize voices with Neural Networks with Python. The main purpose of this project is to explore the capabilities of Neural Networks and the extraction of features from signals in order to recognize different voices. This project was born out of the idea to build the hability of an virtual assistant to recognize solely your own voice. This idea came to me when contributing to the [Jarvis](https://github.com/sukeesh/Jarvis) open-source project, which is an virtual assistant for desktop.

## Data preparation

The dataset that this project uses comes soley from the [LibriSpeech](http://www.openslr.org/12/). The files are very well organized. I've build two Juypter Notebooks to process the dataset first as a set of files with each speaker id (_LibriSpeech_Files_Pre_Processing.ipynb_), and then to extract features from their voices (_Signal_Feature_Extraction.ipynb_). You can define hyperparameters in order to prepare more data automatically. In the most recent run, I've used 100 different speakers with 30 seconds of audio recordings from each, approximately.

## Neural Network Model

I've choosen to model the features extracted from the signal through dense layer Neural networks (a.k.a Deep Learning) so far I was able to achieve a 72% accuracy. I'm trying to avoid feeding a whole lot of data and exploring how to achieve more with less. 

## Future Works and Contribution

I hope to explore more the Fourier Transformation and Wavelets for the feature extraction from signals. Also, explore more different types of Neural Networks to better achieve results.

## Acknowledgment

Jurgen Arias has documented a similar project very well. It has really helped this project of mine kickstart.
