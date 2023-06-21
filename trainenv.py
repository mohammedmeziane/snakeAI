import gym
from gym import spaces
import numpy as np
import cv2
import random

def collision_with_apple(apple_position, score):
    apple_position = [random.randrange(1,50)*10,random.randrange(1,50)*10]
    score += 1
    return apple_position, score

def collision_with_boundaries(snake_head):
    if snake_head[0]>=500 or snake_head[0]<0 or snake_head[1]>=500 or snake_head[1]<0 :
        return 1
    else:
        return 0

def collision_with_self(snake_position):
    snake_head = snake_position[0]
    if snake_head in snake_position[1:]:
        return 1
    else:
        return 0
    
def right(snake_position,apple_position):
    snake_head = snake_position[0].copy()
    bound = 49
    while snake_head[0]/10<bound :
        snake_head[0]=snake_head[0]+10
        if snake_head==apple_position :
            return [(apple_position[0]-snake_position[0][0])/10,-1,-1]
        if snake_head in snake_position[1:] :
            return [-1,(snake_head[0]-snake_position[0][0])/10,-1]
    return [-1,-1,49-snake_position[0][0]/10]

def left(snake_position,apple_position):
    snake_head = snake_position[0].copy()
    bound = 0
    while snake_head[0]/10>bound :
        snake_head[0]=snake_head[0]-10
        if snake_head==apple_position :
            return [(snake_position[0][0]-apple_position[0])/10,-1,-1]
        if snake_head in snake_position[1:] :
            return [-1,(snake_position[0][0]-snake_head[0])/10,-1]
    return [-1,-1,snake_position[0][0]/10]

def up(snake_position,apple_position):
    snake_head = snake_position[0].copy()
    bound = 0
    while snake_head[1]/10>bound :
        snake_head[1]=snake_head[1]-10
        if snake_head==apple_position :
            return [(snake_position[0][1]-apple_position[1])/10,-1,-1]
        if snake_head in snake_position[1:] :
            return [-1,(snake_position[0][1]-snake_head[1])/10,-1]
    return [-1,-1,snake_position[0][1]/10]

def down(snake_position,apple_position):
    snake_head = snake_position[0].copy()
    bound = 49
    while snake_head[1]/10<bound :
        snake_head[1]=snake_head[1]+10
        if snake_head==apple_position :
            return [(apple_position[1]-snake_position[0][1])/10,-1,-1]
        if snake_head in snake_position[1:] :
            return [-1,(snake_head[1]-snake_position[0][1])/10,-1]
    return [-1,-1,49-snake_position[0][1]/10]

def upright(snake_position,apple_position):
    snake_head = snake_position[0].copy()
    while snake_head[1]/10>0 and snake_head[0]/10<49:
        snake_head[1]=snake_head[1]-10
        snake_head[0]=snake_head[0]+10
        if snake_head==apple_position :
            return [(apple_position[0]-snake_position[0][0]+snake_position[0][1]-apple_position[1])/10,-1,-1]
        if snake_head in snake_position[1:] :
            return [-1,(snake_head[0]-snake_position[0][0]+snake_position[0][1]-snake_head[1])/10,-1]
    return [-1,-1,2*min(snake_position[0][1]/10,49-snake_position[0][0]/10)]

def upleft(snake_position,apple_position):
    snake_head = snake_position[0].copy()
    while snake_head[1]/10>0 and snake_head[0]/10>0:
        snake_head[1]=snake_head[1]-10
        snake_head[0]=snake_head[0]-10
        if snake_head==apple_position :
            return [(snake_position[0][1]-apple_position[1]+snake_position[0][0]-apple_position[0])/10,-1,-1]
        if snake_head in snake_position[1:] :
            return [-1,(snake_position[0][0]-snake_head[0]+snake_position[0][1]-snake_head[1])/10,-1]
    return [-1,-1,2*min(snake_position[0][1]/10,snake_position[0][0]/10)]
def downright(snake_position,apple_position):
    snake_head = snake_position[0].copy()
    while snake_head[1]/10<49 and snake_head[0]/10<49:
        snake_head[1]=snake_head[1]+10
        snake_head[0]=snake_head[0]+10
        if snake_head==apple_position :
            return [(apple_position[0]-snake_position[0][0]+apple_position[1]-snake_position[0][1])/10,-1,-1]
        if snake_head in snake_position[1:] :
            return [-1,(snake_head[0]-snake_position[0][0]-snake_position[0][1]+snake_head[1])/10,-1]
    return [-1,-1,2*min(49-snake_position[0][1]/10,49-snake_position[0][0]/10)]

