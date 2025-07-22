from demo import func1


def world_1():
    print("Name", __name__)
    func1()
    print("world 1")


def world_2():
    print("world 2")


world_1()