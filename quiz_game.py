#!/usr/bin/env python3

score = 0
print("Welcome to my computer quiz!")

playing = input("Would you like to play? ")

if playing.lower() != "yes":
    quit()
else:
    print("Cool!")

answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("You are correct!")
    score += 1
else:
    print("You are wrong")

answer = input("What does GPU stand for: ").lower()
if answer == "graphics processing unit":
    print("You are correct!")
    score += 1
else:
    print("You are wrong")

answer = input("What does RAM stand for? ").lower()
if answer == "random access memory":
    print("You are correct!")
    score += 1
else:
    print("You are wrong")

print(f"You got {score} questions correct")
print(f"A percentage of {(score / 3) * 100} %")
