def Rucksack_reorganization():
    import string

    shared_items = []
    step = 0
    badge_sum = 0
    total_items, total_badges = 0, 0
    rucksack1, rucksack2, rucksack3 = 0, 0, 0
    possible_badges = []

    def item_sums(shared_items):
        priority_sum = 0
        for item in shared_items:
            for i, p in enumerate(string.ascii_lowercase[:26], start = 1):
                if item == p:
                    priority_sum += i
            for i, p in enumerate(string.ascii_uppercase[:26], start = 27):
                if item == p:
                    priority_sum += i
        return priority_sum

    with open('day3_input.txt') as list_of_items:
        for i in list_of_items:
            compartment_1 = i[:len(i)//2]
            compartment_2 = i[len(i)//2:]
            shared_items = []

            for p in compartment_1:
                if p in compartment_2 and p not in shared_items:
                    shared_items.append(p)

            total_items += item_sums(shared_items)

            step += 1
            rucksack3 = rucksack2
            rucksack2 = rucksack1
            rucksack1 = i
            
            if step >= 3 and step % 3 == 0:
                for x in rucksack1:
                    if x in rucksack2 and x in rucksack3 and x not in possible_badges:
                        possible_badges.append(x)
                total_badges += item_sums(possible_badges)
                possible_badges = []


        print(total_items)
        print(total_badges)

Rucksack_reorganization()
