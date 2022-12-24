from prod.model.entity import *


class Sorter:

    @staticmethod
    def sort(park):
        if isinstance(park, Parking):
            for i in range(len(park) - 1):
                for index in range(len(park) - 1 - i):
                    if park[index].number > park[index + 1].number:
                        temp = park[index]
                        park[index] = park[index + 1]
                        park[index + 1] = temp


park = Parking(10)
print(park)

park.add(Transport(1, 1, "Bbbbb"))
park.add(Transport(1, 1, "Aaaaa"))
park.add(Transport(1, 1, "Eeeee"))
park.add(Transport(1, 1, "Ddddd"))

print("\nBefore sorting: ")
print(park)

Sorter.sort(park)

print("\nAfter sorting: ")
print(park)