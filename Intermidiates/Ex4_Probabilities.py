import random

def main():
    prob = 0.20
    c = random.random()
    if c < prob:
        print('cats')
    else:
        print('dogs')
    print(' ',int(c*100))
main()