# https://atcoder.jp/contests/abc244/tasks/abc244_b

n = int(input())
t_list = list(input())
d_list = ["east", "south", "west", "north"]
d_i = 0
x, y = 0, 0
for t in t_list:
    if t == "S":
        d = d_list[d_i]
        if d == "east":
            x +=1
        elif d == "south":
            y -=1
        elif d == "west":
            x -=1
        else:
            y +=1
    else:
        d_i = (d_i+1) % 4

print(x,y)
