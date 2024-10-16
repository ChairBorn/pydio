from pydub import AudioSegment

def load_audio(file_path):
    """Load audio file using PyDub."""
    return AudioSegment.from_file(file_path)

def save_audio(audio_segment, file_path, format="mp3"):
    """Save processed audio to a file."""
    audio_segment.export(file_path, format=format)
