import re

pattern = r'spam' # use raw patterns
string = 'spamspam'

'''re.match() is similar to .startswith() but returns a match object or None rather than True or False. Match object has methods that can be used to give more information - see later'''

print(re.match(pattern, string)) # <_sre.SRE_Match object; span=(0, 4), match='spam'>
print(string.startswith(pattern)) # True

'''Match object evaluates to True, None to False'''

if re.match(pattern, string):
	print('Match')
else:
	print('No match')	# Match

'''re.search(pattern, string) searches the whole string'''

string = 'pamspam'

print(re.match(pattern, string)) # None
print(re.search(pattern, string)) # <_sre.SRE_Match object; span=(3, 7), match='spam'>

'''re.findall(pattern, string) returns a list of all substrings that match pattern'''

string = 'spamspam'

print(re.findall(pattern, string)) # ['spam', 'spam']

'''If pattern is a regex pattern rather than a string, list elements might not all be the same'''

'''re.finditer(p, s) is similar but returns an iterator:'''

print(re.finditer(pattern, string)) # <callable_iterator object at 0x11207a048>

'''Match object method demo:'''

pattern = r'pam'
string = 'eggspamsausage'
match = re.search(pattern, string)
if match:
	print(match.group()) # pam (this is the SUBSTRING MATCHED which == pattern here as pattern is non-regex)
	print(match.start()) # 4
	print(match.end()) # 7
	print(match.span()) # (4, 7)
	# etc
	
'''re.sub(this, that, string, count) is equivalent to string.replace(this, that, count), but slower and harder to read. Count is optional in both cases (number of subs to perform. Default = all)'''

this = 'sausage'
that = 'bratwurst'

new_string = re.sub(this, that, string)
print(new_string)

'''Patterns can be divided into groups with () to enable use of .group() and .groups() methods to see what each group is matching'''

pattern = r'(o)(m)'
string = 'omgy'
match = re.search(pattern, string)
print(match.group()) # om
print(match.group(1)) # o
print(match.group(2)) # m
print(match.groups()) # ('o', 'm')

'''Named groups can be accessed by group(name), as well as group(number). format: (?P<name>...)'''

pattern = r'(o)(?P<Mike>m)'
match = re.search(pattern, string)
print(match.group('Mike')) # m

'''Non-capturing groups have the format (?:...) and are not accessible by .group() or .groups(), so they CAN BE ADDED TO AN EXISTING REGEX WITHOUT BREAKING THE NUMBERING'''

# can't be bothered to put an example here


