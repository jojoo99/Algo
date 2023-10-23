N = int(input())
card_lst = set(map(int, input().split()))
# print(card_lst)
M = int(input())
new_lst = list(map(int, input().split()))
# print(new_lst)

for i in new_lst:
    if i in card_lst:
        print(1, end=' ')
    else:
        print(0, end=' ')