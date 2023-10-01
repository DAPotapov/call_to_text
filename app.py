#!.venv/bin/python

import logging
import os
import speech_recognition as sr
import subprocess as sp
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
        sys.exit("Usage: python app.py <audio file to process>")

    input_file = sys.argv[1]
    # abs_path = os.path.abspath(sys.argv[1])
    folder = os.path.split(sys.argv[1])[0]
    filename = os.path.splitext(os.path.split(sys.argv[1])[1])[0] # only file name w\o extenstion
    extension = os.path.splitext(sys.argv[1])[1]

    # Check which filetype user gave to the script, try to convert if not 'wav', overwrite existing
    if extension != '.wav':
        # TODO make this conversion can be used on other OS (use python modules for this)
        wav_filename = os.path.join(folder, filename + ".wav")
        try:
            sp.run(f"ffmpeg -y -i {sys.argv[1]} {wav_filename}", shell=True)
        except sp.CalledProcessError as e:
            logger.error(f"Couldn't convert '{sys.argv[1]}' to wav with this error: {e}")
            sys.exit(f"Couldn't convert '{sys.argv[1]}' to wav. Be sure you provided audio file.")
    else:
        wav_filename = sys.argv[1]

    # TODO get mp3, decode to wav, give this wav to sr to recognize
    
    recognizer = sr.Recognizer()

    # open audio file and use it as source for recognizer
    with sr.AudioFile(wav_filename) as source:
        audio = recognizer.record(source=source, duration=20)

    # Recognize speech using Google Speech Recognition
    try:
        words = recognizer.recognize_google(audio, language='ru-RU')
    except sr.UnknownValueError as e:
        print(e)
        logger.error(f"Couldn't recognize {input_file} at all (Error: {e})")
    except sr.RequestError as e:
        print(e)
        logger.error(f"Check interner connection (or API-KEY failed) (Error: {e})")
    else:
        print(words)

        # TODO save to <input filename>.txt


if __name__ == '__main__':
    main()
