def Camp_cleanup():

    fully_contains = 0
    overlaps = 0

    with open('day4_input.txt') as assignments:
        for assignment in assignments:
            assignment = assignment[:-1]
            assignment = assignment.split(",")
            schd1 = list(map(int, assignment[0].split("-")))
            schd2 = list(map(int, assignment[1].split("-")))

            if schd1[0] == schd2[0] and schd1[1] == schd2[1]:
                fully_contains += 1
            elif schd1[0] <= schd2[0] and schd1[1] >= schd2[1]:
                fully_contains += 1
            elif schd2[0] <= schd1[0] and schd2[1] >= schd1[1]:
                fully_contains += 1

            for i in range(schd1[0], schd1[1] + 1):
                if schd2[0] <= i <= schd2[1]:
                    overlaps += 1
                    break

        print(fully_contains)
        print(overlaps)

Camp_cleanup()
