def quitA():
    quitA = str(input('do you want to go futher (yes) or (no)')) # this
    if quitA == 'yes' or quitA == 'Yes':
        return()
    elif quitA == 'no' or quitA == 'No':
        quit()
    else:
        print ('Invalid input, please enter yes or no ')
        quitA()

print('Welcome to the grade conversion')
print('You can quit at any time')
quitA()
grade = int(input('Please insert the marks you recieved  \n'))
quitA()
if grade < 40:
    print("You have recieved an F")
elif grade >= 40 or grade == 50:
    print('You have recieved a D')
elif grade >= 50 or grade == 60:
    print('You have recieved a C')
elif grade >= 60 or grade == 70:
    print('You have recieved a B')
else:
    print('You have recieved an A')




    
