from lab_python_oop.square import square
from lab_python_oop.circle import circle
from lab_python_oop.rect import rect

def main():
    s = square(5.3, 'красный')
    c = circle(2, 'зеленый')
    r = rect(10, 5, 'синий')

    print('Фигуры:\n{}\n{}\n{}'.format(s, c, r))
    

if __name__ == "__main__":
    main()
