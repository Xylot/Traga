# C:/Users/Joseph/AppData/Local/Programs/Python/Python37/python.exe C:/Users/Joseph/Documents/GitHub/Traga/log.py "%N" "%L" "%G" "%F" "%R" "%D" "%C" "%Z" "%T" "%I"

import os
import sys
import json
import subprocess
from pathlib import Path


LOG = True
TESTING = False

HOME_DIRECTORY = os.path.dirname(os.path.realpath(__file__)) + '/'
MEDIA_LIST_PATH = Path(HOME_DIRECTORY + 'MediaList.txt').absolute()
WINRAR_PATH = Path('C:/Program Files/WinRAR/WinRAR.exe').absolute()
DESTINATION_PATH = Path('D:/Unsorted TV Shows/').absolute()
CONFIG_LOG_PATH = Path(HOME_DIRECTORY + '/Config/').absolute()


def get_arguments() -> list:
    if TESTING:
        return get_test_arguments()
    else:
        return sys.argv


def get_test_arguments() -> list:
    return [
        "C:/Users/Joseph/Documents/GitHub/Traga/log.py",
        "Cunk.And.Other.Humans.On.2019.S01E04.HDTV.x264-LiNKLE",
        "",
        "",
        "D:/Completed Torrents/Cunk.And.Other.Humans.On.2019.S01E04.HDTV.x264-LiNKLE",
        "D:/Completed Torrents/Cunk.And.Other.Humans.On.2019.S01E04.HDTV.x264-LiNKLE",
        "D:/Completed Torrents",
        "4",
        "34570705",
        "http://tracker.alpharatio.cc:2710/dee7c09413e0f3a580847dfb081d766f/announce",
        "004882b094bcf0b0e69851550b448a47df741a04"
    ]


def get_torrent_config(args: list) -> dict:
    return {
        'name': args[1],
        'category': args[2],
        'tags': args[3],
        'content_path': args[4],
        'root_path': args[5],
        'save_path': args[6],
        'num_of_files': args[7],
        'size': args[8],
        'tracker': args[9],
        'hash': args[10],
        'config_out_path': str(CONFIG_LOG_PATH) + '/' +  args[10] + '_config.json'
    }


def get_winrar_arguments(torrent_config: dict) -> list:
    arguments = []
    arguments.append(str(WINRAR_PATH))
    arguments.append('x')
    arguments.append('-ibck')
    arguments.append('-inul')
    arguments.append('-o+')
    arguments.append(torrent_config['content_path'] + '\\*.r00')
    arguments.append(str(DESTINATION_PATH))
    return arguments


def get_destination_paths():
    pass


def read_file(file_path: Path) -> list:
    names = []
    with open(file_path) as file:
        for line in file:
            line = line.rstrip('\n').lower()
            names.append(line)
    return names


def is_wanted(media_list: list, torrent_name: str) -> bool:
    for media in media_list:
        if media in torrent_name.lower():
            return True
    return False


def is_extactable(torrent_config: dict) -> bool:
    for file in os.listdir(torrent_config['content_path']):
        if 'r00' in file:
            return True
    return False


def is_valid(torrent_config: dict) -> bool:
    media_list = read_file(MEDIA_LIST_PATH)

    return is_wanted(media_list, torrent_config['name']) and is_extactable(torrent_config)


def log_torrent_config(torrent_config: dict):
    if LOG:
        with open(torrent_config['config_out_path'], 'w') as file:
            json.dump(torrent_config, file)


def extract_torrent(torrent_config: dict):
    if is_valid(torrent_config):
        log_torrent_config(torrent_config)
        subprocess.call(get_winrar_arguments(torrent_config))


if __name__ == "__main__":
    arguments = get_arguments()
    torrent_config = get_torrent_config(arguments)
    extract_torrent(torrent_config)
