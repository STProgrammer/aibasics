class Kalman():
    def __init__(self):
        self._dt = 1  # time step since it's just one I didn't use it in equations
        self._pos = 785 # postition estimated
        self._vel = 1 # velocity estimated
        self._pos_est_err = 300 # estimation error / uncertainty for postiion
        self._vel_est_err = 100 # estimation error / uncertainty for velocity 
        self._pos_mea_err = 300 # measurement error for position
        self._vel_mea_err = 100 # measurement error for velocity
        self._alpha = 1 # alpha
        self._beta = 1 # beta
        
        self._q = 27 # 27 process noise for position
        self._q_v = 10 # 10 process noise for velocity
        
    """ I have first tried using gamma, but that just makes things too complicated. Most of the time the Target has
    has constant velocity, it only accelerates once in each try and that's when changing position. So I thought there's no need
    to include acceleration or gamma, and just use a model where there's constant velocity. But since the velocity isn't
    constant 100% of the time in reality, we added some "process uncertainty" for velocity estimation error and position
    estimation error to make up for that, as described in KalmanFilter.net
    """


    def calc_next(self, zi):
        
        #Since dt = 1 we don't use self._dt in the code below as 
        #it doesn't make any difference in this case
        
        #State extrapolation
        self._pos = self._pos + self._vel
        
        #Covariance extrapolation
        self._pos_est_err = self._pos_est_err + self._vel_est_err + self._q
        self._vel_est_err = self._vel_est_err + self._q_v
        
        #Alhpa-beta update
        self._alpha = self._pos_est_err / (self._pos_est_err + self._pos_mea_err)
        self._beta = self._vel_est_err / (self._vel_est_err + self._vel_mea_err)
        
        #State update
        pos_prev = self._pos
        self._pos = pos_prev + self._alpha*(zi - pos_prev)
        self._vel = self._vel + self._beta*((zi - pos_prev)/self._dt)
        
        #Covariance update
        self._pos_est_err = (1-self._alpha)*self._pos_est_err
        self._vel_est_err = (1-self._beta)*self._vel_est_err

        return self._pos
