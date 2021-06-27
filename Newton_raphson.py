def smart_div(func):
    def inner(a, b):
        if 0 == b:
            print(" Exception Caught, Zero Division Error: The denominator is zero")
            return
        return func(a, b)
    return inner


@smart_div
def div(a, b):
    return a / b


def newt_raph(fx,
              dfx,
              x=1,
              iterations=100,
              tolerance=1E-8):
    """ This newton_raphson basic solver takes a function and its derivative
    with maximum number of iterations and the tolerance it returns if it finds
    solution with in the iterations count"""
    for i in range(iterations):
        xstar = x - div(fx(x), dfx(x))
        if abs(xstar - x) <= tolerance:
            break
        x = xstar
    return xstar


if __name__ == "__main__":
    y = lambda xi: (xi ** 2.0) + 4.0
    dy = lambda xi: 2.0 * xi
    print(f'The root of the function is {newt_raph(y, dy, 0)}')
