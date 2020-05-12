# 중첩 for문
for i in range( 2, 10, 1):
    for j in range( 1, 10, 1):
        msg = "%s*%s=%3s, " % ( i, j, i*j )
        print( msg, end="\n")
    print()