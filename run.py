import whisper
import gemini_summarize

modelo = input("""Escolha entre pacotes!
tamanho|	Parametros|	Apenas em ingles   |Quantia de  VRAM|Velocidade
tiny   |	39 M      |	tiny.en	tiny       |~1 GB           |~10x
base   |	74 M      |	base.en	base       |~1 GB           |~7x
small  |	244 M     |	small.en           |~2 GB	        |~4x
medium |	769 M     |	medium.en          |~5 GB	        |~2x
large  |	1550 M    |	N/A	large          |~10 GB          |1x
turbo  |	809 M     |	N/A	turbo          |~6 GB           |~8x \n""")

model = whisper.load_model(modelo)

audio_file = input("")

audio = whisper.load_audio(audio_file)
audio = whisper.pad_or_trim(audio)

mel = whisper.log_mel_spectrogram(audio).to(model.device)

_, probs = model.detect_language(mel)
print(f"Detected language: {max(probs, key=probs.get)}")

result = model.transcribe(audio_file)

transcription = result["text"]

print(gemini_summarize.get_summary((transcription)))