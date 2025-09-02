lane =[]
for i in range(4):
    lights = list(map(int,input().split()))
    lane.append(lights)



# accident = False
# while True:
#     if lane[0][0]== 1 and lane[3][3] == 1:
#         print("Yes")
#         accident = True
#         break
#     if lane[0][3] == 1 and lane[1][1] == 1:
#         print("Yes")
#         accident = True
#         break
#     if lane[1][3] == 1 and lane[2][0] == 1:
#         print("Yes")
#         accident = True
#         break
#     if lane[2][3] == 1 and lane[3][0] == 1:
#         print("Yes")
#         accident = True
#         break
#     if lane[0][2] == 1 and lane[0][3] == 1:
#         print("Yes")
#         accident = True
#         break
#     if lane[1][2] == 1 and lane[1][3] == 1:
#         print("Yes")
#         accident = True
#         break
#     if lane[2][2] == 1 and lane[2][3] == 1:
#         print("Yes")
#         accident = True
#         break
#     if lane[3][2] == 1 and lane[3][3] == 1:
#         print("Yes")
#         accident = True
#         break
#     if lane[0][1] == 1 and lane[3][3] == 1:
#         print("Yes")
#         accident = True
#         break
#     if lane[0][3] == 1 and lane[1][1] == 1:
#         print("Yes")
#         accident = True
#         break
#     if lane[1][3] == 1 and lane[2][1] == 1:
#         print("Yes")
#         accident = True
#         break
#     if lane[2][3] == 1 and lane[3][1] == 1:
#         print("Yes")
#         accident = True
#         break
#     if lane[0][0] == 1 and lane[2][3] == 1:
#         print("Yes")
#         accident = True
#         break
#     if lane[1][0] == 1 and lane[3][3] == 1:
#         print("Yes")
#         accident = True
#         break
#     if lane[2][0] == 1 and lane[0][3] == 1:
#         print("Yes")
#         accident = True
#         break
#     if lane[3][0] == 1 and lane[1][3] == 1:
#         print("Yes")
#         accident = True
#         break
#     else:
#         print("No")
#         break
        