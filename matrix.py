# 🚨 Don't change the code below 👇
row1 = ["a1","a2","a3"]
row2 = ["b1","b2","b3"]
row3 = ["c1","c2","c3"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
    # 🚨 Don't change the code above 👆

    #Write your code below this row 👇
sli = int(position[0])
el = int(position[1])

map[el-1][sli-1] = "X"
print(f"{row1}\n{row2}\n{row3}\n")
map[1][1] = "b12"

map[0][2]="Z"
print(map)

print(f"{row1}\n{row2}\n{row3}")
