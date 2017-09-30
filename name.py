# This program says hello and asks for my name

print ('Hello World!')

print ('What is your name?') # ask for their name
myName = input ()
print ('It is good to meet you, ' + myName)
print ('The length of your name is:')
print (len(myName))

print ('What is your age?') # ask for their age
myAge = input ()
print ('You will be ' + str(int(myAge) + 1) + ' in a year.')

print ('What is your gender?') # ask for their gender
myGender = input ()
print ('You are a ' + myGender)

print ('Please ask who you are, and I will tell you.') # ask who they are
myWho = input ()
print (myName + ', you are ' + myAge + ', and you are a ' + myGender + '.')
