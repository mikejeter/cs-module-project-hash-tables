# Your code here


def expensive_seq(x, y, z, mySeq = dict()):
    
    if x <= 0:  
        return y + z

    if (x, y, z) not in mySeq:
        add1 = expensive_seq(x - 1, y + 1, z, mySeq)
        add2 = expensive_seq(x - 2, y + 2, z * 2, mySeq)
        add3 = expensive_seq(x - 3, y + 3, z * 3, mySeq)
        mySeq[(x, y, z)] = add1 + add2 + add3
        return mySeq[(x, y, z)]
    else:
        return mySeq[(x, y, z)]



if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
