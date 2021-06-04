for %%f in (*.mp3) do (
  ffmpeg -y -i "%%f" -c:a alac -q:a 100 -b:a 320000 -c:v copy -map_metadata 0 "%%~nf".m4a
)
for %%f in (*.wav) do (
  ffmpeg -y -i "%%f" -c:a alac -q:a 100 -b:a 320000 -c:v copy -map_metadata 0 "%%~nf".m4a
)
