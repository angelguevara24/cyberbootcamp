# Import the zipfile module into the application
import zipfile

# create another reference, this time to a locked ZIP file
lockedZip = zipfile.ZipFile("MusicSheets.zip")

# Variable used to store the password string
password = "ComicSans"

# Run the `.extractall()` function with a password
lockedZip.extractall(pwd=password.encode())