mystring = input()

def isPelindrome(word):
    return (word == word[::-1])

if(isPelindrome(mystring)) :
    print(1)
else :
    print(0)