from graphics import *
win = GraphWin('chess', 450, 450)

nodes = []
s = 50
p = 50 
c = 0
for x in range(8):
    for y in range(8):
        nodes.append((x, y))
        rect = Rectangle(Point(x * s - s/2 + p, y * s - s/2 + p), Point(p + x * s + s / 2, p + y * s + s/2))
        if (x + y) % 2 == 1:
            rect.setFill("darkgrey")
        else:
            rect.setFill("lightgrey")
        rect.setOutline(color_rgb(200,200,200))
        rect.draw(win)
        point = Circle(Point(p + x * s, p + y * s), 5)
        point.setFill("black")
        point.draw(win)

directions = [(2,1), (1,2), (-1,-2), (-2,-1), (-1, 2), (-2,1), (1, -2), (2, -1)]

for (px, py) in nodes:
    for (dx, dy) in directions:
        if dx + px >= 0 and dx + px < 8 and dy + py >= 0 and dy + py < 8:
            line = Line(Point(p + (px + dx) * s, p + (py + dy) * s), 
                        Point(p + px * s , p + py * s))
            line.draw(win)
            c += 1
print("c:", c/2)
while True:
    pass
