import os
import sys
import json
import logging
import subprocess
from pathlib import Path

VERBOSE = False

HOME_DIRECTORY = os.path.dirname(os.path.realpath(__file__)) + '/'
MEDIA_LIST_PATH = Path(HOME_DIRECTORY + 'MediaList.txt').absolute()
WINRAR_PATH = Path('C:/Program Files/WinRAR/WinRAR.exe').absolute()
DESTINATION_PATH = Path('H:/Unsorted TV Shows/').absolute()
LOG_PATH = Path(HOME_DIRECTORY + '/Logs/log.log').absolute()

def create_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('[%(asctime)s] %(name)s: %(message)s')
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    stream_handler.setLevel(logging.WARNING)
    file_handler = logging.FileHandler(LOG_PATH)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)
    return logger

logger = create_logger()

def get_media_list(file_path: str) -> list:
    with open(file_path, 'r') as file:
        threads = file.readlines()
    return [thread.strip() for thread in threads]

class Torrent:
    
    def __init__(self, config: list, media_list: list):
        self.media_list = media_list
        self.name = config[1]
        self.category = config[2]
        self.tags = config[3]
        self.content_path = config[4]
        self.root_path = config[5]
        self.save_path = config[6]
        self.num_of_files = config[7]
        self.size = config[8]
        self.tracker = config[9]
        self.hash = config[10]
        self.extractable_file_path = self.content_path + '\\*.rar'

    def _wanted(self) -> bool:
        logger.debug('Checking if {} is wanted...'.format(self.name))
        for media in self.media_list:
            if media in self.name.lower():
                return True
        logger.warning('Torrent {} is not wanted!'.format(self.name))
        return False

    def _extractable(self) -> bool:
        logger.debug('Checking if {} is extractable...'.format(self.name))
        for file in os.listdir(self.content_path):
            if 'r00' in file:
                return True
        logger.warning('Torrent {} is not extractable!'.format(self.name))
        return False

    def valid(self) -> bool:
        logger.info('Checking if torrent {} is valid...'.format(self.name))
        return self._wanted() and self._extractable()


class Extractor:

    def _get_extract_args(self, torrent: Torrent):
        logger.debug('Getting WinRaR extraction arguments...')
        return [str(WINRAR_PATH), 'x', '-ibck', '-o+', torrent.extractable_file_path, str(DESTINATION_PATH)]

    def extract(self, torrent: Torrent):
        logger.info('Extracting {}...'.format(torrent.name))

        extract_args = self._get_extract_args(torrent)

        if VERBOSE:
            result = subprocess.run(extract_args, universal_newlines=True, encoding='utf-8', errors='replace')
        else:
            result = subprocess.run(extract_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, encoding='utf-8', errors='replace')

        if result.returncode != 0:
            logger.critical('{} failed to extract! Exiting...'.format(torrent.name))
            sys.exit(0)

        logger.info('Extracted torrent {} successfully! Media is located at: {}'.format(torrent.name, DESTINATION_PATH))


def main():
    media_list = get_media_list(MEDIA_LIST_PATH)
    torrent = Torrent(sys.argv, media_list)

    if torrent.valid():
        Extractor().extract(torrent)

main()