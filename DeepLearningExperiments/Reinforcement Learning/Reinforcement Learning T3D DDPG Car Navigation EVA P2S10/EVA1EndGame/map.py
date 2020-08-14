# Self Driving Car

# Importing the libraries
import os
import numpy as np
import random
import matplotlib.pyplot as plt
import time
import torch
import torchvision
import torchvision.transforms as transforms
import sys
import scipy.ndimage
import scipy.misc

# Importing the Kivy packages
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line
from kivy.config import Config
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.core.image import Image as CoreImage
from PIL import Image as PILImage
from kivy.graphics.texture import Texture
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen , ScreenManager

import pyscreenshot as ImageGrab
# Importing the Dqn object from our AI in ai.py
#from ai import Dqn, ObsSpaceNetwork
from ai import ReplayBuffer, Actor, Critic, TD3
from numpy import asarray



# Adding this line if we don't want the right click to put a red point
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '1429')
Config.set('graphics', 'height', '660')

# Introducing last_x and last_y, used to keep the last point in memory when we draw the sand on the map
last_x = 0
last_y = 0
n_points = 0
length = 0
seed = 15 # Random seed number
start_timesteps = 1e4 # Number of iterations/timesteps before which the model randomly chooses an action, and after which it starts to use the policy network
eval_freq = 5e3 # How often the evaluation step is performed (after how many timesteps)
max_timesteps = 5e5 # Total number of iterations/timesteps
save_models = True # Boolean checker whether or not to save the pre-trained model
expl_noise = 0.5 # Exploration noise - STD value of exploration Gaussian noise
batch_size = 100 # Size of the batch
discount = 0.99 # Discount factor gamma, used in the calculation of the total discounted reward
tau = 0.005 # Target network update rate
policy_noise = 0.2 # STD of Gaussian noise added to the actions for the exploration purposes
noise_clip = 0.5 # Maximum value of the Gaussian noise added to the actions (policy)
policy_freq = 2 # Number of iterations to wait before the policy network (Actor model) is updated
episode_reward = 0
maxepisode_timesteps = 500

torch.manual_seed(seed)
np.random.seed(seed)
state_dim = 5
action_dim = 1
max_action = 5
min_action = -5

# Getting our AI, which we call "brain", and that contains our neural network that represents our Q-function
#brain = Dqn(5,3,0.9)
action2rotation = [0,5,-5]
#spacenetwork = ObsSpaceNetwork()
policy = TD3(state_dim, action_dim, max_action)
replay_buffer = ReplayBuffer()
last_reward = 0
scores = []
im = CoreImage("./images/MASK1.png")
total_timesteps = 0
timesteps_since_eval = 0
episode_num = 0
episode_timesteps = 0
done = True
t0 = time.time()

# textureMask = CoreImage(source="./kivytest/simplemask1.png")


# Initializing the map
first_update = True
i = 0

def init():
    global sand
    global goal_x
    global goal_y
    global first_update
    global img
    global sand_rotation

    global sand_penalty
    global living_penalty
    global reward

    #global ALPHA 
    sand = np.zeros((longueur,largeur))
    img = PILImage.open("./images/mask.png").convert('L')
    sand = np.asarray(img)/255
    sand_rotation = np.asarray(PILImage.open("./images/MASK1.png").convert('L'))
    goal_x = 360 #1420
    goal_y = 315 #622
    first_update = False
    #max_timesteps = 500000
    #ALPHA = 0.01
    global swap
    swap = 0
    sand_penalty = 0
    living_penalty = 0
    reward = 0
    
    
    


# Initializing the last distance
last_distance = 0

# Creating the car class

class Car(Widget):
    
    angle = NumericProperty(0)
    rotation = NumericProperty(0)
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self, rotation):
        #print("move")
        self.pos = Vector(*self.velocity) + self.pos
        ##print(rotation,type(rotation))
        self.rotation = rotation
        self.angle = self.angle + self.rotation


