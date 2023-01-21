# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt

class Kalman():
    
    def __init__(self, initial_weight):
        self._n = 0
        self._z_n = initial_weight
        self._xn_n = 0.0
        self._xn_n_minus_1 = 0.0
        self._xn_n_pluss_1 = 0.0
        self._K_n = 0.0
    
    def Kn(self):
        if self._n > 0:
            self._K_n = 1 / self._n
        return self._K_n
    
    def StateUpdateEquation(self):
        return self._xn_n_minus_1 + self.Kn() * (self._z_n - self._xn_n_minus_1)
    
    def Iterate(self):
        self._n += 1
        self._xn_n_minus_1 = self._xn_n
    
    def Measurement(self, value):
        self._z_n = value
        self._xn_n_pluss_1 = self._xn_n
    
    def Run(self, weights):
        kalmanlist = list()
        for weight in weights:
            self.Measurement(weight)
            self.Iterate()
            self._xn_n = self.StateUpdateEquation()
            self._xn_n_pluss_1 = self._xn_n
            kalmanlist.append(self._xn_n)
        return kalmanlist


actual_weight = 78.56
zns = [78.2,78.9,78.1,78.3,78.4,78.9,78.6, 78.8,78.7,78.4,79,78.2,78.7,78.7,78.3]

k = Kalman(70)



kalman_list = k.Run(zns)

x_axis = list(range(0,len(kalman_list)))

plt.plot(x_axis, zns)
plt.plot(x_axis, [actual_weight for _ in range(len(x_axis))])
plt.plot(x_axis, kalman_list)
plt.legend(['Målt', 'Virkelig', 'Kalman'])
plt.xlabel('Måling nr.')
plt.ylabel('Vekt')
plt.show()


    
    
    