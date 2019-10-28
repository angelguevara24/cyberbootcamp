Start with the password.lst file from `/usr/share/metasploit-framework/data/wordlists`

We'll start with **cat** which is probably the most basic text display command. This will display the entirity of a file until it gets to the end. In Linux terms, it reads files, and then writes them to standard output. 

Let's start by doing **man cat** and **cat --help**

We can take it a step further by doing something like **cat -n ** to display the line numbers of a file. 

Now, let's incorporate this with something we talked about last week, **grep**. Keeping in mind this is a list of commonly used passwords, how would we display the list passwords that are **god**: `cat -n password.lst | grep god`

Now, it is important to not confused **grep** with **find**. Find looks for things like files and directories. Grep looks for text within a file. Think of it like almost doing Ctrl+F on a keyboard when you're working in Word or some similar program. 

With these results, we found every instances of the word **god** within any part of the file, regardless if it was the word, or within the word. There's a lot. How many? Let's use **wc** to find out. 

Let's look at **grep --help** to see if there's an option we can use to only look for the whole word: `cat -n password.lst | grep -w god`

Now we're looking at the word **god** by itself, but also the line numbers associated with the location in the password file. We can use some regular expressions to limit it to just the word god: `grep "^god$" password.lst`

Now, let's introduce a new command. Say I wanted a count of how many results I just got, that's where **wc** comes in. Let's look at the man page and the help file for it. 

Update your command with `wc -l`

## Making Heads and Tails of things

Let's say we just wanted to look at the beginning of the file. Let's use **head** to show us the first 10 lines of the file.

Then, let's look at **tail** to look at the last 10 lines. 

You can update it with something like `tail -20 password.lst`

## Catting multiple files

Navigate here: https://github.com/danielmiessler/SecLists/tree/master/Passwords

Used **wget** to pull two random .txt password files, then use cat to combine them into a single file.

But what if we just want the unique values? Take this opportunity to introduce the **sort** command. And then the **uniq** command
`sort twitter-banned.txt darkweb2017-top10000.txt | uniq | wc -l`


## Using grep, nl, tail, and head. 

Let's say you want to dispaly the five lines immediatley before a line that says something like a password. Let's say we want to find the 5 passwords right before password 10,000. Let's start by finding out what password 10,000 is: `cat -n password.lst | grep 10000`

Let's start by using **tail** with the **-n+** option to specify which line to start at. 

`tail -n+1000 password.lst` will show me the end of the file starting from line 10,000, but now I want to just see that line, and the next 5 passwords. So our total command looks like this:
` tail -n+10000 password.lst | head -n 6`



