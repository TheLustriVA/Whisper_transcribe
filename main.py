import argparse
from src.languages import display_languages as dl
from src.transcribe import translate_file 
from src.transcribe import detect_language 
from src.transcribe import simple_transcribe
from src.transcribe import esl_transcribe  

parser = argparse.ArgumentParser(description="Processes and transcribes audio using OpenAI's Whisper model.")

parser.add_argument("-i", "--input_file", help="Input file to use. Must be a .wav file. Defaults to .wav contents of the inputs/ directory of the base install path.", required=False, default="inputs/*.wav")
parser.add_argument("-m", "--model", help="The size of the Whisper model to use. Defaults to 'base'.", required=False, default="base")
parser.add_argument("-l", "--language", help="Set the source language. If flag set but no language given, Whisper will attempt to detect the source language.", required=False, default="True")
parser.add_argument("-t", "--translate", help="If --language is set, the audio will be translated into English. If -t is set but -l is not set, Whisper will attempt to detect the source language.", required=False, action="store_true")
parser.add_argument("-d", "--disp_lang", help="Display the list of languages available for translation with Whisper.", required=False, action="store_true")

args = parser.parse_args()

if args.input_file:
    input_file = args.input_file
if args.model:
    model = args.model
if args.language:
    language = args.language
if args.translate:
    translate = args.translate
if args.disp_lang:
    dl()
if args.disp_lang == True and (language or translate or model or input_file) is not None:
    print("The -d | --disp_lang flag cannot be used with any other flags.")
    exit
    
def main(input_file: str, model: str, language, translate: bool)->str:

    if language in dl() and translate is True:  # If translate is True and the language was given, translate the transcription into English.
        outfile = translate_file(input_file, model, language) # Translate into English and transcribe.
    elif language in dl() and (translate is False or translate is None): # If q proper language was given but translation not flagged.
        outfile = esl_transcribe(input_file, model, language) # Translate the audio but do not translate.
    elif (language not in dl() or language is None) and translate is True: # If a proper language was not given but translation is flagged, detect the language and translate.
        outfile = detect_language(input_file, model, language) # Translate the file from the given language into English and transcribe.
    else:
        outfile = simple_transcribe(input_file, model) # Transcribe the file without translation.

            
            