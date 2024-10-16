import librosa
import numpy as np

class AudioAnalyzer:
    def __init__(self, file_path):
        # Load the audio file
        self.audio, self.sr = librosa.load(file_path)

    def detect_tempo(self):
        # Detect tempo and beats
        tempo, beats = librosa.beat.beat_track(y=self.audio, sr=self.sr)
        return tempo, beats

    def detect_pitch(self):
        # Calculate pitch (fundamental frequency) using the autocorrelation method
        pitches, magnitudes = librosa.core.piptrack(y=self.audio, sr=self.sr)
        pitch_values = []
        for t in range(pitches.shape[1]):
            index = magnitudes[:, t].argmax()
            pitch = pitches[index, t]
            if pitch > 0:
                pitch_values.append(pitch)
        return pitch_values

    def get_spectrogram(self):
        # Return a mel spectrogram (useful for visualization or further analysis)
        S = librosa.feature.melspectrogram(y=self.audio, sr=self.sr)
        return S
