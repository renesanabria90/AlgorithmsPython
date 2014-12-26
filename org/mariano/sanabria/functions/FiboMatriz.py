#Modulo FiboMatriz
def mul(A, B):
    a, b, c = A
    d, e, f = B
    return a*d + b*e, a*e + b*f, b*e + c*f

def pow(A, n):
    if n == 1:     return A
    if n & 1 == 0: return pow(mul(A, A), n//2)
    else:          return mul(A, pow(mul(A, A), (n-1)//2))

def fibMat(n):
    if n < 0: 
	    print "La posicion debe de ser mayor a cero"
	    main()
    if n < 2: 
	    return n
    return pow((1,1,0), n-1)[0]
