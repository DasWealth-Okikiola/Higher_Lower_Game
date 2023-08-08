import random
from game_data import data
from art import logo, vs


def format_name(datas):
    """Formats Data And Returns Readable format"""
    name = datas['name']
    description = datas['description']
    country = datas['country']
    return f"{name} , A {description} from {country}."


def compare_followers(guess, a, b):
    """Take each follower count of users and compare them """
    if a > b and guess == "a":
        return True
    elif a > b and guess == "b":
        return False
    elif b > a and guess == "b":
        return True
    else:
        return False


print(f"Welcome To The Higher Lower Game \n {logo}")
cont = True
score = 0
with open("High_score.txt") as high:
    High_score = high.read()
Data2 = random.choice(data)
while cont:
    Data1 = Data2
    print(f'compare who has more followers?\n\n{format_name(Data1)}')
    print(vs)
    Data2 = random.choice(data)
    while Data2 == Data1:
        Data2 = random.choice(data)
    print(f"Against {format_name(Data2)}\n\n")

    choice = input("Press (A) for Option 1 and (B) for Option 2\n ").lower()

    Data1_followers = Data1['follower_count']
    Data2_followers = Data2['follower_count']
    # print(f'{choice}, {Data1_followers}, {Data2_followers}')

    right = compare_followers(choice, Data1_followers, Data2_followers)

    if right:

        score += 1
        print(f"You're right!!\nHigh_score is :{High_score}  \nYour Score is :{score}\n\n")
        if score > int(High_score):
            print("[Setting_a_new_High_Score]\n\n")
        if score >= 5:
            print("Amazing")
    else:
        print("Sorry you're Wrong!!")
        cont = False
        print(f"Final score = {score}\nHigh_score = {High_score}\n\n")
        if score > int(High_score):
            print(f"You Beat the HIGH_SCORE!!\nYour score:{score}\nHigh_score was:{High_score}")
            High_score = score
            with open("High_score.txt", mode="w") as High:
                High.write(f"{High_score}")
