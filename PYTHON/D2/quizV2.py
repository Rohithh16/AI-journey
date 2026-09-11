questions = [
    "Capital of India is",
    "1+1 equals",
    "King of the jungle is",
    "Shortest Minion is",
    "Chinese people speak"
]
answers = [
    "delhi",
    "2",
    "lion",
    "beatriz",
    "chinese"
]
score = 0

score = 0

for i in range(len(questions)):
    ans = input(questions[i] + ": ")

    if ans.lower() == answers[i]:
        print(ans, "is correct!")
        score += 1
    else:
        print(ans, "is wrong!")

        retry=input("TRY AGAIN:")

        if retry.lower()==answers[i]:
            print(retry, "is correct")
            score += 1
        else:
            print(retry,"is still wrong!")

print("Score:", score, "/5")















