word = "laptop"
lives = 4
answer = "_"*len(word)
print(f"Welcome to Hangman Game. You have {lives} lives to guess the word.")
print(answer)

while lives > 0:
    ans = input("Enter your guess : ")
    print(f"Your guess is {ans}")
    if ans in word:
        print("you guess correct letter")
        characters = list(answer)
        index = 0
        for char in word:
            if char == ans:
                characters[index] = ans
            index += 1
        answer = "".join(characters)
        if answer in word:
            print("\n\n")
            print("*"*20)
            print("Congratulations...!!!You wan the Game...!!!")
            print("*" * 20)
            break
        print(answer)
    else:
        lives -= 1
        if lives > 0:
            print("*"*20)
            print(f"You guess wrong letter. {lives} more to go...best of luck...")
            print("*" * 20)

if "_" in answer:
    print("\n\nSorry :( You lost the Game...!!!")


print("Thanks for Playing Hangman Game")
print("-"*80)


