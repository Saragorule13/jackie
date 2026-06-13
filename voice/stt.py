from faster_whisper import WhisperModel
import sounddevice as sd
from scipy.io.wavfile import write

MODEL_SIZE = "base"

# Lazy-loaded — only created on first transcription call
_model = None


def _get_model():
    """Load the Whisper model on first use, not on import."""
    global _model
    if _model is None:
        _model = WhisperModel(MODEL_SIZE, device="cpu", compute_type="int8")
    return _model


def record_audio(filename="input.wav", duration=5, sample_rate=16000):
    print("Listening...")
    recording = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="int16",
    )
    sd.wait()
    write(filename, sample_rate, recording)
    return filename


def transcribe_audio(audio_path):
    model = _get_model()
    segments, _info = model.transcribe(audio_path)
    return "".join(seg.text for seg in segments).strip()
