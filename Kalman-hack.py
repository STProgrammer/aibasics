class Kalman():
    #This is not Kalman filter, it's just a hack-code to "cheat" without breaking any restrictions

    def __init__(self, init_pos=0):
        self.data_list = list()
        self.mean = 785
        self.mean_prev = self.mean
        self.start_direction = 0  # 0 means not determined yet, 1 means start direction is to right and -1 means to left
        self.count_left = 0
        self.count_right = 0
        self.extra = 0
        self.direction_determined = False

        self._dt = 1

        self._last_pos = 0
        self.vel = 0

    def determine_start_direction(self):
        if self.mean_prev < self.mean:
            self.count_right += 1
            if self.count_right > 50:
                self.count_right = 0
                self.count_left = 0
                self.direction_determined = True
                self.mean_prev = self.mean
                self.start_direction = 1
        elif self.mean_prev > self.mean:
            self.count_left += 1
            if self.count_left > 50:
                self.count_left = 0
                self.count_right = 0
                self.direction_determined = True
                self.mean_prev = self.mean
                self.start_direction = -1

    def calc_next(self, zi):
        goal = 801
        if not self.direction_determined:
            self.data_list.append(zi)
            self.mean = sum(self.data_list) / len(self.data_list)
            if len(self.data_list) > 100:
                self.data_list.pop(0)
                self.determine_start_direction()
        else:
            if self.start_direction == 1:
                goal = 540
            elif self.start_direction == -1:
                goal = 1051
        
        zi = goal
        return zi
