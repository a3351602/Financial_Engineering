def BOP_call(S,X,r,u,d):
    print("caculate call price")
    import math
    R = math.exp(r/100)
    p = (R-d)/(u-d)
    C = [[],[],[],[]]

    for j in range(4):
        s = S*(u**(3-j))*(d**j)
        C[3].append(max(s-X,0))

    i = 2
    while i >= 0:
        for j in range(i+1):
            payoff = (p*C[i+1][j]+(1-p)*C[i+1][j+1])/R
            C[i].append(payoff)
        i -= 1

    for i in range(3):
        for j in range(i+1):
            print('C[%d][%d]:%.2f' %(i,j,C[i][j]),end=" ")
        print('\n')

def BOP_put(S,X,r,u,d):
    print("caculate put price")
    import math
    R = math.exp(r/100)
    p = (R-d)/(u-d)
    C = [[],[],[],[]]

    for j in range(4):
        s = S*(u**(3-j))*(d**j)
        C[3].append(max(X-s,0))

    i = 2
    while i >= 0:
        for j in range(i+1):
            payoff = (p*C[i+1][j]+(1-p)*C[i+1][j+1])/R
            C[i].append(payoff)
        i -= 1

    for i in range(3):
        for j in range(i+1):
            print('C[%d][%d]:%.2f' %(i,j,C[i][j]),end=" ")
        print('\n')

S = int(input("Enter stock price:"))
X = int(input("Enter strike price:"))
r = int(input("Enter rate(%):"))
u = float(input("Enter u:"))
d = float(input("Enter d:"))
BOP_call(S,X,r,u,d)
BOP_put(S,X,r,u,d)
