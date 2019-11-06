# Navigate into the Docs folder
cd Docs

# Create MP3 and FLAC folders
mkdir Music/MP3 Music/FLAC

# Find and copy all MP3 files
find . -type f -iname '*.mp3' -exec cp {} Music/MP3 \;

# Find and copy all FLAC files
find . -type f -iname '*.flac' -exec cp {} Music/FLAC \;

# Count all MP3 files (561)
find Music/MP3 -type f | wc -l

# Count all FLAC files (225)
find Music/FLAC -type f | wc -l
