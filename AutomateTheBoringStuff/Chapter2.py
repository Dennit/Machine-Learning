True and True
True and False
False and True
False and False

True or True
True or False
False or True
False or False

not True
not False
not not not True

print( 'What is your name')
name = input()
print( 'Enter a password')
password = input()
if name == 'Mary':
	print( 'Hello Marry')
	if password == 'swordfish':
		print( 'Access granted.')
	else:
		print( 'Wrong Password')
else:
	print( 'Hello m8')


# elif, secondary condition
if name == 'Alice':
	print( 'Hi, Alice')
elif age < 12: # Acts as an additional if statement under the assumption if is false
	print( 'not not not Alice')
elif age > 2000:
	print( 'xD')

# While loops
cupHead = 0

# The if condition runs through in only one iteration
if cupHead < 5:
	print( 'Cup Head still too small: ' + cupHead)
	cupHead += 1

# The while condition runs through until the condition is met
while cupHead < 5:
	print( 'Cup Head still too small: ' + cupHead)
	cupHead += 1

# Break Statements
while True:
	print( 'Please type your name.')
	name = input()
	if name == 'your name':
		break
print( 'asas')

# Continue Statement, terminates the current iteration and runs the next iteration
while True:
	print( 'Who are you')
	name = input()
	if name != 'Joe':
		continue
	print( name)