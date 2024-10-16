import unittest
from melodycoach.analyzer import AudioAnalyzer
from melodycoach.feedback import FeedbackGenerator

class TestAnalyzer(unittest.TestCase):
    def test_tempo_detection(self):
        analyzer = AudioAnalyzer("test_audio.wav")
        tempo, beats = analyzer.detect_tempo()
        self.assertGreater(tempo, 0)
        self.assertIsNotNone(beats)

    def test_pitch_detection(self):
        analyzer = AudioAnalyzer("test_audio.wav")
        pitches = analyzer.detect_pitch()
        self.assertGreater(len(pitches), 0)

class TestFeedback(unittest.TestCase):
    def test_compare_tempo(self):
        analyzer = AudioAnalyzer("test_audio.wav")
        feedback = FeedbackGenerator(analyzer)
        result = feedback.compare_tempo(120)
        self.assertIn("Great job", result)

if __name__ == '__main__':
    unittest.main()
