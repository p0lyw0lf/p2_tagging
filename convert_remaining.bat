for %%f in (*.mp3) do (
  ffmpeg -y -i "%%f" -vn -c:a alac -q:a 100 -b:a 320000 -map_metadata 0 "%%~nf".m4a
)
for %%f in (*.wav) do (
  ffmpeg -y -i "%%f" -vn -c:a alac -q:a 100 -map_metadata 0 "%%~nf".m4a
)