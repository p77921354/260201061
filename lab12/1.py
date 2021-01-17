class Cylinder:
    def __init__(self,radius,height):
        self.radius = radius
        self.height = height
    def get_radius(self):
        return self.radius
    def get_height(self):
        return self.height
    def set_radius(self,radius):
        if radius > 0:
          self.radius = radius
    def set_height(self,height):
        if height > 0:
           self.height = height
    def calc_base_area(self):
        return 3.14*self.radius**2
    def calc_surf_area(self):
        return self.height*self.radius
    def calc_area(self):
        return 2*(self.calc_base_area())+self.calc_surf_area()
    def calc_volume(self):
        return self.height*self.calc_base_area()
cylinder1 = Cylinder(3,5)
cylinder1.set_height(7)
print(cylinder1.calc_area())
print(cylinder1.calc_volume())