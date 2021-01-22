# importing Image class from PIL package  
from PIL import Image  
  
# creating a image objects  
correctImg = Image.open(r"correct.png")
incorrectImg = Image.open(r"incorrect.png")

# set correct "password"
correctPass = "password"
userInput = input("Please enter your password: ")

# test to see if the user has input the correct answer and display correct images
if userInput == correctPass:
    correctImg.show()
else:
    incorrectImg.show()