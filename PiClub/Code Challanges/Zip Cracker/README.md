# Zip File Cracker

### Subject Links

* [Python zipfile Module](https://docs.python.org/3/library/zipfile.html)
* [Python Try Except](https://www.w3schools.com/python/python_try_except.asp)
* [Python For Loops](https://www.w3schools.com/python/python_for_loops.asp)
* [Python Read Files](https://www.w3schools.com/python/python_file_open.asp)
* [Brute Force Attacks](https://en.wikipedia.org/wiki/Brute-force_attack)

Your second challenge will have you brute force into a ZIP file to extract the secret code. 

> ZIP is a widely used archive file format that's used to compress one or more files together into a single location, reducing the overall size, and making it easier to transport the files. ZIP files work in much the same way as a standard folder on your computer. - Dropbox.com

In addition to compressing files, you are able to set a password protection on a ZIP file. These passwords are not immune from an attack known as a "Brute Force Attack"

> A brute force attack uses trial-and-error to guess login info, encryption keys, or find a hidden web page. Hackers work through all possible combinations hoping to guess correctly - Kaspersky.com

Manually typing in thousands of passwords one at a time can become time consuming, and in most cases impractical. This is where Python comes in handy. We will use a list of possible words to brute force our way into the example ZIP file. 

First thing we need to do is obtain our word list. For this we will use a text file containing all English words split up on individual lines. Follow [this link](https://github.com/dwyl/english-words/blob/master/words.txt) and right click to download the download icon. Save the file in your working directory for this program. 

Now startup your favorite text editor and lets start with our code!

## Code

Python has a built in library for handling ZIP files that we will import

```python
import zipfile
```

Next we will import our wordlist that we want to use in this brute force attack. Remember this is the text file you downloaded earlier you will need to change the "words.txt" to the name of the file you downloaded. It needs to be in the same directory as your Python script to be loaded correctly!

```python
wordlist = open("words.txt","rb").readlines()
```

Now we will load our target ZIP file and create an object that will allow us to open, read, write, close, and list the files. You will want to place your target ZIP file in the same directory as your python code. Change the "crackme.zip" to match the file name of the ZIP file you are targeting. 

```python
zip_file = zipfile.ZipFile("crackme.zip")
```

Just for fun let's print out the number of words in our "words.txt" by using the **len()** function.  

```python
print(len(wordlist))
```

Our list is made up for roughly 370 thousand words! Imagine having to hand type in all of these words one at a time!

We're now going to put this list to work with a **for** loop. In the for loop we will take one word at a time from our word list and try it against the ZIP file with the **extractall** method that is part of the zipfile library we imported. 

The **extractall** method takes a **pwd** argument that let's us pass in our word from the wordlist. We add the **strip()** method to the end of the word to help strip off the new line character which looks like **\n**.

You probably notice the **try/except/else** statements. The **try** and **except** is used for error handling, under normal circumstances, if we tried to pass an incorrect password into the **extractall** method, our program would come to a screeching halt with an error.

The **except** statement let's us ignore that error and go on to the next word by using **continue**.

If we do have a successful password, the program will move on to the **else** statement and print our our successful password!

```python
for word in wordlist:
    try:
        print(word.strip())
        zip_file.extractall(pwd=word.strip())
    except:
        continue
    else:
        print("Password found:", word.decode().strip())
        exit(0)
```

First one to email Mr. K with the contents of the included ZIP file with the password wins the bounty! Get hacking!
