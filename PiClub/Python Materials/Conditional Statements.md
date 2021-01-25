# Conditional Statements

## if Conditional Statements

Conditional statements allow us to build logic into our code. Our most basic statement is the **if** statement.

```python
if this:
    then that
```

Our first line checks to see if our condition is met. If this condition is met, then our statement will execute whatever is on line two.

A simple real life example might be, if it's raining, I will bring an umbrella.

```python
if rain:
    bring umbrella
```

Let's try this out in our terminal.

```python
if 9>4:
    print('True')
    
if 4>9:
    print('True')
```

What happened when you ran both if statements? 

You should have seen "True" printed for the first comparison, because 9 > 4 is True. 

You can probably guess why nothing was returned for the second statement. We know 9 is not greater than 4, so our print statement was never ran,

Python is flexible enough to do more than just numbers. The "**==**"can be used to compare strings. 

```python
name = 'John'

if name == 'John':
    print('Hello John, great to see you!')
```

We could even use '**in**' to search for string segments in larger strings. 

```python
if 'Goode' in 'Sarah Goode STEM Academy':
    print('True')
```

Python will search our long string and return true if it finds "Goode" in it! 

This could be handy if you were searching for a snippet of text in a long string.         

We could also search a list of items. Try it out.

```python
animals = ['cat','dog','mouse']

if 'cat' in animals:
    print('True')
```

Once again if you needed to confirm a single item in a list of thousands, this could be powerful. 

## else Clause

So we've addressed what we want our code to do if our condition is meant, but what should our code do if it doesn't meet our defined conditions? Que the **else** clause!

Let's take a quick look at what this would look like.

```python
if this:
    then that
else:
    then this
```

You can see we followed the **if** statement with the **else**. Pay attention to the semicolon in the code after both the **if** and **else** line. 

Let's try it out!

```python
if 10>100:
    print('True')
else:
    print('False')
```

Your code should print "False". We know 10 > 100 is false. This will trigger the **else** code and we should see "False" printed in the terminal. 

## elif Clause

Sometimes life isn't as simple as this or that. That's where the else if clause comes in, shortened to "**elif**" in Python.  

```python
if this:
    then that
elif this:
    then that
elif this:
    then that
```

You can see we can test for more than one condition with the **elif** clause.

Try it out with the code below.

```python
x = 5

if x == 1:
    print('X is 1')
elif x == 2:
    print('X is 2')
elif x == 3:
    print('X is 3')
elif x == 4:
    print('X is 4')
elif x == 5:
    print('X is 5')
```

 The code above sets our variable **x** equal to **5**. We then run it through our if/elif statement. Our variable **x** is tested against each if statement, but not until the very end does it test as true. 

You should see "x is 5" printed to your console. 

These are just some of the basics of Python's else\elif\if conditionals. I hope you can see how these would help you start creating more dynamic code. You can read more about conditionals bellow. 



> [Conidtitional Statements in Python - Real Python](https://realpython.com/python-conditional-statements/#introduction-to-the-if-statement)
>
> [Python If ... Else - W3 Schools](https://www.w3schools.com/python/python_conditions.asp)