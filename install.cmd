@echo off
del cube_helper_build.log
del updater_build.log
echo Building Main Program
pyinstaller scrambler.py --onefile --name "CubeHelper" --add-data ".env;.env"  2>> cube_helper_build.log
echo Building Updater
pyinstaller updater.py --onefile --name "Updater" --add-data ".env;.env" 2>> updater_build.log
if %1.==. GOTO End
echo Moving Main program
copy dist\CubeHelper.exe C:\\Users\jonat\OneDrive\Desktop\CubeHelper\CubeHelper.exe
echo Starting program
start cmd.exe /C "cd c:\\Users\jonat\OneDrive\Desktop\CubeHelper && CubeHelper.exe"
:End