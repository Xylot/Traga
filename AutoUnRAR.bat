@ECHO off
timeout /t 10 /nobreak
set arg1=%1
set arg2=%2
shift
shift
python "C:\Program Files\WinRAR\AUR.py" "%arg1%" "%arg2%"