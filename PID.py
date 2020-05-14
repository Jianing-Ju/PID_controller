import time

class PID:

    def __init__(self, Kp, Ki, Kd, origin_time=None):
        if origin_time is None:
            origin_time = time.time()

        # Gains for each term
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd

        # Corrections (outputs)
        self.Cp = 0.0
        self.Ci = 0.0
        self.Cd = 0.0

        self.previous_time = origin_time
        self.previous_error = 0.0
        self.target = 0.0
        self.output = 0.0
        self.sample_time = 0.0

    def update(self, feedback, current_time=None):
        
        if current_time is None:
            current_time = time.time()
        dt = current_time - self.previous_time
        if dt <= 0.0:
            return 0
        
        error = self.target - feedback
        de = error - self.previous_error
        
        if (dt >= self.sample_time):
            self.Cp = error
            self.Ci += error * dt
            self.Cd = de / dt

        self.previous_time = current_time
        self.previous_error = error

        self.output =(self.Kp * self.Cp) + (self.Ki * self.Ci) + (self.Kd * self.Cd) 

    def setKp(self, proportional_gain):
        self.Kp = proportional_gain

    def setKi(self, integral_gain):
        self.Ki = integral_gain

    def setKd(self, derivative_gain):
        self.Kd = derivative_gain

    def setSampleTime(self, sample_time):
        self.sample_time = sample_time
