N, T = map(int, input().split())
food_list = []
for n in range(N):
    A, B = map(int, input().split())
    food_list.append((A, B, B / A))
food_list.sort(key=lambda x: x[2], reverse=True)

is_eating = False
satisfy = 0

for t in range(T + 1):
    if is_eating == True:
        if t == eating_end_time:
            is_eating = False
    if is_eating == False:
        for food in food_list:
            if food[0] + t <= T:
                is_eating = True
                eating_end_time = food[0]+t
                satisfy += food[1]
                food_list.remove(food)
                print(food)
    print(satisfy)

print(satisfy)
