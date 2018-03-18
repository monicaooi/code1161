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
# I think there will be an error because there is not quotation marks
for word in some_words:
    print(word) # it did not print word
# i think it will not print because "x" is not in the list 
for x in some_words:
    print(x) 
# i think it will print some_words = what, does, this, line, do, ?
print(some_words)#this printed some_words = what does this line do ?

if len(some_words) > 3:
    # I think it will print "some_words contains more than 3 words"
    print('some_words contains more than 3 words')#it printed "some_words contains more than 3 words"

#i dont know
def usefulFunction():# gave info on my laptop. really cool. 
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())

usefulFunction()
