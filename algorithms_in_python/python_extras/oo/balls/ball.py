from abc import ABC, abstractmethod

class BallInterface:
    def __init__(self):
        raise Exception("Cannot implement the BallInterface")
    def bounce(self):
        pass
    
class BasketBall(BallInterface):
    def __init__(self):
        pass
    def bounce(self):
        print("Bounce Bounce Bounce")
    
class CannonBall(BallInterface):
    def __init__(self):
        pass
    def bounce(self):
        print("Boom!")
        
def bounce(b:BallInterface):
    b.bounce()
    
    
if __name__ == "__main__":
    b = BasketBall()
    bounce(b)
    
    b = CannonBall()
    bounce(b)