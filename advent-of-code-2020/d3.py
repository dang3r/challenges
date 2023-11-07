
maze = [line.strip() for line in open("d3.in").readlines()]

vecs = [(1,1), (3,1), (5,1), (7,1), (1,2)]
trees_product = 1
width = len(maze[0])
height = len(maze)
for vec in vecs:
    trees = 0
    x,y = 0,0
    while y < height -1:
        x, y = (x+vec[0]) % width, y+vec[1]
        print(x,y)
        print(maze[y][x])
        trees += int(maze[y][x] == "#")
    trees_product *= trees
print(trees_product)