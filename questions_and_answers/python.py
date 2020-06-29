import random

# topics

basics = [
	('What is floor division and how is it done?',
    'Rounds the result of the division down to the nearest integer. Using //'),
	('What is the modulo operation and how is it done?',
    'Finds the remainder in a division. Using %, e.g. 4 % 2 = 0. Negative numbers are weird, see Quora.'),
	('How do you escape a character in a string?',
    'Using \\.'),
	('An if statement is run only when...',
    '...its condition evaluates to True.'),
	('The statements inside a while statement execute repeatedly until...',
    '...it evaluates to False.'),
	('How do you break a loop?',
    'Using the break statement.'),
	('What does the continue statement do?',
    'Stops the current iteration and continues with the next one.'),
	('What does dir() do?',
    'Displays all of the attributes and methods of the specified object.'),
	('What does type() do?',
    'Displays the type of an element.'),
	('What does help() do?',
    'Invokes the built-in help system.'),
	('What is a keyword?',
    'A word that defines Python syntax or structure. Cannot be used as a variable name.'),
	("What are Python's Boolean operators?",
    'And, or and not.'),
	('What data structures does Python support?',
    'Lists, dictionaries, tuples and sets.'),
	('a and b evaluates to False unless...',
    'Both are True.'),
	('a or b evaluates to True unless...',
    'Both are False.'),
	]
	
strings = [
	('What does the .join() do?',
    'Joins a list of strings with another string as a separator.'),
	('What does the .replace() do?',
    'Replaces one substring within a string with another.'),
	('What does the .split() do?',
    'Turns a string into a list of strings.'),
	('What does .lower() do?',
    'Returns a string in all-lowercase.'),
	('What does .higher() do?',
    'Returns a string in all-uppercase.'),
	('What does .startswith() do?',
    "Returns True if the associated string starts with the argument within the (), and False if it doesn't."),
	('What does .endswith() do?',
    "Returns True if the associated string ends with the argument within the (), and False if it doesn't."),
	('What does eval() do?',
    'Executes an arbitrary string as Python code.'),
	('What does .zfill() do?',
    'Makes a string a defined number of characters in length by padding its left side with zeroes.'),
	]
	
lists = [
	('What are lists for and how are they created?',
    'Storing an indexed list of items. With square brackets and a comma between items.'),
	('How to check if an item is in a list?',
    'Using in operator e.g. print(*item* in *list*).'),
	('What is a method?',
    'Like a function, but runs on an object.'),
	('What does .append() do?',
    'Adds an item to the end of a list.'),
	('What does .insert() do?',
    'Allows you to insert an item at any position in a list.'),
	('What does .index() do?',
    'Finds the first occurence of a list item and returns its index.'),
	('Compare lists and sets.',
    'Sets cannot be indexed or contain duplicate elements, unlike lists. Because sets do not assign indices to their elements, they use less memory.'),
	('What does .reverse() do?',
    'Reverses the order of a list.'),
	]
	
tuples = [
	
	]
	
sets = [
	('What does .add() do?',
    'Adds an element to the end of a set.'),
	('What does .remove() do?',
    'Removes a specific element from a set.'),
	('What does .pop() do?',
    'Removes and returns a specific element from a list.'),
	('What is the union operator and what does it do?',
    '|. Combines two sets.'),
	('What is the intersection operator and what does it do?',
    '&. Gets items only in both sets.'),
	('What is the difference operator and what does it do?',
    '-. Gets items that are in the first set but not the second.'),
	('What is the symmetric difference operator and what does it do?',
    '^. Gets items that are in one set or the other, but not both.'),
	]
	
dictionaries = [
	('Dictionaries are indexed according to...',
    'Key.'),
	('Why use a dictionary?',
    'For fast key-based lookup.'),
	('What does .keys() do?',
    "Returns dict_keys() with a list of the dictionary's keys in it. Likewise the values() method. Use list(whatever.keys()) if you just want the list."),
	('What does .get() do?',
    "Dictionary method. Returns the value of a key, or - if the key doesn't exist - a specified value (none, by default)."),
	]
	
