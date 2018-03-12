"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"
# I think the function will print "what, does, this, line, do,?" when you ask what some_words is because its given the list
some_words = ['what', 'does', 'this', 'line', 'do', '?'] #it printed "what, does, this, line, do,?"
# I think there will be an error because there is 
for word in some_words:
    print(word)
     #it printed "word"
# i think it will not print because "x" is not in the list 
for x in some_words:
    print(x) 

print(some_words)

if len(some_words) > 3:
    print('some_words contains more than 3 words')

def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())

usefulFunction()
