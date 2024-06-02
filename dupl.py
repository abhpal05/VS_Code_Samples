import random as r


start_point = 1
end_point = 30

def play_snake_ladder_game(n, s, d):
    
    # Dictonary for Ladder
    ladder_dictorary ={
    3:22
    ,5:8
    ,11:26
    ,20:29
    }
    # Dictonary for Snake
    snake_dictorary = {
    17:4
    ,19:7
    ,21:9
    ,27:1
    }

    player_position_dictonary = {}
    player_list = []
    for x in range(1, n+1):
        player_name = input("Enter your name: ")
        player_position_dictonary[player_name] = 1
        player_list.append(player_name)
    
    while True:
        for y in player_list:
            play_choice = input(y + ", please roll the dice (Y to Roll, N to Withdraw)")
            if (play_choice.upper() == 'N'):
                print("Its a shame, you could have win the game.")
                player_list.remove(y)
                if(len(player_list) == 1):
                    print("Congratulations " + player_list[0] + ", you have won the game, because others have left the game.")
                    break;
            elif(play_choice.upper() == 'Y'):
                dice_number = r.randint(1,6)
                print(y + ", you got " + str(dice_number))
                player_position_dictonary[y] = player_position_dictonary[y] + dice_number
                print(y+ ", your position is " + str(player_position_dictonary[y]))
                if(player_position_dictonary[y] > d):
                    player_position_dictonary[y] = player_position_dictonary[y] - dice_number
                    print(y + ", your position is still on " + str(player_position_dictonary[y]) + ". You need " + str(d - player_position_dictonary[y]) + " to reach destination.")
                    print("Dice again")
                else:
                    for ladder_point in ladder_dictorary:
                        if(player_position_dictonary[y] == ladder_point):
                            player_position_dictonary[y] = ladder_dictorary[ladder_point]
                            print("Great! " + y + ", you got ladder and your new position is " + str(player_position_dictonary[y]))
                    for snake_point in snake_dictorary:
                        if(player_position_dictonary[y] == snake_point):
                            player_position_dictonary[y] = snake_dictorary[snake_point]
                            print("OOPS! " + y + ", you got snake and your new position is " + str(player_position_dictonary[y]))
                    if(player_position_dictonary[y] == d):
                        print("Congratulations " + y + ", you have reached the Destination.")
                        player_list.remove(y)
                        break;



print("\n")
print("Welcome to Snake game (in python way)")
print("\n")
no_of_player = int(input("How many players are going to play: "))
print(play_snake_ladder_game(no_of_player,start_point,end_point))
play_snake_ladder_game(no_of_player, start_point, end_point)