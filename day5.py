def Supply_stacks():

    y = 0
    layout = []

    with open('day5_input.txt') as stack:
        for line in stack:
            if any(char.isupper() for char in line):
                y += 1

Supply_stacks()
