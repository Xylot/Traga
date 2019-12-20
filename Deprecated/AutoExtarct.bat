timeout /t 10 /nobreak
set "arg1=%~1"
echo "%arg1%"
set "arg2=%2"
shift
shift
"C:\Program Files\WinRAR\WinRAR.exe" x "%arg1%" "%arg2%"