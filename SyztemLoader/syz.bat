@echo off
title Syztem is loading data.
goto startup

:config
cls
call python config.py
goto restart

:fail
cls
echo Something went wrong when loading Syztem data.
echo.
echo Error description:
echo %error%
echo.
echo Press Shift+Q to restart.
choice /n /c 0Q /cs /d 0 /t 9999

:restart
timeout 2 >> nul
cls
title Syztem is loading data.

:startup
echo Checking files...
if not exist load.txt (
	set error=File not found: load.txt
	goto fail
)
if not exist syztem.py (
	set error=File not found: syztem.py
	goto fail
)
if not exist exec.py (
	set error=File not found: exec.py
	goto fail
)
echo Setting environmental variables...
setx WorkingPath %cd%
set /p a=<%cd%\A\info.txt
set /p b=<%cd%\B\info.txt
set /p c=<%cd%\C\info.txt
setx SyztemDataA "%a%"
setx SyztemDataB "%b%"
setx SyztemDataC "%c%"
set config=0
echo Configuring startup...
echo -Press Shift+W to configure load.txt-
choice /n /c 0WQ /cs /d 0 /t 2
if errorlevel 2 set config=1
if errorlevel 3 goto restart
if %config%==1 goto config
python exec.py


set /p makePause =< %userprofile%\Documents\Syztem\settings\makePause.txt
if %makePause%==false goto end
echo.
echo eof

pause >> nul
:end
exit