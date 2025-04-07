#Take input of a word
string = input("Please Enter Your Own Word : ")
#take input of a character
char = input("Please Enter a Character to Check : ")
i = 0
count = 0
#loop will to find the occurence of character
while(i < len(string)): #string operation
    if(string[i] == char): #condition 1
        count = count + 1
    i = i +1
#Display the Result
print("The Total Number of Times ", char, " has Occurred = ", count)