class Game(Widget):

    car = ObjectProperty(None)


    def serve_car(self):
        #print("servecar")
        #To Randomly Initialize after every episode
        xint = np.random.randint(0,self.width)       
        yint = np.random.randint(0,self.height)
        self.car.center = (xint,yint)
        self.car.velocity = Vector(6, 0)
    
        
    def get_obs(self, xx, yy):
        global goal_x
        global goal_y
        croppedimage = self._subimage(sand_rotation,self.car.x,(largeur - self.car.y),self.car.angle,80)
        ##print(self.car.x,self.car.y,(largeur - self.car.y),self.car.angle)
        croppedimage = croppedimage.reshape(80, 80)
        croppedimage = PILImage.fromarray(croppedimage, 'L')
        #croppedimage.save("hello.png")
        croppedimage.thumbnail((28,28))
        orientation = Vector(*self.car.velocity).angle((xx,yy))/180
        orientation = torch.as_tensor(orientation).reshape(-1, 1)
        distance = np.sqrt((self.car.x - goal_x)**2 + (self.car.y - goal_y)**2)
        distance = torch.as_tensor(distance).reshape(-1, 1)
        return croppedimage, orientation, distance
    def _subimage(self, sand, car_x, car_y, angle, crop_size=40): 
        # function takes sand image as input and center positions of car as input
        # returns an np array of angled cutout: shape (40,40,1)
        pad = crop_size*2
        #pad for safety
        crop1 = np.pad(sand, pad_width=pad, mode='constant', constant_values = 1)
        centerx = car_x + pad
        centery = car_y + pad

        #first small crop
        startx, starty = int(centerx-(crop_size)), int(centery-(crop_size))
        crop1 = crop1[starty:starty+crop_size*2, startx:startx+crop_size*2]

        #rotate
        crop1 = scipy.ndimage.rotate(crop1, -angle, mode='constant', cval=1.0, reshape=False, prefilter=False)
        #again final crop
        startx, starty = int(crop1.shape[0]//2-crop_size//2), int(crop1.shape[0]//2-crop_size//2)
        ##print(crop1.shape)
        return crop1[starty:starty+crop_size, startx:startx+crop_size].reshape(crop_size, crop_size, 1)
    
    def step(self, action, last_distance):
        global goal_x
        global goal_y
        global done
        global swap
        global sand_penalty
        global living_penalty

        #car = car()
        self.car.move(action)
        xx = goal_x - self.car.x
        yy = goal_y - self.car.y
        done = False
        obs, orientation, new_distance = self.get_obs(xx,yy)

        if sand[int(self.car.x),int(self.car.y)] > 0:
             self.car.velocity = Vector(1, 0).rotate(self.car.angle)
             #print(1, goal_x, goal_y, new_distance, max(int(self.car.x),0),max(int(self.car.y),0), im.read_pixel(max(int(self.car.x),0),max(int(self.car.y),0)))
             #Penalty for going on sand
             reward = -0.3
             sand_penalty += 0.3
        else: 
             self.car.velocity = Vector(2, 0).rotate(self.car.angle)
             reward = 1.5
             living_penalty += 1.5
             #print(0, goal_x, goal_y, new_distance, max(int(self.car.x),0),max(int(self.car.y),0), im.read_pixel(max(int(self.car.x),0),max(int(self.car.y),0)))
             if new_distance < last_distance:
                 #Reward for going towards goal
                 reward += 2
                 living_penalty += 2
            #else:
             #   reward = -0.5
                #last_reward = last_reward +(-0.2)
        #Adding done condition and negative reward for going near borders
        # self.car.velocity = Vector(2, 0).rotate(self.car.angle)
        # reward = 1
        if self.car.x < 5:
            self.car.x = 5
            reward -= 10
            sand_penalty += 10
            done = True
        if self.car.x > self.width -5:
            self.car.x = self.width - 5
            reward -= 10
            sand_penalty += 10
            done = True
        if self.car.y < 5:
            self.car.y = 5
            reward -= 10
            sand_penalty += 10
            done = True
        if self.car.y > self.height - 5:
            self.car.y = self.height - 5
            reward -= 10
            sand_penalty += 10
            done = True
        
        if new_distance < 25:
            if swap == 1:
                goal_x = 360
                goal_y = 315
                swap = 0
                file1 = open("rewards.txt","a")
                file1.write("Goal1Total Timesteps: {} Episode Num: {} Reward: {}".format(total_timesteps, episode_num, episode_reward))
                file1.write("\n")
                file1.close()
            else:
                goal_x = 1080
                goal_y = 420
                swap = 1
                file1 = open("rewards.txt","a")
                file1.write("Goal2Total Timesteps: {} Episode Num: {} Reward: {}".format(total_timesteps, episode_num, episode_reward))
                file1.write("\n")
                file1.close()
            #Reward for reaching the Goal
            reward += 25
            done = True
            
        return obs, reward, done,new_distance, orientation
    
    def update(self,dt):

        #global brain
        global last_reward
        global scores
        global last_distance
        global goal_x
        global goal_y
        global longueur
        global largeur
        global swap
        #global i
        global last_reward
        global total_timesteps
        global timesteps_since_eval
        global episode_num
        global done
        global seed# Random seed number
        global start_timesteps  # Number of iterations/timesteps before which the model randomly chooses an action, and after which it starts to use the policy network
        global eval_freq  # How often the evaluation step is performed (after how many timesteps)
        global max_timesteps # Total number of iterations/timesteps
        global save_models  # Boolean checker whether or not to save the pre-trained model
        global expl_noise# Exploration noise - STD value of exploration Gaussian noise
        global batch_size  # Size of the batch
        global discount # Discount factor gamma, used in the calculation of the total discounted reward
        global tau # Target network update rate
        global policy_noise # STD of Gaussian noise added to the actions for the exploration purposes
        global noise_clip # Maximum value of the Gaussian noise added to the actions (policy)
        global policy_freq 
        global max_action
        global episode_reward
        global episode_timesteps
        global xx
        global yy

        global sand_penalty
        global living_penalty
        
        

        longueur = self.width
        ##print("update1")
        largeur = self.height
        if first_update:
            init()
            ##print("firstupdate")
            if len(filename) > 0:
                self.serve_car()
        xx = goal_x - self.car.x
        yy = goal_y - self.car.y
        observationspace, orientation, distance = self.get_obs(xx,yy)
        if len(filename) > 0:
            action = policy.select_action(np.array(observationspace),orientation,distance)
            new_obs, reward, done, new_distance, new_orientation = self.step(float(action),distance)
        else: 
            #print("trainmode")
            #print("total_timesteps:" + str(total_timesteps))
            if done:
                #print("entering done loop")
                if total_timesteps != 0:
                    #print("Total Timesteps: {} Episode Num: {} Reward: {} Sand Penalty: {} Living Penalty: {}".format(total_timesteps, episode_num, episode_reward, sand_penalty, living_penalty))
                    #print("Total Timesteps: {} Episode Num: {} Reward: {}".format(total_timesteps, episode_num, episode_reward))
                    file1 = open("rewards.txt","a")
                    file1.write("Total Timesteps: {} Episode Num: {} Episode Timesteps: {} Reward: {} Sand Penalty: {} Living Penalty: {}".format(total_timesteps, episode_num, episode_timesteps, episode_reward, sand_penalty, living_penalty))
                    file1.write("\n")
                    file1.close()
                    if total_timesteps > start_timesteps:
                        policy.train(replay_buffer, episode_timesteps, batch_size, discount, tau, policy_noise, noise_clip, policy_freq)
                        if save_models and not os.path.exists("./pytorch_models"):
                            os.makedirs("./pytorch_models")
                        policy.save("TD3Model" + str(episode_num) , directory="./pytorch_models")
                # When the training step is done, we reset the state of the environment
                #obs = env.reset()
                self.serve_car()
                done = False
                episode_reward = 0
                episode_timesteps = 0
                episode_num += 1
            if total_timesteps < start_timesteps:
                #action = env.action_space.sample()
                #print("randomized action")
                action =  random.randrange(-5,5)*random.random()
                if expl_noise != 0:
                    action = (action + np.random.normal(0, expl_noise, size=action_dim)).clip(min_action, max_action)
                #print("action" + str(action))
                #self.car.move(action)  
            else: # After 10000 timesteps, we switch to the model
                action = policy.select_action(np.array(observationspace),orientation,distance)
        # If the explore_noise parameter is not 0, we add noise to the action and we clip it
                if expl_noise != 0:
                    action = (action + np.random.normal(0, expl_noise, size=action_dim)).clip(min_action, max_action)
                    #print("action" + str(action))
                    #self.car.move(action)  
            new_obs, reward, done, new_distance, new_orientation = self.step(float(action),distance)
            #print("reward is " + str(reward))

            # We check if the episode is done
            done_bool = 1 if episode_timesteps + 1 == maxepisode_timesteps else float(done)
            if episode_timesteps + 1 == maxepisode_timesteps:
                done = True
            # We check if the episode is done
            #done_bool = 0 if episode_timesteps + 1 == env._max_episode_steps else float(done)

            # We increase the total reward
            episode_reward += reward
            
            # We store the new transition into the Experience Replay memory (ReplayBuffer)
            replay_buffer.add((observationspace, new_obs, float(action), reward, done , orientation, new_orientation,distance,new_distance))
            
            # We update the state, the episode timestep, the total timesteps, and the timesteps since the evaluation of the policy
            observationspace = new_obs
            orientation = new_orientation
            episode_timesteps += 1
            total_timesteps += 1
            timesteps_since_eval += 1
            # if episode_timesteps == maxepisode_timesteps:
            #     done = True
        distance = new_distance

class CarApp(App):
    def build(self):
        parent = Game()
        if len(filename) > 0:
            policy.load(filename, './pytorch_models/')
        parent.serve_car()
        Clock.schedule_interval(parent.update, 1.0/60.0)
        return parent

# Running the whole thing
if __name__ == '__main__':
    global filename
    filename = "" 
    #To check if to run in train mode or evaluation mode by passing a stored model
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        CarApp().run()
    else:
        CarApp().run()
