from bil import Car
test = Car()

def test_light_switch():
    assert test.light_switch(True) =='Front lights are on'

def test_light_status():
    test.light_status(True)
    assert test.light_status(1)=='Hel ljus'
    assert test.light_status(2)=='Halv ljus'

def test_backlights():
    assert test.backlights(True)=='Backlights are on'
    assert test.backlights(False)=='Backlights are off'

def test_warning_light():
    assert test.warning_light(True)=='Warning lights on'
    assert test.warning_light(False)=='Warning lights off'

def test_start_car():
    
    assert test.start_car() == "Engine is on"
    assert test.front_light == True
    assert test.back_light == True


def test_drive():
   assert test.drive(45)=='Your current speed is 45'
   assert test.drive(180)=='The max speed is reached'