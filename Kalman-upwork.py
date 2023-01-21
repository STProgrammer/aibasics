import pygame as pg
from random import random, randint
import numpy as np
from numpy.linalg import norm

fps = 0.0


class Target():

    def __init__(self, background, width):
        self.background = background
        self.rect = pg.Rect(self.background.get_width() // 2 - width // 2,
                            50, width, 32)
        self.dx = 1 if random() > 0.5 else -1

    def move(self):
        self.rect.x += self.dx

        if self.rect.x < 300 or self.rect.x > self.background.get_width() - 300:
            self.dx *= -1

    def noisy_x_pos(self):
        pos = self.rect.x
        center = self.rect.width // 2
        noise = np.random.normal(0, 1, 1)[0]

        return pos + center + noise * 300.0


class Kalman():
    def __init__(self):
        self._dt = 1                                        #time step
        self._u_t = np.array([[0], [0]])                    # state vector [position velocity]'
        self._a_t = np.array([[1, self._dt], [0, 1]])       # A_t matrix
        self._a_t_T = self._a_t.transpose()                 # transpose of the A_t matrix

        self._zigma = np.array([[1, 0], [0, 1]])     #zigma matrix
        self._r_t = np.array([[1, 0], [0, 10]])             #process noise matrix R_t
        self._q_t = np.array([300])                         #measurement noise matrix Q_t
        self._c_t = np.array([1, 0])                        #C_t matrix
        self._c_t_T = np.array([[1], [0]])                  #transpose of the C_t matrix
        self._k_t = np.array([[0], [0]])                    #kalman gain matrix
        self._i = np.array([[1, 0], [0, 1]])                #identity matrix I

        self._last_pos = 0
        self.vel = 0


    def calc_next(self, xi):

        noise = np.random.normal(0, 1, 1)[0]

        #In target tracking we only get the position as a measurement.
        #Neither the velocity of the target or the acceleration.

        #Since there is the velocity in the state vector, we calculate the velocity
        #by (current position - last position)/time.
        self.vel = (xi - self._last_pos)/self._dt
        self._u_t[1][0] = self.vel + noise*50       #we add noise to compensate position noise
        self._last_pos = xi

        #Equation 1 state extrapolation equation--------------------------------------------------------------------------
        self._u_t = np.matmul(self._a_t, self._u_t)  #eq1

        #add state vector noise for both position and velocity
        noise = np.random.normal(0, 1, 1)[0]
        self._u_t[0][0] = self._u_t[0][0] + noise*1000
        self._u_t[1][0] = self._u_t[1][0] + noise
        #------------------------------------------------------------------------------------


        #Equation 2 Covariance extrapolation equation --------------------------------------------------------------------------

        self._zigma = np.matmul(self._a_t, np.matmul(self._zigma, self._a_t_T)) + self._r_t #eq2
        #--------------------------------------------------------------------------------------

        #Equation 3 Kalman gain ------------------------------------------------------------------------

        #since eq 3 is quite long the operations are seperated and processed in two varibles
        mul1 = np.matmul(self._zigma, self._c_t_T)
        mul2 = np.matmul(self._c_t, np.matmul(self._zigma, self._c_t_T)) + self._q_t
        self._k_t = (mul1 * (1/mul2))  #eq3
        #-------------------------------------------------------------------------------------


        # Equation 4 State update equation------------------------------------------------------------------------

        # since eq 4 is quite long the operations are seperated and processed in the temp variable
        temp = xi - np.matmul(self._c_t, self._u_t)
        temp = (self._k_t * temp)
        self._u_t = self._u_t + temp #eq4
        #-----------------------------------------------------------------------------------

        #Equation 5 Covariance update equation------------------------------------------------------------------------

        self._zigma = np.matmul((self._i - self._k_t*self._c_t) , self._zigma)  #eq5
        #----------------------------------------------------------------------------------

        return self._u_t[0][0] #returning the position component of the state vector


class Projectile():

    def __init__(self, background, kalman=None):
        self.background = background
        self.rect = pg.Rect((800, 700), (16, 16))
        self.px = self.rect.x
        self.py = self.rect.y
        self.dx = 0.0
        self.kalm = kalman
        self.count = 0
        self.goal = 0

    def move(self, goal):

        if self.kalm:
            goal = self.kalm.calc_next(goal)
            # print("goal:", goal)

        self.goal = goal

        deltax = np.array(float(goal) - self.px)
        # print(delta2)
        mag_delta = norm(deltax)  # * 500.0
        np.divide(deltax, mag_delta, deltax)

        self.dx += deltax
        # if self.dx:
        # self.dx /= norm(self.dx) * 50

        self.px += self.dx / 50.0
        self.py += -0.5
        try:
            self.rect.x = int(self.px)
        except:
            pass
        try:
            self.rect.y = int(self.py)
        except:
            pass


pg.init()

w, h = 1600, 800

background = pg.display.set_mode((w, h))
surf = pg.surfarray.pixels3d(background)
running = True
clock = pg.time.Clock()

kalman_score = 0
reg_score = 0
iters = 0

while running:
    target = Target(background, 32)
    missile = Projectile(background)
    k_miss = Projectile(background, Kalman())  # comment on this line when Kalman is implemented
    last_x_pos = target.noisy_x_pos
    noisy_draw = np.zeros((w, 20))

    trial = True
    iters += 1

    while trial:

        # Setter en maksimal framerate på 300. Hvis dere vil øke denne er dette en mulig endring
        clock.tick(300)

        for e in pg.event.get():
            if e.type == pg.QUIT:
                running = False

        background.fill(0x448844)
        surf[:, 0:20, 0] = noisy_draw

        last_x_pos = target.noisy_x_pos()
        # print("last_pos:",last_x_pos)
        # print("real_pos:", target.rect.x)

        target.move()
        missile.move(last_x_pos)
        k_miss.move(last_x_pos)  # comment on this line when Kalman is implemented

        pg.draw.rect(background, (255, 200, 0), missile.rect)
        pg.draw.rect(background, (0, 200, 255), k_miss.rect)  # comment on this line when Kalman is implemented
        pg.draw.rect(background, (255, 200, 255), target.rect)

        noisy_draw[int(last_x_pos):int(last_x_pos) + 20, :] = 255
        noisy_draw -= 1
        np.clip(noisy_draw, 0, 255, noisy_draw)

        coll = missile.rect.colliderect(target.rect)
        k_coll = k_miss.rect.colliderect(target.rect)  # comment on this line when Kalman is implemented

        if coll:
            reg_score += 1

        if k_coll:  # comment on this line when Kalman is implemented
            kalman_score += 1

        oob = missile.rect.y < 20

        if oob or coll or k_coll:  # change this check so that k_coll is also included when kalman is implemented
            trial = False

        if not trial:
            print("kalman:", k_miss.goal)
            print("position:", target.rect.x)

        pg.display.flip()

    print('kalman score: ', round(kalman_score / iters, 2))  # comment on this line when Kalman is implemented
    print('regular score: ', round(reg_score / iters, 2))

pg.quit()
