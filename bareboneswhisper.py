import os
import glob
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY") # .env file and load openai api key

# supported extensions
extensions_to_list = ["flac", "mp3", "mp4", "mpeg", "mpga", "m4a", "ogg", "webm", "wav"]

def list_files_with_extensions(extensions):
    print("LIST OF FILES:\n")
    for extension in extensions:
        pattern = "*." + extension
        files = glob.glob(pattern)
        for file in files:
            print(file)

def doTranscribe():
    list_files_with_extensions(extensions_to_list)

    filename = input("\nEnter the file name you want to transcribe: ")

    audio_file = open(filename, "rb")

    transcript = openai.Audio.transcribe(
        file = audio_file,
        model = "whisper-1",
        response_format = "srt" # supported options: json, text, srt, verbose_json, or vtt
    )

    output_filename = filename + "-TRANSCRIBED-SUBTITLES.vtt"
    with open(output_filename, "w", encoding="utf-8") as outputFile:
        outputFile.write(transcript)

    print("Here is the contents of " + filename + "-TRANSCRIBED-SUBTITLES.vtt:")
    with open(output_filename, "r", encoding="utf-8") as readFile:
        print(readFile.read())

def doTranslate():
    list_files_with_extensions(extensions_to_list)

    filename = input("\nEnter the file name you want to transcribe and translate: ")

    audio_file = open(filename, "rb")

    transcript = openai.Audio.translate(
        file = audio_file,
        model = "whisper-1",
        response_format = "srt" # supported options: json, text, srt, verbose_json, or vtt
    )

    output_filename = filename + "-TRANSLATED-SUBTITLES.vtt"
    with open(output_filename, "w", encoding="utf-8") as outputFile:
        outputFile.write(transcript)

    print("Here is the contents of " + filename + "-TRANSLATED-SUBTITLES.vtt:")
    with open(output_filename, "r", encoding="utf-8") as readFile:
        print(readFile.read())

choice = input("Choose (1) for transcription or (2) for translation: ")

if choice == "1":
    doTranscribe()
elif choice == "2":
    doTranslate()
else:
    print("Invalid input")
