import random
import logging
import time


class Crash(Exception):
    pass


class TiltToHigh(Exception):
    pass


class Environment:

    MAX_DEVIATION = 30

    @classmethod
    def get_turmoil(self):
        return random.randint(self.MAX_DEVIATION * -1, self.MAX_DEVIATION)


class Airplane:

    MAX_CORRECTION = 10
    CRASH_LIMIT = 60

    def __init__(self):
        self.angle = 0
        self.__crashed = False

    def apply_turmoil(self):
        self.angle += Environment.get_turmoil()
        self._check()

    def tilt(self, angle):
        if abs(angle) > self.MAX_CORRECTION:
            raise TiltToHigh()
        self.angle += angle
        self._check()

    def _check(self):
        if self.angle < (-1 * self.CRASH_LIMIT) or self.angle > self.CRASH_LIMIT:
            self.__crashed = True
            raise Crash()


class Simulation:
    def __init__(self):
        self.__plane = Airplane()

    def get_correction(self):
        correction = min(Airplane.MAX_CORRECTION, abs(self.__plane.angle))
        if self.__plane.angle < 0:
            return correction
        else:
            return (correction * -1)

    def step(self):
        self.__plane.apply_turmoil()
        angle = self.__plane.angle
        correction = self.get_correction()
        self.__plane.tilt(correction)
        logger = logging.getLogger('flightSimulation')
        logger.info("Angle: %2d Correction: %2d Angle: %2d" % (angle, correction, self.__plane.angle))

    def continuous(self):
        try:
            while True:
                self.step()
                time.sleep(.35)
        except Crash:
            logger = logging.getLogger('flightSimulation')
            logger.info("Plane crashed.")


if __name__ == "__main__":
    logger = logging.getLogger('flightSimulation')
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    logger.addHandler(ch)
    sim = Simulation()
    sim.continuous()
