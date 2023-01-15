class Car:

    def __init__(self) -> None:
        self.front_light = False
        self.back_light = False
        self.light_option = 1
        self.car_status = False
        self.warning_lights = False
        self.speed = 0


    def light_switch(self, car_on):
        if car_on is True:
            self.front_light = True
            return "Front lights are on"
        else:
            self.front_light = False
            return "Front lights are off"





    def light_status(self, x):
        if self.front_light == True:
            if x == 1:
                self.light_option = 1
                return "Hel ljus"
            elif x == 2:
                self.light_option = 2
                return "Halv ljus"


    def backlights(self, car_on):
        if car_on == True:
            self.back_light = True
            return "Backlights are on"
        else:
            self.back_light = False
            return "Backlights are off"

    def warning_light(self, status):
        if status == True:
            self.warning_lights = True
            return "Warning lights on"
        else:
            self.warning_lights = False
            return "Warning lights off"




    def start_car(self):
        self.car_status = True
        self.light_switch(self.car_status)
        self.backlights(self.car_status)
        return "Engine is on"

    def drive(self, more_speed):
        self.car_status == True
        self.speed += more_speed
        if self.speed >= 180:
            self.speed = 180
            return "The max speed is reached"
        else:
            return f'Your current speed is {self.speed}'

 
