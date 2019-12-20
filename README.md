# Traga

Traga is a script aimed to facilitate media library automation. The script is run when a torrent download completes and, given it is in a multi-part extractable archive, extracts to a folder of the user's choosing.

## Requirements

- Python 3.6+
- WinRAR

## Usage

To setup, input the extraction path and WinRAR path in the python script. Once complete, head over to your preferred torrent application and navigate to the "run external program after download completion" section. For example, in qBittorrent, it is located in Options -> Downloads -> Bottom of page. Next, simply input the batch script and pass the torrent name and torrent path parameters.

In qBittorrent, this is done by:

    %PATH_TO_PYTHON% %PATH_TO_SCRIPT% "%N" "%L" "%G" "%F" "%R" "%D" "%C" "%Z" "%T" "%I"

For example, my function call looks like:

    C:/Users/Joseph/AppData/Local/Programs/Python/Python37/python.exe C:/Users/Joseph/Documents/GitHub/Traga/TorrentManager.py "%N" "%L" "%G" "%F" "%R" "%D" "%C" "%Z" "%T" "%I"

NOTE: Parameter names will vary from client to client, so be sure to pass the correct ones

This script will only extract multi-part rar files meaning any media that is has the following structure:

    *.r00
    *.r01
    *.r02
    ...

Finally, you'll need to specifiy a couple of file paths for basic configuration in the body of TorrentManager.py:
	
	WinRar Path -> WINRAR_PATH = Path(%YOUR PATH HERE%).absolute()
	Destination Path -> DESTINATION_PATH = Path(%YOUR PATH HERE%).absolute()


## Documentation

### WinRAR Command Line Parameters

| Parameter |            Function           |
|:---------:|:-----------------------------:|
|     x     | Extract files with full paths |
|   -IBCK   |  Run WinRAR in the background |
|   -INUL   |     Disable Error Messages    |
|    -o+    |    Overwrite Existing File    |