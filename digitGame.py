# Reference : https://codeforces.com/problemset/problem/1419/A

# Input
# First line of input contains an integer t (1≤t≤100)  — the number of matches.

# The first line of each match description contains an integer n (1≤n≤103)  — the number of digits of the generated number.

# The second line of each match description contains an n-digit positive integer without leading zeros.

# Output
# For each match print 1, if Raze wins, and 2, if Breach wins.


def digit_game():
    matchCount = int(input())
    count = 1
    digitCountArry =[]
    numberArry =[]
    # Getting input and store it in different array set
    while (count <= matchCount):
        digitCountArry.append(int(input())) 
        numberArry.append(input()) 
        count = count+1
    
    #Print the result
    for index in range(0,matchCount):
        digitCount = digitCountArry[index]
        number = numberArry[index]
        
        if digitCount == 1:
            if int(number) % 2 == 0:
                print (2)
            else :
                print (1)
        else :
            
            if digitCount % 2 == 0:
                pos = 1
                isBreachWon = None
                while pos < digitCount:
                    if int(number[pos]) % 2 == 0:
                        isBreachWon = True
                        break 
                    pos = pos+2
                print (2) if isBreachWon else print (1)
                
            else :
                pos = 0
                isRazeWon = None
                while pos < digitCount:
                    if int(number[pos]) % 2 != 0:
                        isRazeWon = True
                        break 
                    pos = pos+2
                print (1) if isRazeWon else print (2) 

if __name__ =="__main__":
    digit_game()