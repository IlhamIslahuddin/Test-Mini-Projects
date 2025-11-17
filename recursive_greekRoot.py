def greekRoot(x):
    return guess(x,1)

def guess(x,g):
    if g**2 == x:
        return g
    else:
        return guess(x,(g+x/g)/2)

if __name__ == "__main__":
  greekRoot(64)
