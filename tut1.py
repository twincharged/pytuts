# This is a comment. It's a way of leaving notes in your code!

# Here are the basic Python data types:

3                           # This is a number. It can be an integer, decimal number (3.45), etc
false                       # This is a boolean. It can be either true or false.
None                        # Exactly what it sounds like. It's a null value.
"Hey!"                      # This is a string. It can contain letters, numbers, or pretty much anything you want. It must be surrounded by single or double quotes.
[1, 5, "Hey", true]         # This is a list. It can contain multiple values. Must use brackets and commas.
{"name": "Joe", "age": 20}  # This is a dictionary. It's a bunch of corresponding keys and values. Must use braces, strings as keys, and commas.

# Here are basic mathematic operations:

1 + 1     # This is adding. It will equal two.
1 - 1     # Subtracting
1 * 1     # Multiplying
1 / 1     # Dividing

# Other:

my_variable = 4        # This is how you set a variable (named "my_variable" in this example) to a value

def my_function():     # This is a function named "my_function". Functions are way of grouping lines of code together that allows you to run them whenever you want.
  return 1 + 1         # You must define a function with the word "def", then the name of the function, followed by the arguments (which go in the parenthesis) then the colon. Everything indented beneath the "def" line is inside the funtion.
  
  
my_function()          # This is how you call a function (you have to use the parenthesis). This specific example will return the number 2.




# Here's an example of all that, but with function arguments too:

def add_numbers(num1, num2):
  return num1 + num2
  
add_numbers(5, 7)               # Will equal 12



# Etcetera:

def average(num1, num2, num3):
  sum = num1 + num2 + num3
  average = sum / 3
  return average
  
average(2, 3, 4)                # Will equal 3
