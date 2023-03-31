"""
translation with ai
"""
import whisper

def main_translator(path):
    print("Start converter")
    model = whisper.load_model("small")
    options = {"language": "de", "task": "translate"}
    res = model.transcribe(path, **options)
    return res["text"]

if __name__ == "__main__":
    main_translator("audio_files/test1.mp3")

