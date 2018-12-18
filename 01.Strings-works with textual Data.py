          #01.Strings-Work with textual Data#

#Strings
print('Hello World')

#Strings with Variable

message = 'Hello World' 

print(message)

print(len(message))

#String Indexing & Slicing

print(message[0:5])
print(message[6:])

#Upper and lower case
print(message.upper())

print(message.lower())

#Count Method

print(message.count('Hello'))
print(message.count('l'))
print(message.count('p'))

#find method

print(message.find('World'))

print(message.find('r'))

#replace Method
new_message = message.replace('World', 'Universre')
print(new_message)
print(message)
#print(message.replace('World', 'Universre'))

#Here 'message' is a variable name and 'Hello world' is it's
#Value

#Concetenation(combining strings):
greeting = 'Hello'
name = 'William'
#as usual 
another_message = greeting + ', ' + name + '. welcome!'

print(another_message)
#.format Method
next_message = '{}, {}. Welcome!'.format(greeting, name)

print(next_message)
#f' Method
message2 = f'{greeting}, {name.upper()}. Welcome!'

print(message2)

#What can we with a variable? ans!
#print(dir(name))

#for any help type....

#print(help(str.lower))

