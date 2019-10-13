import sys
import os

def modify_the_line(filename):
    file = open(filename, "r")
    line = file.read()
    repeating_occurs = True
    while repeating_occurs:
        repeating_occurs = False
        if len(line) == 0 or len(line) == 1:
            pass
        else:
            buffer = open("buffer.txt", "w")
            n = len(line) - 1
            repeats = False
            for i in range(n):
                if line[i] == line[i+1]:
                    repeats = not repeats
                    repeating_occurs = True
                else:
                    if not repeats:
                        buffer.write(line[i])
                    repeats = False
            # Last element
            if line[n] != line[n-1] or not repeats:
                buffer.write(line[n])
            else:
                repeating_occurs = True
            buffer.close()
            buffer = open("buffer.txt", "r")
            line = buffer.read()
            buffer.close()
    print(line)
    try:
        os.remove("buffer.txt")
    except FileNotFoundError:
        pass


if __name__=="__main__":
    filename = sys.argv[1]
    modify_the_line(filename)