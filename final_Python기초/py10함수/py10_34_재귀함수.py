
# 재귀 함수 예제1

def factorial(i, a=1):

    if(i < 2):
        return a

    return factorial(i-1, a*i)

print(factorial(4))  # 24
print(factorial(4, 2))  # 48

# 재귀 함수 예제2


def hanoi(disc, src, aux, dst):
    if(disc > 0):
        hanoi(disc-1, src, dst, aux)
        print('Move disc %s from %s to %s' % (disc, src, dst))
        hanoi(disc-1, aux, src, dst)

hanoi(3, 'src', 'aux', 'dst')
