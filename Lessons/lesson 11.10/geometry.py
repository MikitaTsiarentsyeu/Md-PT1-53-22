class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    x = property(get_x, set_x)
    y = property(get_y, set_y)

    def __str__(self):
        return f"x: {self.x}, y: {self.y}"

p1 = Point(2, 4)
p2 = Point(-3, 8)

print(p1)
print(p2)


class Segment:

    def __init__(self, point_a, point_b):
        self.point_a = point_a
        self.point_b = point_b

    def get_point_a(self):
        return self.__point_a

    def get_point_b(self):
        return self.__point_b

    def set_point_a(self, point_a):
        self.__point_a = point_a

    def set_point_b(self, point_b):
        self.__point_b = point_b

    point_a = property(get_point_a, set_point_a)
    point_b = property(get_point_b, set_point_b)

    def __str__(self):
        return f"A - {self.point_a}; B - {self.point_b}"

s = Segment(p1, p2)
print(s)

class Vector:

    def __init__(self, segment, start_from_a=True):
        self.segment = segment
        if start_from_a:
            self.start = segment.point_a
            self.end = segment.point_b
        else:
            self.start = segment.point_b
            self.end = segment.point_a

    def get_start(self):
        return self.__start

    def get_end(self):
        return self.__end

    def set_start(self, start):
        self.__start = start

    def set_end(self, end):
        self.__end = end

    start = property(get_start, set_start)
    end = property(get_end, set_end)

    def __str__(self):
        return f"start - {self.start}; end - {self.end}"

v = Vector(s, False)
print(v)