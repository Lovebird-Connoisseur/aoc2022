def Calorie_Counting():

    total_calories = 0
    item = 0
    carried_calories = []
    top_3_most_calories = 0    

    with open("day1_input.txt") as input:
        for item in input:
            if item == "\n":
                carried_calories.append(total_calories)
                total_calories = 0
                item = 0
            total_calories += int(item)

    for i in range(3):
        print(max(carried_calories))
        top_3_most_calories += carried_calories.pop(carried_calories.index(max(carried_calories)))
    print(top_3_most_calories)

Calorie_Counting()
