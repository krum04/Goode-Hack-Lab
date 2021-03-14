# Anime Quote Generator

## "It's Over 9000!"

![Over 9000](https://upload.wikimedia.org/wikipedia/en/9/9f/Over_9000%21.png)

This will be a multi step project that will combine APIs and Python's PIL module to generate images overlaid with anime quotes. 

## Part 1: Getting Our Quote

We are going to use a free API found here: https://animechanapi.xyz/

This API lets us get quotes by Character, Anime, or Randomly.

We can read the [documenation here](https://animechanapi.xyz/documentation)

There are four ways we can query the API. 

1. "Quotes" - Will return 10 random quotes

   1. ```text
      https://animechanapi.xyz/api/quotes
      ```

2. "Random" - Will return 1 random quote

   1. ```text
      https://animechanapi.xyz/api/quotes/random
      ```

3. "By Anime" - returns quotes by anime

   1. ```text
      https://animechanapi.xyz/api/quotes?anime=naruto
      ```

4. "By Character" - returns quotes by character

   1. ```text
      https://animechanapi.xyz/api/quotes?char=madara uchiha
      ```

Try pasting these different URLs in your address bar and seeing what you get in return. 

If done correctly, you should get a JSON return that looks something like this. 

```json
{
"status": "ok",
"statusCode": 200,
"data": [
{
"quote": "SLEEPING is the only TALENT I have.",
"character": "Nagi Sanzenin",
"anime": "Hayate no Gotoku!"
}
]
}
```

This JSON format is a neatly wrapped package of data just waiting to be parsed by our script!

Let's break it down real quick.

**status:** this simply tells our program that the request was successful

**statusCode: **this again lets our program know that the request was successful, but gives a numerical code. These are good for troubleshooting when your requests isn't successful. Bellow is a general overview of what these codes relate to. 

* Informational responses (`100`–`199`)
* Successful responses (`200`–`299`)
* Redirects (`300`–`399`)
* Client errors (`400`–`499`)
* Server errors (`500`–`599`)

**data:** here is the good stuff we are looking for,it contains our **quote:, character:, and anime: ** fields!

### Program

Now it's time to get this data into our scripts. For this we will use the **requests** library, similar to how we wrote our joke script a while back. Let's start a new python file and save it as **anime.py** and import the **request**.

```python
import requests
```

Now let's create the variable that will hold our URL for our API request. 

```python
pageUrl = 'https://animechanapi.xyz/api/quotes/random'
```

Let's send a request to that page and save its returned data as a variable called "**page_data**".

```python
page_data = request.get(pageUrl)
```

Go ahead and run your script. If everything working properly, you should get nothing in return. 

Let's see what is hiding in that **page_data** variable that we created with the **print** function.

```python
print(page_data)
```

Did you get **<Response [200]>**? If you did congrats, but where's the quote? For that we need to call the **json method** from our **page_data** object and print it out. 

To keep things tidy, we will create a variable containing just this json data called **page_parsed** and print it out. 

```python
page_parsed = page_data.json()
print(page_parsed)
```

You should get the following in the terminal. 

> {'status': 'ok', 'statusCode': 200, 'data': [{'quote': "Getting dumped always makes a man stronger. But then again, men aren't meant to pursue happiness.", 'character': 'Jiraiya', 'anime': 'Naruto'}]}

If we look closely we can make out the keys that we are interested in. 

We will cover these datatypes in the future, but what we have is a dictionary with a nested list containing another dictionary. 

To get down to the data we want we are going to create a new variable called **quote_data** containing just the quote, character, and anime key/value pairs..

```python
quote_data = page_parsed['data'][0]
```

We can now call on the data we want with keywords. To do that we enter our variable['keyword']. Try it out with the code below. 

```python
print(quote_data['quote'])
```

Try changing 'quote' to character or anime and see what you get in return!

Congrats, you've successfully wrote your program to fetch data from the web and use it in a useful format!

## Part 2 : Getting Our Image

Now that we know how to obtain our epic quotes, it's time to get a fitting image! For this we are going to use the Giphy API. The Giphy API requires us to sign up and obtain our own key to access the API. 

**API Keys** are used to grant permissions to developers, these may be used to cap access to the API and other features.

1.  [Sign-Up for a Giphy Account Here](https://giphy.com/login)
2. [Create a new app access here](https://developers.giphy.com/dashboard/?create=true)
   1. Select SDK and click "Next Step"
   2. Enter a name for your app and a brief description. I.E.
      1. My First App
      2. Testing my Python Script
3. Click "Create App"

Great now you should see a screen with your API Key. In practice you want to keep this key secret, if you think your key has leaked out, you can always cancel it and have a new one generated. 

![](https://github.com/krum04/Goode-Hack-Lab/blob/main/PiClub/Anime%20Quote%20API/ReadMe%20Images/Giphy%20API%20Explorer%20Screen.PNG?raw=true)

Let's see what we can do using the [API Explorer Here](https://developers.giphy.com/explorer).

For the "Choose endpoint" drop down choose "Search"

This should unlock the Parameters to the right. 

| **Parameter** | Description                |
| ------------- | -------------------------- |
| q             | Our search query           |
| limit         | Number of results returned |
| offset        | Result offset              |
| rating        | Content rating             |
| lang          | Default language           |
|               |                            |

By default your **Request URL** should look like this (I've omitted the API Key):

> https://api.giphy.com/v1/gifs/search?api_key=MYSECRETAPIKEY&q=&limit=25&offset=0&rating=g&lang=en

Everywhere we see a "&", also known as an ampersand, we have a new parameter. You can see "**api_key**", "**limit**", "**offset**","**rating**, and "**lang**". If you pay attention to URLs that you use everyday, you will start to notice this pattern. 

Let's try out our first Giphy API query:

Enter "Naruto" into the **q** field and change the **limit** to "1" so we only get a single result and hit "Send Request".

We should see a response in Json bellow. If you scroll down and find "original" we can get the direct url to our gif list after the 'url' entry.

![](https://media3.giphy.com/media/JRlqKEzTDKci5JPcaL/giphy.gif?cid=6208bce65e9t95d82waz0iuyu8kpu04pz1hotgml3jb2i0cn&rid=giphy.gif)

Awesome right! 

Now lets bring this function into our python script!

We will need to create a new API that concatenates our Anime name returned from our first API and the Giphy API URL. To do that we enter the following under our print statements at the end of our code.

```python
search_term = quote_data['anime']
```

This sets a search_term variable to the result of our anime name from the Anime API.

Now we will concatenate, or simply combine our strings to generate our request URL. To do that we will want to grab that demo url from the API explorer and combine it with our **serach_term** variable.  

We will create a new variable with  these combined strings. I've removed the API key from this example, but you will leave yours in. 

```python
giphy_api_url = f"https://api.giphy.com/v1/gifs/search?api_key=MYSECRETKEY={search_term}&limit=1&offset=0&rating=pg&lang=en"
```

Quick note about the **{}** in this example. When you precede a string with **f** you are able to insert variables between the squiggly brackets **{}**. You can see that in our squiggly brackets we have passed in our **search_term** variable.

Now we are able to pull down that Json result form Giphy. To do that we will use the requests module again and save the results to our **giphy_json** variable .

```python
giphy_json = requests.get(giphy_api_url).json()
```

Because our final url containing the direct Gif is inside the Json file, we have a bit of a Russian nesting doll situation. We will step through the Json file to grab this URL and set it to a variable named gifUrl.

```python
gifUrl = giphy_json['data'][0]['images']['original']['url']
```

If you look back at formatted Json return in the API explorer, you can follow our path to the Url with the ordered keys above. 

We now need to do one final request for the image data from the gifUrl and save it locally.

```python
gif_request = requests.get(gifUrl)
```

Now we will create a file named "anime.gif" and save our image data to it. 

```python
with open('anime.gif', 'wb') as f:
    f.write(gif_request.content)
```

Now if you run your script, you should have a Gif saved in your working directory relevant to your quote!