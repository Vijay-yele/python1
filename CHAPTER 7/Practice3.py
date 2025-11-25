# Write a function that takes a string and returns the count of vowels and consonents seprately

def countVovelsConsonents(userInput):
    vowels= "aeiouAEIOU"
    
    countVowels=0
    countConsonents= 0
    
    for eachChar in userInput:
        if(eachChar.isalpha()):
            if(eachChar in vowels):
                countVowels +=1
            else:
                countConsonents+=1

    return countVowels, countConsonents

vowels, consonents = countVovelsConsonents("Vijay Yele")

print(f"vowels are:{vowels} and consonents are;{consonents}")