def downleft(snake_position,apple_position):
    snake_head = snake_position[0].copy()
    while snake_head[1]/10<49 and snake_head[0]/10>0:
        snake_head[1]=snake_head[1]+10
        snake_head[0]=snake_head[0]-10
        if snake_head==apple_position :
            return [(snake_position[0][0]-apple_position[0]+apple_position[1]-snake_position[0][1])/10,-1,-1]
        if snake_head in snake_position[1:] :
            return [-1,(snake_position[0][0]-snake_head[0]-snake_position[0][1]+snake_head[1])/10,-1]
    return [-1,-1,2*min(49-snake_position[0][1]/10,snake_position[0][0]/10)]

#Custom Environment that follows gym interface
class snakeenv(gym.Env):
    def __init__(self):
        super(snakeenv, self).__init__()
        # Define action and observation space
        # They must be gym.spaces objects
        self.action_space = spaces.Discrete(3)
        
        self.observation_space = spaces.Box(low=-50, high=50,
                                            shape=(24,), dtype=np.float64)

    def step(self, action):
        self.t=self.t-1
        self.snake_lastposition=self.snake_position.copy()
        self.reward=0
        apple_reward=0
        
        # Change the head position based on the button direction
        self.prev_snake=self.snake_head
        if action == 0 :
            if self.dir == 0:
                self.snake_head[0] += 10
            elif self.dir == 3:
                self.snake_head[1] -= 10
            elif self.dir == 2:
                self.snake_head[0] -= 10
            else :
                self.snake_head[1] += 10
                
        elif action==1: 
            if self.dir == 0:
                self.snake_head[1] -= 10
                self.dir=3
            elif self.dir == 3:
                self.snake_head[0] -= 10
                self.dir=2
            elif self.dir == 2:
                self.snake_head[1] += 10
                self.dir=1
            else :
                self.snake_head[0] += 10
                self.dir=0
                     
        else: 
            if self.dir == 0:
                self.snake_head[1] += 10
                self.dir=1
            elif self.dir == 3:
                self.snake_head[0] += 10
                self.dir=0
            elif self.dir == 2:
                self.snake_head[1] -= 10
                self.dir=3
            else :
                self.snake_head[0] -= 10
                self.dir=2
        # Increase Snake length on eating apple
        if self.snake_head == self.apple_position:
            self.t=self.t+300
            self.apple_position, self.score = collision_with_apple(self.apple_position, self.score)
            self.snake_position.insert(0,list(self.snake_head))
            apple_reward=3000

        else:
            self.snake_position.insert(0,list(self.snake_head))
            self.snake_position.pop()
            apple_reward=0
        
        
        if collision_with_boundaries(self.snake_head) == 1 or collision_with_self(self.snake_position) == 1:
            self.done=True
        if self.snake_position[0]==self.snake_lastposition[-1] :
            self.breward=-5
        else :
            self.breward=5
            
        self.reward=self.breward+apple_reward
            
        self.observation=right(self.snake_position,self.apple_position)+left(self.snake_position,self.apple_position)+up(self.snake_position,self.apple_position)+down(self.snake_position,self.apple_position)+upright(self.snake_position,self.apple_position)+upleft(self.snake_position,self.apple_position)+downright(self.snake_position,self.apple_position)+downleft(self.snake_position,self.apple_position)
        if self.t==0:
            self.done=True
            
        self.observation=np.array(self.observation)
        self.info={}
        if self.done :
            self.reward=-200
        
        return self.observation, self.reward, self.done, self.info
    
    
    def reset(self):
        self.t=200
        self.breward=0
        self.done=False
        self.img = np.zeros((500,500,3),dtype='uint8')
        self.apple_position = [random.randrange(1,50)*10,random.randrange(1,50)*10]
        self.score = 0
        self.dir = 0
        self.snake_lastposition=0
        self.snake_position = [[250,250],[240,250],[230,250],[220,250]]
        self.snake_head = [250,250]
        self.reward=0
        
        self.observation=right(self.snake_position,self.apple_position)+left(self.snake_position,self.apple_position)+up(self.snake_position,self.apple_position)+down(self.snake_position,self.apple_position)+upright(self.snake_position,self.apple_position)+upleft(self.snake_position,self.apple_position)+downright(self.snake_position,self.apple_position)+downleft(self.snake_position,self.apple_position)
        
        self.observation=np.array(self.observation)
        self.info={}
        return self.observation 

    def close(self):
        cv2.destroyAllWindows()