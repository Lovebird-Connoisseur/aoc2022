def rock_paper_scissors():

    total_points = 0
    points = {"A": 1,
            "B": 2,
            "C": 3
            }

    with open('day2_input.txt') as matches:
        for round in matches:
            play = round.split()

            if play[1] == "X":
                if play[0] == "A":
                    total_points += 3
                if play[0] == "B":
                    total_points += 1
                if play[0] == "C":
                    total_points += 2
            if play[1] == "Y":
                total_points += 3 + points[play[0]]
            if play[1] == "Z":
                total_points += 6
                if play[0] == "A":
                    total_points += 2
                if play[0] == "B":
                    total_points += 3
                if play[0] == "C":
                    total_points += 1

        print(total_points)

rock_paper_scissors()
