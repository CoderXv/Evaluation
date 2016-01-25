__author__ = 'user'
import math

class Point:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        self.r = 0.0
        self.e = 0.0

    def set_reference_point(self, x, y, z, r, e):
        self.x = x
        self.y = y
        self.z = z
        self.r = r
        self.e = e

    def set_centerline_point(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_z(self, z):
        self.z = z

    def set_r(self, r):
        self.r = r

    def set_e(self, e):
        self.e = e

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_z(self):
        return self.z

    def get_r(self):
        return self.r

    def get_e(self):
        return self.e

    # p is a point
    def add(self, p):
        self.x += p.get_x()
        self.y += p.get_y()
        self.z += p.get_z()

    def subtract(self, p):
        self.x -= p.get_x()
        self.y -= p.get_y()
        self.z -= p.get_z()

    def multiply(self, p):
        self.x *= p.get_x()
        self.y *= p.get_y()
        self.z *= p.get_z()

    def division(self, p):
        self.x /= p.get_x()
        self.y /= p.get_y()
        self.z /= p.get_z()

    def multiply_fig(self, a):
        self.x *= a
        self.y *= a
        self.z *= a

    def dot(self, p):
        self.x *= p.get_x()
        self.y *= p.get_y()
        self.z *= p.get_z()
        return self.x + self.y + self.z

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

