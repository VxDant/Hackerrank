import math

#Find angle MBC
ab = int(input())
bc = int(input())

angle_mbc = math.atan(ab/bc)

angle_mbc = math.degrees(angle_mbc)

print(str(round(angle_mbc)) + chr(176))
