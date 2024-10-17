import argparse
from melodycoach.analyzer import AudioAnalyzer
from melodycoach.feedback import FeedbackGenerator
from melodycoach.utils import load_audio

def analyze_audio(args):
    """Analyze audio file for tempo and pitch"""
    analyzer = AudioAnalyzer(args.file)
    
    if args.tempo:
        tempo, beats = analyzer.detect_tempo()
        print(f"Detected Tempo: {tempo:.2f} BPM")
        print(f"Beats: {beats}")
    
    if args.pitch:
        pitches = analyzer.detect_pitch()
        print("Detected Pitches (Hz):", pitches)

def provide_feedback(args):
    """Provide feedback based on expected tempo or pitch"""
    analyzer = AudioAnalyzer(args.file)
    feedback_gen = FeedbackGenerator(analyzer)
    
    if args.expected_tempo:
        tempo_feedback = feedback_gen.compare_tempo(expected_tempo=args.expected_tempo)
        print(tempo_feedback)
    
    if args.expected_pitches:
        expected_pitches = [float(p) for p in args.expected_pitches.split(',')]
        pitch_feedback = feedback_gen.compare_pitch(expected_pitches=expected_pitches)
        print(pitch_feedback)

def main():
    parser = argparse.ArgumentParser(description="MelodyCoach: Audio Analysis and Feedback CLI")
    
    subparsers = parser.add_subparsers(help="Commands", dest="command")
    
    # Subcommand for analysis
    analyze_parser = subparsers.add_parser('analyze', help="Analyze an audio file")
    analyze_parser.add_argument('file', type=str, help="Path to the audio file")
    analyze_parser.add_argument('--tempo', action='store_true', help="Detect tempo of the audio")
    analyze_parser.add_argument('--pitch', action='store_true', help="Detect pitch of the audio")
    analyze_parser.set_defaults(func=analyze_audio)
    
    # Subcommand for feedback
    feedback_parser = subparsers.add_parser('feedback', help="Provide feedback on an audio file")
    feedback_parser.add_argument('file', type=str, help="Path to the audio file")
    feedback_parser.add_argument('--expected-tempo', type=float, help="Expected tempo (in BPM)")
    feedback_parser.add_argument('--expected-pitches', type=str, help="Expected pitches (comma-separated frequencies in Hz)")
    feedback_parser.set_defaults(func=provide_feedback)
    
    args = parser.parse_args()
    
    # Execute the appropriate function based on the subcommand
    if args.command is not None:
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
