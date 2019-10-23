# Part I: Simple Searcher
# ------------------------------------------------- 
# Find all files
find -type f

# Find all folders
find -type d




# Part II: Title Searcher
# ------------------------------------------------- 
# Find all files containing the letter Z
find -type f -iname *Z* 

# Find all files that contain the word "rice"
find -type f -iname *rice*




# Part III: File Type Searcher 
# ------------------------------------------------- 
# Find all Excel files
find -type f -iname *.xlsx*

# Find all Word files 
find -type f -iname *.docx*




# Part III: Combo Searcher
# ------------------------------------------------- 
# Find all text files containing the number 2
find -type f -iname '*2*' -a -iname *.txt*

# Find all word files at least 200 KB in size
find -type f -iname *docx* -size +200k




# Part IV: Challenge Searcher
# ------------------------------------------------- 

# Find all Excel files, at most 15 kb in size, and  max 3 levels of depth from the surface
find -maxdepth 3 -type f -iname *xlsx* -size -15k

# Find all files that are not writable in Gibberish_Folder/folder_3
find Gibberish_Folder/folder_3 ! -writable




# Part V: Partner Search
# ------------------------------------------------- 

# Find all files modified by your partner
find . -mmin -5 

# Find all files changed by your partner
find . -cmin -5
