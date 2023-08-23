# barebones-whisper

A simple python script that pushes audio/video files to OpenAI's Whisper API for transcription

## Getting Started

You need python installed as well as these packages which you can get by running:

```pip install openai dotenv```

Then create a `.env` file and define your OpenAI API key. `.env.example` is provided to show the correct format.

## Running

The script will ask if you want to transcribe or translate. Transcribing will write the transcript in the original spoken language while translation will translate the transciption into English.

For convenience, the script will list all the files in the current directory with the file types that are supported by the API. The API has a 25MB limit but the script currently does not enforce this. Make sure the file you want to upload is within this limit, and compress if needed. Extracting the audio in the case of a video file can also help.

For easiest use, place your files in the same directory as the script. The script will also save the transcription into an SRT subtitle file by default (this can be opened with notepad). 

You can consult the [OpenAI Whisper API Reference](https://platform.openai.com/docs/api-reference/audio) to make modifications to the script to suit your needs.
