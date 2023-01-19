import time
import requests
import os

while True:
    os.system("clear")   #clear screen
    print("Getting a new quote...")
    result = requests.get(f"https://meowfacts.herokuapp.com/?count=1").json()
    quote = result["data"][0]
    wordcount = len(quote.split())
    print(quote)
    print("----------------------------------------")
    startTime=time.time()
    textInput=str(input("Type the sentence: " ))
    endTime=time.time()
    accuracy= len(set(textInput.split())&set(quote.split()))
    accuracy=accuracy/wordcount*100
    timeTaken=round(endTime-startTime,2)
    wpm=round(wordcount/timeTaken*60)
    print("----------------------------------------")
    print ("Your accuracy is: ", accuracy)
    print ("Time taken: ", timeTaken, "seconds")
    print("Your typing speed is: ",wpm,"words per minute")
    if accuracy < 50 or wpm < 30:
        print("You need to practice typing more!")
    elif accuracy < 80 or wpm < 60:
        print("You are doing great!")
    elif accuracy <= 100 or wpm <= 100:
        print("You are a pro in typing!")
    else:
        print("You are a typing machine!")
    choice = input("Do you want to try again? (y/n): ")
    if  choice == "y":
        continue
    else:
        break
