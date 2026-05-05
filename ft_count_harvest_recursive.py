def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def count(current, days):
        if current > days:
            print("Harvest time!")
            return
        print("Day " + str(current))
        count(current + 1, days)

    count(1, days)
