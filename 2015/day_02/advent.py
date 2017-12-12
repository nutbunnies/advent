class Box(object):
    def __init__(self, l, w, h):
        self.l = l
        self.w = w
        self.h = h

    def surface_area(self):
        return 2*self.l*self.w + 2*self.w*self.h + 2*self.h*self.l

    def smallest_side_area(self):
        return min([self.l*self.w, self.w*self.h, self.h*self.l])

    def ribbon_needed(self):
        smallest = sorted([self.l, self.w, self.h])[:2]
        ribbon_needed = smallest[0] + smallest[0] + smallest[1] + smallest[1]
        ribbon_needed += self.l * self.w * self.h
        return ribbon_needed

    def total_paper_needed(self):
        return self.surface_area() + self.smallest_side_area()

total_paper_needed = 0
total_ribbon_needed = 0
with open('input.txt', 'r') as data:
    for present in data.read().strip().split("\n"):
        box = Box(*list(map(int, present.split("x"))))
        total_paper_needed += box.total_paper_needed()
        total_ribbon_needed += box.ribbon_needed()

print("total paper needed: ", total_paper_needed)
print("total ribbon needed: ", total_ribbon_needed)