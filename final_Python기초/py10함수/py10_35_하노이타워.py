# 하노이의 탑(Tower of Hanoi)는 세 개의 기둥과 이 기둥에 꽂을 수 있는
# 크기가 다양한 원판들이 순서대로 쌓여 있다.아래의 두 가지 조건을
# 만족시키면서, 한 기둥에 꽂힌 원판들을 그 순서 그대로 다른 기둥으로 옮겨서
# 다시 쌓는 것이다.

# 1. 한 번에 하나의 원판만 옮길 수 있다.
# 2. 큰 원판이 작은 원판 위에 있어서는 안 된다.


def hanoi(disc, src, aux, dst):
    if(disc > 0):
        hanoi(disc-1, src, dst, aux)
        print('Move disc %s from %s to %s' % (disc, src, dst))
        hanoi(disc-1, aux, src, dst)


hanoi(3, 'src', 'aux', 'dst')
