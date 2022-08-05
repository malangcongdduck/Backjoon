import sys
# [left, right] 합구간
# [start, end] 각 노드가 가진 수 구간
# diff = val - li[index] -> 차이를 더해줘서 값을 업데이트


def init(node, start, end):
    if start == end:  # leef node
        tree[node] = li[start]
        return tree[node]
    else:
        tree[node] = init(node*2, start, (start+end)//2) + \
            init(node*2+1, (start+end)//2+1, end)
        return tree[node]


def sum_node(node, start, end, left, right):
    if left > end or right < start:  # 넘어가는 경우
        return 0

    # 구해야 하는 합의 범위에 있는 수
    if left <= start and end <= right:
        return tree[node]

    return sum_node(node*2, start, (start+end)//2, left, right) + sum_node(node*2+1, (start+end)//2+1, end, left, right)


def update_node(node, start, end, index, diff):
    if index < start or index > end:
        return

    tree[node] += diff  # 차이를 더해줘서 값을 업데이트

    if start != end:  # 리프노드가 아닌 경우 자식 값 변경
        update_node(node*2, start, (start+end)//2, index, diff)  # 왼쪽 자식 update
        update_node(node*2+1, (start+end)//2+1, end,
                    index, diff)  # 오른쪽 자식 update


n, m, k = map(int, sys.stdin.readline().rstrip().split())
li = [int(sys.stdin.readline()) for _ in range(n)]
tree = [0] * 10000000

init(1, 0, n-1)

for _ in range(m+k):
    a, b, c = map(int, sys.stdin.readline().split())

    if a == 1:
        diff = c - li[b-1]
        li[b-1] = c
        update_node(1, 0, n-1, b-1, diff)
    else:
        print(sum_node(1, 0, n-1, b-1, c-1))
