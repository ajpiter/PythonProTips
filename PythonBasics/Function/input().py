## Function input()

#### input() allows us to create programs where the user provides additional information in the form of inputs. 

x = input()

#Now by calling 'x' anywhere in my program I get the value inputed by the user
x

#The default data type for inputs are strings 
#Multipling the input prints the interger value twice. 
print(x*2)
print(type(x))

#You can provide instructions for users on what to input by including a print() statement before the input() request
#Then convert the str to int() allowing for int multiplication 
print('Please input an interger value:')
x = input()
x = int(x)
print(x*2)

#Functional Composition 
#Requires users to input an integer value 
int(input('Please enter an integer value: '))
#Requires user to input a numeric value, including decimals 
int(float(input('Please enter a number: ')))
#Functional composition makes the program code simpler.

## Add if, ifelse or elif Statements 
#### By incorporating if statements into your input() functions you can control what values users are able to use 

TempC = int(input("Please enter the tempature in Celsius:"))
if TempC >= -90: # First check
    if TempC <= 58: # Second check
        print("The tempature in F is ", (TempC*2 + 30))
    else:
        print("Are you sure you entered the Tempature in C? ", TempC, " degrees Celsius is larger than the highest recorded temperature on earth which was 56.7.")
else:
    print("Are you sure you entered the Tempature in C?", TempC, "degrees Celsius is smaller than the lowest recorded temperature on earth which was -89.2.")
    
## Add print() Statements 
#### after a user has inputed a value 

#Even if there isn't an output indicate that the value was recieved 
print('Thank you for your input of ' + str(x))
#Classic minimal example 
print('Done')

#More descriptive print() statements help a user understand the result of the program 
#print('Given B = $' + str(B) + ', S = $' + str(S) + ' for ' + str(N) + ':')
#print('Your monthly management fee will be $' + '{:.2f}'.format(F) + ".")
#print("The total revenue from this sale will be $" + '{:.2f}'.format(TAR) + " and the commission earned by " + A + " will be $" + '{:.2f}'.format(C) + '.')
