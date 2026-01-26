class Buffer:
    def __init__(self):
        self.list = []

    def add(self, *a):
        for arg in a:
            self.list.append(arg)
        return self.list

    def get_current_part(self):
        sum_of_first_five = 0
        if len(self.list)  >=  5:
            for i in range(5):
                sum_of_first_five += self.list[i]
            for i in range(5):
                self.list.pop(0)
        return sum_of_first_five

if __name__ == "__main__":
    buf = Buffer()
    print(buf.add(5,5,6))
    print(buf.get_current_part())
    print(buf.add(1,11,5,8,6,4))
    print(buf.get_current_part())
    print(buf.add(1,2))
    print(buf.get_current_part())
    print(buf.add(1,2,3,4))
    print(buf.get_current_part())
    print(buf.add(15,24,45,89))
    print(buf.get_current_part())