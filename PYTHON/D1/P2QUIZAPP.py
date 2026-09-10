score = 0

ans = input("Capital of India is: ")
ans2 = input("1+1 equals: ")
ans3 = input("King of the jungle is: ")
ans4 = input("Who is the shortest Minion? ")
ans5 = input("Chinese people speak: ")

if ans.lower() == "delhi":
    print(ans, "is correct!")
    score += 1
else:
    print(ans, "is wrong!")
    retry = input("TRY AGAIN: ")

    if retry.lower() == "delhi":
        print(retry, "is correct!")
        score += 1
    else:
        print(retry, "is still wrong!")
print()

if ans2.lower() == "2":
    print(ans2, "is correct!")
    score += 1
else:
    print(ans2, "is wrong!")
    retry = input("TRY AGAIN: ")

    if retry.lower() == "2":
        print(retry, "is correct!")
        score += 1
    else:
        print(retry, "is still wrong!")
print()

if ans3.lower() == "lion":
    print(ans3, "is correct!")
    score += 1
else:
    print(ans3, "is wrong!")
    retry = input("TRY AGAIN: ")

    if retry.lower() == "lion":
        print(retry, "is correct!")
        score += 1
    else:
        print(retry, "is still wrong!")

print()

if ans4.lower() == "beatriz":
    print(ans4, "is correct!")
    score += 1
else:
    print(ans4, "is wrong!")
    retry = input("TRY AGAIN: ")

    if retry.lower() == "beatriz":
        print(retry, "is correct!")
        score += 1
    else:
        print(retry, "is still wrong!")

print()

if ans5.lower() == "chinese":
    print(ans5, "is correct!")
    score += 1
else:
    print(ans5, "is wrong!")
    retry = input("TRY AGAIN: ")

    if retry.lower() == "chinese":
        print(retry, "is correct!")
        score += 1
    else:
        print(retry, "is still wrong!")
print()
print("Score:", score, "/5")





    
