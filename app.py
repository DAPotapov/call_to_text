#!.venv/bin/python

import logging
import speech_recognition as sr

# Configure logging
logging.basicConfig(filename=".data/log.log",
                    filemode='a',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    recognizer = sr.Recognizer()
    # with sr.Microphone() as source:
    #     print("Say something:")
    #     audio = recognizer.listen(source)

    # TODO open audio file and use it as source for recognizer

    # Recognize speech using Google Speech Recognition
    words = recognizer.recognize_google(audio)

    print(words)


if __name__ == '__main__':
    main()
