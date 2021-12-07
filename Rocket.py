import math
import numpy as np
from matplotlib import pyplot as pp

MODEL_G = 9.81
MODEL_DT = 0.001
M = 0.5

class Body:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

        self.trajectory_x = []
        self.trajectory_y = []

    def advance(self):
        while (self.y >= 0):
            self.trajectory_x.append(self.x)
            self.trajectory_y.append(self.y)
            self.x += self.vx * MODEL_DT
            self.y += self.vy * MODEL_DT
            self.vy -= MODEL_G * MODEL_DT


class Rocket(Body):
    def __init__(self, x, y, weight_fuel, weight_rocket, v_fuel, ang):

        self.weight_rocket = weight_rocket
        self.weight_fuel = weight_fuel
        self.v_fuel = v_fuel
        self.ang = ang
        self.weight = self.weight_fuel + self.weight_rocket

        super().__init__(x, y, 0, 0)

    def advance(self):
        t = 0
        fuel = self.weight_fuel
        while t * M <= fuel:
            self.trajectory_x.append(self.x)
            self.trajectory_y.append(self.y)

            self.vx = math.log(self.weight/(self.weight - M*t)) * self.v_fuel * math.cos(self.ang)
            self.vy = math.log(self.weight/(self.weight - M*t)) * self.v_fuel * math.sin(self.ang)

            self.weight = (self.weight_fuel + self.weight_rocket) / 2.71**(self.vx/(self.v_fuel*math.sin(ang)))
            t += MODEL_DT

        while (self.y >= 0):
            self.trajectory_x.append(self.x)
            self.trajectory_y.append(self.y)
            self.x += self.vx * MODEL_DT
            self.y += self.vy * MODEL_DT
            self.vy -= MODEL_G * MODEL_DT

weight_rocket = 37.4
weight_fuel = 4.6
ang = 3.14/4
r = Rocket(0, 0, weight_fuel, weight_rocket, 2000, ang)
r.advance()
pp.plot(r.trajectory_x, r.trajectory_y)
pp.grid()
pp.title('Траектория реактивного снаряда М-13 без учета сил сопротивления по углом в 45 град. ')
pp.xlabel('Горизонтальная координата, м')
pp.ylabel('Вертикальная координата, м')
pp.show()