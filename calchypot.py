import math
points = [(6, 8), (3, 4)]
x1 = points[0][0]
y1 = points[0][1]
x2 = points[1][0]
y2 = points[1][1]
distances=[x2-x1,y2-y1]
def euclideanDistance():
    return math.sqrt(distances[0]**2+distances[1]**2)

print(distances)
print(euclideanDistance())