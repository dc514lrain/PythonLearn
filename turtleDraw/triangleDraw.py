import turtle

# 最小循环工作：逆时针画一个等边三角形，只需要传入海龟实例和边长变量
def draw_triangle(t, length):
    for _ in range(3):
        t.forward(length)
        t.left(120)

# 递归主函数
def draw_nested_triangles(t, length, depth, start_points):    #(海龟实例，边长，深度，起点列表)
    if depth == 0:  #深度判断，这里是递归的退出锁，不设置好会无限循环爆炸
        return

    new_points = []
    for (x, y) in start_points:
        
        # 找点+画三角，这部分是实际工作
        t.penup()
        t.goto(x, y)
        t.pendown()
        #for _ in range(3):
        new_points.append(t.pos())
        t.left(120)
        t.forward(length/2)
        new_points.append(t.pos())
        t.forward(length/2)
        t.left(120)
        t.forward(length)
        t.left(120)
        t.forward(length/2)
        new_points.append(t.pos())
        t.forward(length/2)
        # 这部分是处理每次新增的起点
        # new_points.append((x + length / 2, y))
        # new_points.append((x + length / 4, y - (length * (3**0.5)) / 4))

    # 递归调用自身
    draw_nested_triangles(t, length / 2, depth - 1, new_points)


def main():
    
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)  #可以自己设置速度

    start_points = [(0, 0)]    # 初始起点 这是一个全局变量，这种实现方法不是很优雅

    draw_nested_triangles(t, 200, 5, start_points)
    turtle.done()
    
if __name__ == "__main__":
    main()
