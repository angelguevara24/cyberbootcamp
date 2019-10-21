
### Instructions

  * The zip file provides you with three maze-like file directories.  Each folder maze is composed of a set of deeply nested subfolders. 
  
  
  *  At the base of each folder is a file called **start.txt**. Your task is to copy this file into the `End` folder that is buried somewhere in the maze. You may use only *one* copy command as part of each solution. 

* **Hints:**

  * Your final solutions should each take the form of something like the following `cp start.txt ./Kitchen/Cabinet/BreadBox/Loaf/End/`.

  * The first two mazes use file trees that looks like the following:

    ```
    Maze 1
    ------------------------------
    Start.txt
    Bedroom
      Closet
      Dresser
      Bonus.txt
    Bathroom
      MedicineCabinet
        Toothpaste
        Brush
      Shower
        End
        
    Maze 2
    ------------------------------
    Start.txt
    Kitchen
      Refrigerator
        Bonus.txt
      Oven
    LivingRoom
      CoffeeTable
        Remotes
          End
        Books
      MediaCenter
        MediaPlayer
          DVD
          VHS
    ```

  * For the third challenge, you may want to create a similar file tree to help you navigate.

  * Stay persistent! This is a bit of a brainteaser, but it's great practice for the real-world.

  * Remember that `cd ..` will take you back a folder in case you hit a dead end while navigating the directories.

* **Bonus:**

  * If you finish early, take on an extra challenge.

  * Buried in each of the folder mazes is a file called **Bonus.txt**. Your goal is to create a single `cd` command to navigate from the root of the maze to the point of the **Bonus.txt** file and then to create a single `cp` command to relocate the file into the `End` folder.
