#!.venv/bin/python

import logging
import os
import speech_recognition as sr
import sys


# Configure logging
logging.basicConfig(filename=".data/log.log",
                    filemode='a',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    # Check for command-line usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python app.py <file to process>")

    input_file = sys.argv[1]
    folder = os.path.dirname(sys.argv[1])
    filename = os.path.split(sys.argv[1])[1]
    extension = os.path.splitext(filename)[1]
    wav_filename = input_file

    # TODO get mp3, decode to wav, give this wav to sr to recognize
    
    recognizer = sr.Recognizer()

    # open audio file and use it as source for recognizer
    with sr.AudioFile(wav_filename) as source:
        audio = recognizer.record(source=source, duration=20)

    # Recognize speech using Google Speech Recognition
    try:
        words = recognizer.recognize_google(audio)
    except Exception as e:
        print(e)
        logger.error(f"Input file: {input_file} cause this error: {e}")
    else:
        print(words)

        # TODO save to <input filename>.txt

        
if __name__ == '__main__':
    main()
