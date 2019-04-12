import random

class Crash(Exception):
    pass


class TiltToHigh(Exception):
    pass


class Airplane:

    MAX_TILT = 10

    def __init__(self):
        self.__angle = 0
        self.__crashed = False

    def apply_turmoil(self):
        self.__angle += random.randint(-20, 20)
        self._check()

    def tilt(self, angle):
        if abs(angle) > self.MAX_TILT:
            raise TiltToHigh()
        self.__angle += angle
        self._check()

    def _check(self):
        if self.__angle < - 60 or __angle > 60:
            self.__crashed = True
            raise Crash()


class Simulation:
    def __init__():
        self.__plane = Airplane()

    def get_correction(self):
        correction = max(Airplane.MAX_TILT, abs(self.__plane.__angle))
        if self.__plane.__angle > 0:
            return correction
        else:
            return (correction * -1)

    def step(self):
        self.__plane.apply_turmoil()
        angle = self.__plane.__angle
        correction = self.get_correction()
        self.__plane.tilt(correction)
        print("Angle: %2d Correction: %2d Angle: %2d" % (angle, correction, self.__plane.__angle))
