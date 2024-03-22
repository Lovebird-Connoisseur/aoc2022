def Rock_Paper_Scissors():

    total_score = 0

    with open('day2_input.txt') as input:
        for item in input:
            play = item.split()
            print(play)
            if play[0] == "A":
                if play[1] == "X":
                    total_score += 3+1
                if play[1] == "Y":
                    total_score += 6+2
                if play[1] == "Z":
                    total_score += 0+3
            elif play[0] == "B":
                if play[1] == "X":
                    total_score += 0+1
                if play[1] == "Y":
                    total_score += 3+2
                if play[1] == "Z":
                    total_score += 6+3
            elif play[0] == "C":
                if play[1] == "X":
                    total_score += 6+1
                if play[1] == "Y":
                    total_score += 0+2
                if play[1] == "Z":
                    total_score += 3+3
        print(total_score)

Rock_Paper_Scissors()
