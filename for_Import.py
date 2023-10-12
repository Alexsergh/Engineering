def summ(x, *args):
    one = x ** 2
    two = sum(args) / len(args)
    three = max(args)
    print(f"one={one}\ntwo={two}\nthree={three}")

    return one * two * three
