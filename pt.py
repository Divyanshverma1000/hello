BASE=[(1,1),(2,1),(2,2),(1,2)]

def acw_rotate(k):
    p=[]
    for i in range(len(k)):      
        p.append((1*k[i][1],1*k[i][0]))
    return p
    
def shift_in_x(k,n):
    r=[]
    for i in range(len(k)):      
        r.append((1*k[i][0]+1*pow(2,(n-1)),1*k[i][1]))
    return r
def shift_in_xandy(k,n):
    s=[]
    for i in range(len(k)):      
        s.append((1*k[i][0]+1*pow(2,(n-1)),1*k[i][1]+1*pow(2,(n-1))))
    return s
def shift_in_Yand_cw_rotate(k,n):
    m=[]
    for i in range(len(k)): 
        m.append((1*pow(2,n)+1-1*k[i][1]-1*pow(2,(n-1)),1*pow(2,n)+1-1*k[i][0]))
    return m
def Boss(g):
    if g==2:
        return (acw_rotate(BASE)+shift_in_x(BASE,2)+shift_in_xandy(BASE,2)+shift_in_Yand_cw_rotate(BASE,2))
    else:
        return (acw_rotate(Boss(g-1))+shift_in_x(Boss(g-1),n)+shift_in_xandy(Boss(g-1),n)+shift_in_Yand_cw_rotate(Boss(g-1),n))
        
n=int(input("enter n"))
print(Boss(n))
