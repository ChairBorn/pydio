import numpy as np

class FeedbackGenerator:
    def __init__(self, analyzer):
        self.analyzer = analyzer

    def compare_tempo(self, expected_tempo):
        # Compare detected tempo with the expected one
        detected_tempo, _ = self.analyzer.detect_tempo()
        deviation = abs(detected_tempo - expected_tempo)
        if deviation < 5:
            return "Great job! Your tempo is accurate."
        else:
            return f"Your tempo deviates by {deviation} BPM. Try to stay more consistent."

    def compare_pitch(self, expected_pitches):
        # Compare detected pitch sequence with expected one
        detected_pitches = self.analyzer.detect_pitch()
        matched = np.isclose(detected_pitches, expected_pitches, atol=20)  # Allow small tolerance
        match_percentage = np.mean(matched) * 100
        if match_percentage > 90:
            return f"Excellent! You matched {match_percentage}% of the notes."
        else:
            return f"Your pitch accuracy is {match_percentage}%. Keep practicing!"
