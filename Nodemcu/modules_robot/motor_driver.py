import machine

class MotorDriver:
    def __init__(self, motor_a_pwm:int, motor_a_dir:int, motor_b_pwm:int, motor_b_dir:int):
        self.motor_a_pwm = machine.PWM(machine.Pin(motor_a_pwm, machine.Pin.OUT))
        self.motor_a_dir = machine.Pin(motor_a_dir, machine.Pin.OUT)
        self.motor_a_pwm.freq(50)
        
        self.motor_b_pwm = machine.PWM(machine.Pin(motor_b_pwm, machine.Pin.OUT))
        self.motor_b_dir = machine.Pin(motor_b_dir, machine.Pin.OUT)
        self.motor_b_pwm.freq(50)

    def backwards(self):
        self.motor_a_pwm.duty(255)
        self.motor_a_dir.on()
        self.motor_b_pwm.duty(255)
        self.motor_b_dir.on()
        
    def forward(self):
        self.motor_a_pwm.duty(255)
        self.motor_a_dir.off()
        self.motor_b_pwm.duty(255)
        self.motor_b_dir.off()
        
    def left(self):
        self.motor_a_pwm.duty(255)
        self.motor_a_dir.off()
        self.motor_b_pwm.duty(0)
        self.motor_b_dir.off()
    
    def right(self):
        self.motor_a_pwm.duty(0)
        self.motor_a_dir.off()
        self.motor_b_pwm.duty(255)
        self.motor_b_dir.off()
        
    def stop(self):
        self.motor_a_pwm.duty(0)
        self.motor_b_pwm.duty(0)
        
