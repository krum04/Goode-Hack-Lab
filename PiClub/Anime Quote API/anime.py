# import libraries
import requests

# define page URL
pageUrl = 'https://animechanapi.xyz/api/quotes/random'

# request data from page url
page_data = requests.get(pageUrl)

# let's view the data returned from our page_data object
print(page_data)

# create a variable using the .json method to return the page data and print
page_parsed = page_data.json()
print(page_parsed)

# create variable containt just the quote,character, and anime key value pairs
quote_data = page_parsed['data'][0]

# print out the quote, anime, and character
print(quote_data['quote'])
print(quote_data['anime'])
print(quote_data['character'])
