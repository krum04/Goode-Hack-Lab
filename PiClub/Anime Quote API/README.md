# Anime Quote Generator

## "It's Over 9000!"

![Over 9000](https://upload.wikimedia.org/wikipedia/en/9/9f/Over_9000%21.png)

This will be a multi step project that will combine APIs and Python's PIL module to generate images overlaid with anime quotes. 

## Part 1

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

Now it's time to get this data into our scripts. For this we will use the **request** and **json** libraries. Similar to how we wrote our joke script a while back. Let's start a new python file and save it as **anime.py**.

Next we can import the libraries.

```python
import requests
import json
```

Now let's create the variable that will hold our URL for our API request. 

```python
pageURL = 'https://animechanapi.xyz/api/quotes/random'
```

Let's send a request to that page and save its returned data.

```python
page_data = request.get(pageUrl)
```

Go ahead and run your script. If everything working properly, you should get nothing in return. 

Let's see what is hiding in that **page_data** variable that we created with the **print** function.

```python
print(page_data)
```

Did you get **<Response [200]>**? If you did congrats, but where's the quote? For that we need to call on our **Json** library to extract the data from our **page_data** object and print it out. 

```python
page_parsed = page_data.json()
print(page_parsed)
```

You should get the following in the terminal. 

```tex
{'status': 'ok', 'statusCode': 200, 'data': [{'quote': "Getting dumped always makes a man stronger. But then again, men aren't meant to pursue happiness.", 'character': 'Jiraiya', 'anime': 'Naruto'}]}
```

If we look closely we can make out those keys that we are interested in. 

We will cover these datatypes in the future, but what we have is a dictionary with a nested list containing another dictionary. 

To get down to the data we want we are going to create a new variable.

```python
quote_data = page_parsed['data'][0]
```

We can now call on the data we want with keywords. To do that we enter our variable['keyword']. Try it out with the code below. 

```python
print(quote_data['quote'])
```

