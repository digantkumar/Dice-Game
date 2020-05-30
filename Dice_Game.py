# Digant Kumar

import random

# A function that keeps on simulating two dice until they both yield the same value, and returns the length of the game.
def play():
    count = 0
    prev_throw = random.randint(1,6)
    next_throw = random.randint(1,6)
    count += 2
    while prev_throw != next_throw:
        prev_throw = random.randint(1, 6)
        next_throw = random.randint(1, 6)
        count += 2
    return count

# Function that simulates 1000 runs of the game and prints the average and maximum run length
def simulations():
    length = 1
    max_count = 1
    average = 0
    len_dict = {}
    while length != 1000:
        new_game = play()
        average = average + new_game
        if new_game > max_count:
            max_count = new_game
        length += 1
        if new_game in len_dict:
            len_dict[new_game] += 1
        else:
            len_dict[new_game] = 1
    print("The maximum run length is: ",max_count)
    print("The average run length is: ",average/length)
    return len_dict

# Function that shows graphically the result of the 1000 simulations of the game above.
# Here, an asterisk represents five runs of the game.
# Considering the runs of length less than 200 only
def hist():
    total_len = simulations()
    sorted_dict = sorted(total_len.items())
    zero_nine,ten_19,twenty_29,thirty_39,forty_49,fifty_59,sixty_69 = 0,0,0,0,0,0,0
    seventy_79, eighty_89, ninety_99, one100_one109, one110_one119, one120_one129 = 0, 0, 0, 0, 0, 0
    one30_one39, one40_one59, one50_one59,one60_one69,one70_one79,one80_one89,one90_one99 = 0,0,0,0,0,0,0
    for key,value in sorted_dict:
        if key >= 0 and key <= 9:
            zero_nine = zero_nine + value
        elif key >= 10 and key <= 19:
            ten_19 = ten_19 + value
        elif key >= 20 and key <= 29:
            twenty_29 = twenty_29 + value
        elif key >= 30 and key <= 39:
            thirty_39 = thirty_39 + value
        elif key >= 40 and key <= 49:
            forty_49 = forty_49 + value
        elif key >= 50 and key <= 59:
            fifty_59 = fifty_59 + value
        elif key >= 60 and key <= 69:
            sixty_69 += value
        elif key >= 70 and key <= 79:
            seventy_79 += value
        elif key >= 80 and key <= 89:
            eighty_89 += value
        elif key >= 90 and key <= 99:
            ninety_99 += value
        elif key >= 100 and key <= 109:
            one100_one109 += value
        elif key >= 110 and key <= 119:
            one110_one119 += value
        elif key >= 120 and key <= 129:
            one120_one129 += value
        elif key >= 130 and key <= 139:
            one30_one39 += value
        elif key >= 140 and key <= 119:
            one40_one59 += value
        elif key >= 150 and key <= 159:
            one50_one59 += value
        elif key >= 160 and key <= 169:
            one60_one69 += value
        elif key >= 170 and key <= 179:
            one70_one79 += value
        elif key >= 180 and key <= 189:
            one80_one89 += value
        elif key >= 190 and key <= 199:
            one90_one99 += value
    divide1, divide2, divide3, divide4, divide5, divide6 = zero_nine//5, ten_19//5, twenty_29//5, thirty_39//5, forty_49//5, fifty_59//5
    divide7, divide8, divide9, divide10, divide11, divide12 = sixty_69 // 5, seventy_79 // 5, eighty_89 // 5, ninety_99 // 5, one100_one109 // 5, one110_one119 // 5
    divide13, divide14, divide15, divide16, divide17, divide18 = one120_one129//5, one30_one39//5, one40_one59//5, one50_one59//5, one60_one69//5, one70_one79//5
    divide19, divide20 = one80_one89//5, one90_one99//5
    print("0-9:",'*'*divide1)
    print("10-19:", '*' * divide2)
    print("20-29:", '*' * divide3)
    print("30-39:", '*' * divide4)
    print("40-49:", '*' * divide5)
    print("50-59:", '*' * divide6)
    print("60-69:", '*' * divide7)
    print("70-79:", '*' * divide8)
    print("80-89:", '*' * divide9)
    print("90-99:", '*' * divide10)
    print("100-109:", '*' * divide11)
    print("110-119:", '*' * divide12)
    print("120-129:", '*' * divide13)
    print("130-139:", '*' * divide14)
    print("140-149:", '*' * divide15)
    print("150-159:", '*' * divide16)
    print("160-169:", '*' * divide17)
    print("170-179:", '*' * divide18)
    print("180-189:", '*' * divide19)
    print("190-199:", '*' * divide20)
