import sys
import math

def get_coefficient(index: int, promt: str) -> float:
    try:
        coef = float(sys.argv[index])
    except:
        print(promt)
        coef = float(input())
    return coef

def solve_biquadratic(a: float, b: float, c: float) -> list[float]:
    ret = list()
    d_inner = b**2 - 4*a*c

    def check_d(d: float, ret: list[float]):
        if d < 0:
            return

        if d == 0:
            ret.append(0)
        else:
            ret.append(math.sqrt(d))
            ret.append(-math.sqrt(d))

    if d_inner < 0:
        return ret

    if d_inner == 0:
        check_d(-b / (2.0 * a), ret)
        return ret

    else:
        check_d((-b + math.sqrt(d_inner)) / (2.0 * a), ret)
        check_d((-b - math.sqrt(d_inner)) / (2.0 * a), ret)
        return ret

def main():
    a = get_coefficient(1, 'Введите параметр A')
    b = get_coefficient(2, 'Введите параметр B')
    c = get_coefficient(3, 'Введите параметр C')

    print("Уравнение {}x^4 + {}x^2 + {} = 0".format(a, b, c))

    results = solve_biquadratic(a, b, c)
    if len(results) == 0:
        print("Данное уравнение не имеет корней")
    else:
        print("Корни уравнения: {}".format(results))

if __name__ == "__main__":
    main()