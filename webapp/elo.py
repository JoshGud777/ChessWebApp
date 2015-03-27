'''
Coustom made Elo moduel for the chess web app
(c) 2015 Joshua Gudmundson
'''


def estimate(Ra, Rb):
    '''Returns for any two player rantings the % they will win'''
    Ea = 1 / (1 + 10 ** ((Rb - Ra) / 400))
    Eb = 1 / (1 + 10 ** ((Ra - Rb) / 400))
    return round(Ea, 2), round(Eb, 2)


def rate(Ra, Rb, Sa, K=20):
    '''Returns new rantings for given ranks and Scor for A'''
    Ea, Eb = estimate(Ra, Rb)
    Sb = 1 - Sa
    nRa = Ra + K * (Sa - Ea)
    nRb = Rb + K * (Sb - Eb)
    return round(nRa, 1), round(nRb, 1)


def main():
    '''Used only to test this code'''
    print(str(estimate(1100, 1000)[0]*100) + '% is ', end='')
    print(str(type(estimate(1100, 1000)[0])))
    print(str(estimate(1100, 1000)[1]*100) + '% is ', end='')
    print(str(type(estimate(1100, 1000)[1])))

    print(str(rate(1100, 1000, 1, 40)[0]) + ' is ', end='')
    print(str(type(rate(1100, 1000, 1, 40)[0])))
    print(str(rate(1100, 1000, 1, 40)[1]) + ' is ', end='')
    print(str(type(rate(1100, 1000, 1, 40)[1])))


if __name__ == '__main__':
    main()
