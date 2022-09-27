class Simpleton:

    test_attr = "the global value for the class"

    def print_test_attr(self):
        print(self.test_attr)

s = Simpleton()
print(s.test_attr)

s1 = Simpleton()
print(s1.test_attr)

s1.test_attr = "new value"

print(s.test_attr)
print(s1.test_attr)

s.print_test_attr()
# print(Simpleton, type(Simpleton))
# print(s, type(s))

