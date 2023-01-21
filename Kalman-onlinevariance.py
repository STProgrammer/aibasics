class OnlineVariance(object):
    """
    this code calculates variance and mean of upcoming data
    """

    def __init__(self, iterable=None, ddof=0):
        self.ddof, self.n, self.mean, self.M2 = ddof, 0, 0.0, 0.0
        #ddof means start value of index
        #self.n start iteration
        #M2 variance
        if iterable is not None:
            for datum in iterable:
                self.include(datum)

    def include(self, datum):
        self.n += 1
        self.delta = datum - self.mean #deviation from the mean
        self.mean += self.delta / self.n #update the mean of the zi values got into
        self.M2 += self.delta * (datum - self.mean) #update the variance

    @property
    def variance(self):
        #print("M2", self.M2)
        #print("n", self.n)
        #print("ddof", self.ddof)
        return self.M2 / (self.n - self.ddof) #return mean of variances

    @property
    def std(self):
        return np.sqrt(self.variance)

class Kalman():
    def __init__(self):
        self._dt = 1  # time step
        self._pos = 785
        self._vel = 1
        #self._acc = 0
        self._pos_est_err = 300 #300
        self._vel_est_err = 100 #100
        self._acc_est_err = 4 #4
        self._pos_mea_err = 300
        self._vel_mea_err = 100
        self._acc_mea_err = 4
        self._alpha = 1
        self._beta = 1
        self.online_variance = OnlineVariance(ddof=0)
        #self._gamma = 0.01 # the acceleration doesn't change much
        
        self._q = 27 # 27 process uncerrainty for position
        self._q_v = 10 # 10 process uncertainty for velocity
        #self._q_a = 0.01 # process uncertainty for velocity


    def calc_next(self, zi):
        
        self.online_variance.include(zi)
        
        #self._pos_mea_err = self.online_variance.variance
        #self._vel_mea_err = self.online_variance.variance
        #print(self._vel_mea_err)
        
        #State extrapolation
        self._pos = self._pos + self._vel #+ 0.5*self._acc*self._dt**2
        self._vel = self._vel
        #self._acc = self._acc 
        
        #Covariance extrapolation
        self._pos_est_err = self._pos_est_err + self._vel + self._q #+ self._vel_est_err + self._q
        self._vel_est_err = self._vel_est_err #+ 0.25*self._acc_est_err + self._q
        #self._vel_est_err = self._vel_est_err + self._q_v
        #self._acc_est_err = self._acc_est_err + self._q_a
        
        #Alhpa-beta-gamma update
        self._alpha = self._pos_est_err / (self._pos_est_err + self._pos_mea_err)
        self._beta = self._vel_est_err / (self._vel_est_err + self._vel_mea_err)
        #self._gamma = self._acc_est_err / (self._acc_est_err + self._acc_mea_err)
        
        #State update
        pos_prev = self._pos
        self._pos = pos_prev + self._alpha*(zi - pos_prev)
        self._vel = self._vel + self._beta*((zi - pos_prev)/self._dt)
        #self._acc = self._acc + self._gamma*((zi - pos_prev) / (0.5*self._dt**2))
        
        #Covariance update
        self._pos_est_err = (1-self._alpha)*self._pos_est_err
        #self._vel_est_err = (1-self._beta)*self._vel_est_err
        #self._acc_est_err = (1-self._gamma)*self._acc_est_err

        return self._pos

