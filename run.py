import whisper
import gemini_summarize

model = whisper.load_model("base")

audio_file = input("")

audio = whisper.load_audio(audio_file)
audio = whisper.pad_or_trim(audio)

mel = whisper.log_mel_spectrogram(audio).to(model.device)

_, probs = model.detect_language(mel)
print(f"Detected language: {max(probs, key=probs.get)}")

result = model.transcribe(audio_file)

transcription = result["text"]

print(gemini_summarize.get_summary((transcription)))