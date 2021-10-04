from lab_python_fp.field import field
from lab_python_fp.gen_random import gen_random

def main():
    goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'color': 'black'}
]
    # for i in field(goods, 'title', 'color', 'dad'):
    #     print(i)

    for i in gen_random(10, 1, 10):
        print(i)

if __name__ == '__main__':
    main()