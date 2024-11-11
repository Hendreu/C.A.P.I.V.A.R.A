import pyautogui
import whisper
import gemini_summarize
from pytubefix import YouTube
from pytubefix.cli import on_progress
from os import remove
import cv2
import pytesseract

def porPrint():
    pyautogui.screenshot("print.jpg")

    read = cv2.imread("print.jpg")

    convertImgToString = pytesseract.image_to_string(read)

    transcription = convertImgToString

    print(gemini_summarize.get_summary((transcription)))

    remove("print.jpg")

def ytVid():
    modelo = input("""Escolha entre pacotes!
    modelo |Parametros    |	Apenas em ingles   |Quantia de  VRAM|Velocidade
    tiny   |	39 M      |	tiny.en	tiny       |~1 GB           |~10x
    base   |	74 M      |	base.en	base       |~1 GB           |~7x
    small  |	244 M     |	small.en           |~2 GB	        |~4x
    medium |	769 M     |	medium.en          |~5 GB	        |~2x
    large  |	1550 M    |	N/A	large          |~10 GB          |1x
    turbo  |	809 M     |	N/A	turbo          |~6 GB           |~8x \n""")

    model = whisper.load_model(modelo)

    url = input("Escreva o link do video do youtube a ser resumido \n")

    yt = YouTube(url, on_progress_callback=on_progress)
    print(yt.title)

    yt = YouTube(url, on_progress_callback=on_progress)
    ys = yt.streams.get_audio_only()
    ys.download(mp3=True)

    audio_file = yt.title + ".mp3"

    audio = whisper.load_audio(audio_file)
    audio = whisper.pad_or_trim(audio)

    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    _, probs = model.detect_language(mel)
    print(f"Detected language: {max(probs, key=probs.get)}")

    result = model.transcribe(audio_file)

    transcription = result["text"]

    print(gemini_summarize.get_summary((transcription)))

    remove(yt.title + ".mp3")

def aquivoDeAudio():
    modelo = input("""Escolha entre pacotes!
    modelo |Parametros    |	Apenas em ingles   |Quantia de  VRAM|Velocidade
    tiny   |	39 M      |	tiny.en	tiny       |~1 GB           |~10x
    base   |	74 M      |	base.en	base       |~1 GB           |~7x
    small  |	244 M     |	small.en           |~2 GB	        |~4x
    medium |	769 M     |	medium.en          |~5 GB	        |~2x
    large  |	1550 M    |	N/A	large          |~10 GB          |1x
    turbo  |	809 M     |	N/A	turbo          |~6 GB           |~8x \n""")

    model = whisper.load_model(modelo)
    audio_file = input("")
    result = model.transcribe(audio_file)

    transcription = result["text"]

    print(gemini_summarize.get_summary((transcription)))

def menu():
    selOperacao = input("Selecione entre dois modulos de uso \n 1 para usar o link do youtube \n 2 para usar o arquivo de audio \n 3 por captura de tela\n")

    match selOperacao:
        case "1":
            ytVid()
        case "2":
            aquivoDeAudio()
        case "3":
            porPrint()
        case _:
            print("Opção invalida, tente novamente")
            return menu()
menu()