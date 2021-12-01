import math
from matplotlib import pyplot as plt
MODEL_G = 9.81
MODEL_DT = 0.001

class Body:
    def __init__(self, x, y, vx, vy):

        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

        self.trajectory_x = []
        self.trajectory_y = []

    def advance(self):

        self.trajectory_x.append(self.x)
        self.trajectory_y.append(self.y)


        self.x += self.vx * MODEL_DT
        self.y += self.vy * MODEL_DT
        self.vy -= MODEL_G * MODEL_DT

obj = Body(0, 0, 487.9, 487.9)
while obj.y >= 0:
    obj.advance()

plt.plot(obj.trajectory_x, obj.trajectory_y)
plt.grid()
plt.title('Полёт снаряда гаубицы Д-30 при отсутствии сопротивления под углом в 45 град.')
plt.xlabel('Горизонтальная координата, м')
plt.ylabel('Вертикальная координата, м')

plt.show()
