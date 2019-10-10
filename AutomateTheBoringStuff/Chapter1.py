# // -> Integer Division/ Floor Quotion,	22/8 == 2    -> Converts to Int
# // -> Regular Division					22/8 == 2.75 -> Converts to Float
# 'A' * 5 = 'AAAAA'
# 'A' * 5.0 => Type Error: Can't multiply sequency by non-int of type 'str'
# 'StringA' + 'StringB' vs other concatenating techniques? efficiency

# Name Error: true ( name 'true' is not defined)
# Syntax Error: 5 + * 2 ( Invalid Syntax)
#				True = 2 + 2 ( Assignment to keyword)
# Value Error: int( '99.99') ( invalid literal for int() with base 10: '99.99')
#			   int( 'Twelve') ( invalid literal for int() with base 10: 'Twelve')
# Type Error: 'ABC' * 'BAC'( Can't multiply sequence by non-int of type 'float')
#			  'ABC' * 5.0  ( Can't multiply sequence by non-int of type 'float')
#			  'Alice' + 52 ( Can't convert 'int' object to str implicity)

print( 'Hello World')
print( 'What is your name')
myName = input()
print( 'It is good to meet you ' + myName)
print( 'The length of your name is:')
print( len( myName))
print( 'What is your age?')
myAge = input()
print( 'Your age is ' + myAge)

# str(), int(), float(); input as: string, int, or float
# str()
#	Having integer or floats and want to concatenate them to a string
# int()
#	Converting a string that represents a number
# input()
#	Always will return a string, you might need to convert to an int or a float

print ('int( 7.7)')
int( 7.7)
print ('int( 7.7) + 1')
int( 7.7) + 1
print( '42 == "42"')
42 == '42'
