'''
A simple program used to spit out random secuances of hex with db as the first
two letters and as the last to. takes a bit of time to prosess
'''
import binascii
import os
import cgitb
cgitb.enable()


def main():
    '''Main Looping part'''
    print("Content-type: text/plain\n")
    loopnum = 0
    while loopnum < 50:
        data = binascii.hexlify(os.urandom(16)).decode('utf8')
        if data[0] == 'd' and data[1] == 'b' and data[-2] == 'd' \
           and data[-1] == 'b':

            if loopnum < 9:
                collon = '  : '
            else:
                collon = ' : '

            print(str(loopnum+1) + collon + data)
            loopnum += 1

if __name__ == '__main__':
    main()
