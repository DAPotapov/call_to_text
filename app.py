#!.venv/bin/python

import logging


# Configure logging
logging.basicConfig(filename=".data/log.log",
                    filemode='a',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    print("Hello, world")


if __name__ == '__main__':
    main()
