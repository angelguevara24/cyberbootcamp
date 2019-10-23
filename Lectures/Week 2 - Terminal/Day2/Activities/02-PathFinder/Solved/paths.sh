# Enter the Mazes directory
cd Mazes

# Find all the Start Files 
find . -type f -name start.txt

# Find all the Bonus Files
find . -type f -name Bonus.txt

# Find all the End Folders
find . -type d -name End

# Move all the Start files to End folders
cp Maze_1/start.txt Maze_1/Right/Right/End
cp Maze_2/start.txt Maze_2/Right/Left/Left/End
cp Maze_3/start.txt Maze_3/Right/Left/Left/Left/Right/End

# Find and move all the Bonus files to End folders
cp Maze_1/Left/Bonus.txt Maze_1/Right/Right/End
cp Maze_2/Left/Left/Bonus.txt Maze_2/Right/Left/Left/End
cp Maze_3/Left/Left/Right/Bonus.txt Maze_3/Right/Left/Left/Left/Right/End