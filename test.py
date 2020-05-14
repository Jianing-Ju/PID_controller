import PID
import time
import matplotlib.pyplot as plt
import numpy as np

def test(P = 0.2,  I = 0.0, D= 0.0, L=5, t = 0.01):
    pid = PID.PID(P, I, D)

    pid.target=0.0
    pid.setSampleTime(t)

    end_sample_time = int(L/t)
    feedback = 0

    feedback_list = []
    time_list = []
    target_list = []

    for i in range(1, end_sample_time):
        pid.update(feedback)
        output = pid.output
        if pid.target > 0:
            feedback += (output - (1/i))
        if i > 200:
            pid.target = 1
        time.sleep(t)

        feedback_list.append(feedback)
        target_list.append(pid.target)
        time_list.append(i)

    time_array = np.array(time_list)
    time_array = time_array * t
    feedback_array = np.array(feedback_list)
    target_array = np.array(target_list)

 #   plt.plot(time_smooth, feedback_smooth)
    plt.plot(time_array, target_array)
    plt.plot(time_array, feedback_array)
    plt.xlim((0, L))
    plt.ylim((min(feedback_list)-0.5, max(feedback_list)+0.5))
    plt.xlabel('time (s)')
    plt.ylabel('Velocity (m/s)')
    plt.title('Task 1')

    plt.ylim((1-0.5, 1+0.5))

    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    test(0.4, 0, 0.0, L=5, t = 0.01)
