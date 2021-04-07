'''
@Author: rishi
'''


class Car:
    def __init__(self):
        self.brake = "car has brake"
        self.wheel = "car has wheeel"


class Renault(Car):
    def __init__(self):
        super(Renault, self).__init__()
        self.steering = "power steering"


class Honda(Car):
    def __init__(self):
        super(Honda, self).__init__()
        self.wheel = "alloy wheel"
        self.steering = "no power steering"


obj1 = Honda()
print(obj1.brake, "\n", obj1.wheel, "\n", obj1.steering)
