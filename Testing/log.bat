@echo off
rem C:/Users/Joseph/Documents/GitHub/Traga/log.bat "%N" "%L" "%G" "%F" "%R" "%D" "%C" "%Z" "%T" "%I"
rem "C:/Users/Joseph/Documents/GitHub/Traga/log.bat" "%N" "%L" "%G" "%F" "%R" "%D" "%C" "%Z" "%T" "%I"

rem SET out = "C:/Users/Joseph/Documents/GitHub/Traga/parameters.txt"

(
	@echo %%N = %1
	@echo %%L = %2
	@echo %%G = %3
	@echo %%F = %4
	@echo %%R = %5
	@echo %%D = %6
	@echo %%C = %7
	@echo %%Z = %8
	@echo %%T = %9	
) > "C:/Users/Joseph/Documents/GitHub/Traga/parameters.txt"