import random
memorized_number = random.randint(1, 10)
print("Hi!,Am Thinking of a number beetween 1 and 10, guess my number")


def guess_number():
    guess_count = 0
    while (guess_count < 3):
        guessed_number = int(input().lower())
        guess_count += 1
        if (guessed_number == memorized_number):
            print('Wow!, You guessed my number correctly')
            break
        elif (guessed_number < memorized_number):
            print('Number is LOW!')
        elif(guessed_number > memorized_number):
            print('Number is HIGH!')
    else:
        print("You couldn't guess my number in " + str(guess_count) + " trials")
        print("I was thinking of " + str(memorized_number))
    return guess_number

guess_number() 