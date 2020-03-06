#  可视化递归算法
#  递归绘制螺旋
'''

插图工具   turtle

'''
import turtle

# myTurtle = turtle.Turtle()#龟龟对象
# myScreen = turtle.Screen()#绘制窗口

# def drawSpiral(myTurtle,lineLen):
#     if lineLen > 0:
#         myTurtle.forward(lineLen)
#         myTurtle.left(90)
#         drawSpiral(myTurtle,lineLen - 5)

# drawSpiral(myTurtle,100)
# myScreen.exitonclick()# 单击推出


#  树形
# def tree(branchLen,t):
#     if branchLen > 5:
#         t.forward(branchLen)
#         t.right(20)
#         tree(branchLen - 15,t)
#         t.left(40)
#         tree(branchLen - 15,t)
#         t.right(20)
#         t.backward(branchLen)


# def main():
#     t = turtle.Turtle()

#     myScreen = turtle.Turtle

#     t.left(90)
#     t.up()
#     t.backward(100)
#     t.down()
#     t.color("red")
#     tree(75,t)
#     myScreen.exitonclick()

# main()


from pythonds.basic.stack import Stack


def moveTower(height,formPole,toPole,withPole):
    if height >= 1:
        moveTower(height - 1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        moveTower(height - 1,withPole,toPole,formPole)


def moveDisk(fp,tp):
    print("移动盘子   从",fp,"到",tp)


fromPole = Stack()
toPole = Stack()
withPole = Stack()

moveTower(5,fromPole,toPole,withPole)