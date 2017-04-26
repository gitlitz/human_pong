import time
import datetime
import logging
import math

ITERATION_TIME = 0.1  # in seconds

# field properties
WIDTH = 100
HEIGHT = 100

class Ball(object):

    def __init__(self):
        self.x = WIDTH / 2
        self.y = HEIGHT / 2
        self.velocity = 3
        self.angle = math.pi * 0.3  # in radians

    def update(self):
        x_diff = self.velocity * math.cos(self.angle)
        y_diff = self.velocity * math.sin(self.angle)
        self.x += x_diff
        self.y += y_diff
        logging.debug("(%.2f, %.2f)" % (self.x, self.y))
        
    def bounce_back_player(self):
        self.angle = -math.pi - self.angle
        self.velocity = -self.velocity

    def bounce_back_wall(self):
        




class Game(object):

    def __init__(self, ball, player1, player2):
        #Initialize ball and players?
        pass
    
    def update(self):
        self.ball.update()
        if self.ball.x >= WIDTH:
            if player1.is_hit(self.ball.y):
                self.ball.bounce_back()
            else:
                # Scored

        if self.ball.x <= 0:
            if player2.is_hit(self.ball.y):
                self.ball.bounce_back()
                # Do trigo shit to send ball other way
            else:
                # Scored
        
        if self.ball.y >= HEIGHT:


        
class Player(object):
    def __init__(self):
        #TODO: Hold all kinds of shit about the sensros and shit 
        pass

    def is_hit(pos_y):
        # TODO: Return if player in given position
        return True 

def update(ball):

    ball.update()


def main():
    ball = Ball()
    game = Game()
    while True:
        before = datetime.datetime.now()
        game.update()
        after = datetime.datetime.now()

        
        delta_seconds = (after - before).total_seconds()
        time_to_sleep = ITERATION_TIME - delta_seconds
        if time_to_sleep < 0:
            logging.error("iteration took too long: " + str(delta_seconds) + "seconds")
        else:
            logging.info("sleeping for: " + str(time_to_sleep) + "seconds")


if __name__ == '__main__':
    main()
