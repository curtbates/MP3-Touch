@echo off
for %%F in (*.mp3) do (
	echo %%F
	copy /b "%%F" +,,
	timeout 60
)
