import time
import threading


class C:
    def __init__(self):
        self.captured_input = ()
        self.captured_time = ()

    def capture_input(self):
        new_input = []
        time_input = []
        starting_time = time.time()
        capturing = True
        while capturing:
            user_input = input()
            loop_time = time.time()
            time_since_start = (int(1000 * (loop_time - starting_time)))
            new_input.append(user_input)
            time_input.append(time_since_start)
            if user_input == 'quit':
                self.captured_input = new_input
                self.captured_time = time_input
                capturing = False

    def replay(self):
        starting_time = time.time()
        time_since_start = 0
        for i in range(len(self.captured_input)):
            # Wait for the time
            while time_since_start < self.captured_time[i]:
                loop_time = time.time()
                time_since_start = (int(1000 * (loop_time - starting_time)))
            # Print the output
            print(self.captured_input[i])


t1 = threading.Thread(target=C.capture_input(C), name='t1')
t2 = threading.Thread(target=C.replay(C), name='t2')

print('finish')