regex = [
	('How to access regular expressions?',
    'Import the re module (part of the standard library.)'),
	('What are raw strings? Why and how are they used?',
    'They don\'t escape anything, making use of regular expressons easier. Use r"whatever".'),
	('What does re.match() do?',
    'Checks if a defined expression matches the beginning of a string.'),
	('What does re.search() do?',
    'Finds a match of a pattern anywhere in a string.'),
	('What does re.findall() do?',
    'Returns a list of all substrings that match a pattern.'),
	('What does re.finditer() do?',
    'Returns an iterator of all substrings that match a pattern.'),
	('What does the metacharacter * mean?',
    'Zero or more repetitions of the previous thing (character, class or group of characters in parentheses).'),
	('What does the metacharacter + mean?',
    'One or more repetitions of the previous thing.'),
	('What does the metacharacter ? mean?',
    'Zero or one repetitons of the previous thing.'),
	('What does the metacharacter | mean?',
    'Or.'),
	('What does the metacharacter . match?',
    'Any character, other than a new line.'),
	('What does the metacharacter ^ match?',
    'The start of a string.'),
	('What does the metacharacter $ match?',
    'The end of a string.'),
	('What does the pattern "^gr.y$" match?',
    'A string that starts with gr, follows with any character other than a newline, and ends with y.'),
	('Regex: what are character classes and how are they created?',
    "A way to match one of a specified set of characters. Using square brackets, e.g. pattern = r'[aeiou]' matches any string that contains a lower-case vowel."),
	('Regex character classes: what does [G-P] match?',
    'Any upper case letter from G to P.'),
	('Regex character classes: what does [A-Za-z] match?',
    'A letter of any case.'),
	('Regex character classes: what does ^ do?',
    'If placed at the start of the class, inverts it, i.e. causes it to match any character other than the ones included. For example, [^A-Z] excludes all-upper-case strings.'),
	('Regex: how are curly braces used?',
    'To specify the number of repetitions of the previous thing. For example, {0, 1} is the same as ?.'),
	('Regex: what does a backslash followed by another character signify?',
    'A special sequence. Various uses, depending on character.'),
	('Regex: what does the special sequence \d match? What about \D?',
    'Digits (equivalent to [0-9]). Upper case inverts meaning [^0-9].'),
	('Regex: what does the special sequence \s match? What about \S?',
    'Whitespace i.e. [\\t\\n\\r\\f\\v]. Upper case inverts meaning. Can probably forget about \\r (carriage return), \\f (formfeed), \\v (vertical tab).'),
	('Regex: what does the special sequence \w match? What about \W?',
    'Word characters i.e. [a-zA-Z0-9_]. Upper case inverts meaning.'),
	('Regex: what does (\D+\d) match?',
    'One or more non-digits followed by a digit.'),
	('Regex: what does the special sequence \A... match?',
    '... if it is at the start of the string.'),
	('Regex: what does the special sequence \Z... match?',
    '... if it is at the end of the string.'),
	('Regex: what does the special sequence \\b... match?',
    '... if it is at the beginning of a word.'),
	('Regex: what does the special sequence ...\\b match?',
    '... if it as at the end of a word.'),
	('Regex: what does the special sequence \\b represent? What about \B?',
    'Basically, the boundary between words (transition from a non-word character to a word character or vice-versa). Upper case is the opposite - will match if the specified characters are NOT at the beginning or end of a word.'),
	]
	
functions = [
	("What is returned by functions that don't have a return statement?",
    'None.'),
	('What does map() do?',
    'Applies a function to an interable to create a new iterable.'),
	('What does filter() do?',
    'Removes items from an iterable.'),
	('How do you create a generator?',
    'Using a function and the yield statement.'),
	('Compare lists and generators.',
    "Lists allow indexing, generators don't. For loop works on both. Generators use less memory."),
	('In short, generators allow you to...',
    'Declare a function that can be used in a for loop.'),
	('How is the keyword pass used?',
    'Generally as a placeholder. Nothing happens when pass is executed. Stops the interpreter complaining if you have e.g. a not-yet-complete function.'),
	('What is the correct order for named arguments without default values, named args with, and *args?',
    'Named args without, named args with, then *args.'),
	('How are *args accessed inside a function?',
    'As the tuple args. Note no *.'),
	('What does **kwargs return?',
    'A dictionary in which the keys are the argument names, and the values are the argument values.'),
	('What are decorators?',
    'Functions that modify other functions.'),
	('What are the argument-unpacking and keyword argument-unpacking operators?',
    '* and **.'),
	]
	
misc = [
	('How do you access the Zen of Python?',
    'Import this.'),
	('Range can have a third argument. What does it do?',
    'Determines the interval of the sequence produced.'),
	('How do you import a module or object under a different name?',
    'Using the as keyword.'),
	('What is PyPI?',
    'Python Package Index - a library of third-party modules.'),
	('What are assertions useful for?',
    'Catching your own errors.'),
	('How do you close a file?',
    '3 ways:\nUse the close method \nUse the close method in conjunction with try and finally, so it closes even if an error occurs \nUsing with open(file) as (usually) f - the file is automatically closed at the end of the with statement, even if exceptions occur within it.'),
	('How is else used with try/except statements?',
    'The code within it is only executed if no error occurs in the try statement.'),
	('What is packaging?',
    'Putting modules you have written in a standard format, so that other programmers can install and use them with ease.'),
	('What is the American Standard Code for Information Interchange?',
    'A character-encoding scheme that is used to represent text in computers.'),
	('What does .choice() do? In which module is it found?',
    'Returns a random value from a list. In the random module.'),
	('What is short-circuiting?',
    "Where Python evaluates an expression only part-way because the rest doesn't change what it evaluates to."),
	('Can you store a list or dictionary in a variable?',
    'No - only a reference.'),
	('What are docstrings?',
    "Multiline strings containing an explanation of a function below a function's first line"),
	('How does the is keyword differ from the == operator?',
    'is tests if two variables refer to the same object. == tests if two variables are equal.'),
	('What is the difference between .reverse() and reversed()?',
    '.reverse() reverses the elements in the container. reversed() creates an object that can be used to iterate over the container\'s elements in reverse order (often faster, if that\'s what you need). reversed() works on strings, .reverse() doesn\'t.'),
	]
	
master = basics + strings + lists + tuples + sets + dictionaries + regex + functions + misc
total_questions = len(master)
topics_dict = {'1': basics, '2': strings, '3': lists, '4': tuples, '5': sets, '6': dictionaries, '7': regex, '8': functions, '9': misc}
	
print("Welcome to Michael's Python revision program!")
print("The program will ask a question. Press enter to reveal the answer.")
print(f'There are currently {total_questions} questions in total.') # shit - lost one from Revision2
print()


while True:
	print('Choose topics: Enter a number or numbers, or nothing for all topics.')
	topics_chosen = []
	print('1 basics\n2 strings\n3 lists \n4 tuples \n5 sets\n6 dictionaries\n7 regex\n8 functions\n9 misc')
	user_input = input()
	if user_input:
		for i in user_input:
			if i.isnumeric():
				topics_chosen.extend(topics_dict[i])
	else:
		topics_chosen += master
	print()
	random.shuffle(topics_chosen)
	for i, j in topics_chosen:
		print('Q.', i)
		input()
		print('A.', j)
		print()
	print('All questions asked. Restarting:')