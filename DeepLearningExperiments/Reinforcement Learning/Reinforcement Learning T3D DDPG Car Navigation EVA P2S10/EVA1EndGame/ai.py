# AI for Self Driving Car

# Importing the libraries

import numpy as np
import random
import os
import torch 
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torch.autograd as autograd
from torch.autograd import Variable
import time
import matplotlib.pyplot as plt

from collections import deque

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

#observationspace
# Implementing Experience Replay """

class ReplayBuffer(object):

  def __init__(self, max_size=1e6):
    self.storage = []
    self.max_size = max_size
    self.ptr = 0

  def add(self, transition):
    if len(self.storage) == self.max_size:
      self.storage[int(self.ptr)] = transition
      self.ptr = (self.ptr + 1) % self.max_size
    else:
      self.storage.append(transition)

  def sample(self, batch_size):
    ind = np.random.randint(0, len(self.storage), size=batch_size)
    batch_states, batch_next_states, batch_actions, batch_rewards, batch_dones, batch_orientations, batch_new_orientations, batch_distances, batch_new_distances= [], [], [], [], [], [], [],[],[]
    for i in ind: 
      state, next_state, action, reward, done, orientation, new_orientation,distance,new_distance = self.storage[i]
      batch_states.append(np.array(state, copy=False))
      batch_next_states.append(np.array(next_state, copy=False))
      batch_actions.append(np.array(action, copy=False))
      batch_rewards.append(np.array(reward, copy=False))
      batch_dones.append(np.array(done, copy=False))
      batch_orientations.append(np.array(orientation, copy=False))
      batch_new_orientations.append(np.array(new_orientation,copy=False))
      batch_distances.append(np.array(distance, copy=False))
      batch_new_distances.append(np.array(new_distance, copy=False))
    return np.array(batch_states), np.array(batch_next_states), np.array(batch_actions).reshape(-1, 1), np.array(batch_rewards).reshape(-1, 1), np.array(batch_dones).reshape(-1, 1), np.array(batch_orientations).reshape(-1,1), np.array(batch_new_orientations).reshape(-1,1),np.array(batch_distances).reshape(-1,1), np.array(batch_new_distances).reshape(-1,1)


class Actor(nn.Module):

  def __init__(self, state_dim, action_dim, max_action):
    super(Actor, self).__init__()
    self.max_action = max_action
    self.conv1 = nn.Conv2d(1,10,3)
    self.conv1_bn = nn.BatchNorm2d(10)

    self.conv2 = nn.Conv2d(10,10,3)
    self.conv2_bn = nn.BatchNorm2d(10)

    self.conv3 = nn.Conv2d(10,20,3)
    self.conv3_bn = nn.BatchNorm2d(20)

    self.conv4 = nn.Conv2d(20,10,1)
    self.conv4_bn = nn.BatchNorm2d(10)

    self.conv5 = nn.Conv2d(10,10,3)
    self.conv5_bn = nn.BatchNorm2d(10)

    self.conv6 = nn.Conv2d(10,20,3)
    self.conv6_bn = nn.BatchNorm2d(20)

    self.conv7 = nn.Conv2d(20,10,1)
    self.conv7_bn = nn.BatchNorm2d(10)

    self.avgpool_1 = nn.AvgPool2d(kernel_size=7)

    self.dropout = nn.Dropout(0.25)

    self.fc1 = nn.Linear(12, 50)
    self.fc2 = nn.Linear(50,10)
    self.fc3 = nn.Linear(10, 1)          

  def forward(self, x, o,d):
    #print("actor forward")
    #x = x/255
    #o = o/180
    x = x.view(-1, 1, 28, 28)
    x = F.relu(self.conv1_bn(self.conv1(x)))
    x = F.relu(self.conv2_bn(self.conv2(x)))
    x = F.max_pool2d(self.dropout(F.relu(self.conv3_bn(self.conv3(x)))),2)
    x = F.relu(self.conv4_bn(self.conv4(x)))
    x = F.relu(self.conv5_bn(self.conv5(x)))
    x = self.dropout(F.relu(self.conv6_bn(self.conv6(x))))
    x = self.avgpool_1(F.relu(self.conv7_bn(self.conv7(x))))
    x = x.view(-1, 10)
    x = torch.cat([x,  o, -o], 1)
    x = F.relu(self.fc1(x))
    #x = torch.cat([x,  o, -o], 1)
    x = F.relu(self.fc2(x))
    x = self.max_action * torch.tanh(self.fc3(x))
    return  x
    
    #F.log_softmax(x)
class Critic(nn.Module):
  
  def __init__(self, state_dim, action_dim):
    super(Critic, self).__init__()
    # Defining the first Critic neural network
    #print("critic_forward")
    self.conv1 = nn.Conv2d(1,10,3)
    self.conv1_bn = nn.BatchNorm2d(10)

    self.conv2 = nn.Conv2d(10,10,3)
    self.conv2_bn = nn.BatchNorm2d(10)

    self.conv3 = nn.Conv2d(10,20,3)
    self.conv3_bn = nn.BatchNorm2d(20)

    self.conv4 = nn.Conv2d(20,10,1)
    self.conv4_bn = nn.BatchNorm2d(10)

    self.conv5 = nn.Conv2d(10,10,3)
    self.conv5_bn = nn.BatchNorm2d(10)

    self.conv6 = nn.Conv2d(10,20,3)
    self.conv6_bn = nn.BatchNorm2d(20)

    self.conv7 = nn.Conv2d(20,10,1)
    self.conv7_bn = nn.BatchNorm2d(10)

    self.avgpool_1 = nn.AvgPool2d(kernel_size=7)

    self.dropout_1 = nn.Dropout(0.25)

    self.fc1 = nn.Linear(13, 50)
    self.fc2 = nn.Linear(50,10)
    self.fc3 = nn.Linear(10, 1)   

    ### second network critic
    self.conv8 = nn.Conv2d(1,10,3)
    self.conv8_bn = nn.BatchNorm2d(10)

    self.conv9 = nn.Conv2d(10,10,3)
    self.conv9_bn = nn.BatchNorm2d(10)

    self.conv10 = nn.Conv2d(10,20,3)
    self.conv10_bn = nn.BatchNorm2d(20)

    self.conv11 = nn.Conv2d(20,10,1)
    self.conv11_bn = nn.BatchNorm2d(10)

    self.conv12 = nn.Conv2d(10,10,3)
    self.conv12_bn = nn.BatchNorm2d(10)

    self.conv13 = nn.Conv2d(10,20,3)
    self.conv13_bn = nn.BatchNorm2d(20)

    self.conv14 = nn.Conv2d(20,10,1)
    self.conv14_bn = nn.BatchNorm2d(10)

    self.avgpool_2 = nn.AvgPool2d(kernel_size=7)

    self.dropout_2 = nn.Dropout(0.25)

    self.fc4 = nn.Linear(13, 50)
    self.fc5 = nn.Linear(50,10)
    self.fc6 = nn.Linear(10, 1)    

  def forward(self, x, u, o,d):
    #xu = torch.cat([x, u], 1)
    # Forward-Propagation on the first Critic Neural Network
    #print("critic forward")
    #u.reshape(100, 1)
    #x = x/255
    u = u/5
    #o = o/180
    x1 = x.view(-1, 1, 28, 28)
    x1 = F.relu(self.conv1_bn(self.conv1(x1)))
    x1 = F.relu(self.conv2_bn(self.conv2(x1)))
    x1 = F.max_pool2d(self.dropout_1(F.relu(self.conv3_bn(self.conv3(x1)))),2)
    x1 = F.relu(self.conv4_bn(self.conv4(x1)))
    x1 = F.relu(self.conv5_bn(self.conv5(x1)))
    x1 = self.dropout_1(F.relu(self.conv6_bn(self.conv6(x1))))
    x1 = self.avgpool_1(F.relu(self.conv7_bn(self.conv7(x1))))
    x1 = x1.view(-1, 10)
    x1 = torch.cat([x1, u, o, -o], 1)
    x1 = F.relu(self.fc1(x1))
    x1 = F.relu(self.fc2(x1))
    x1 = self.fc3(x1)
    
    # Forward-Propagation on the second Critic Neural Network
    #print("critic forward2")
    #u.reshape(100, 1)
    x2 = x.view(-1, 1, 28, 28)
    #x2 = x.view(-1, 1, 28, 28)
    x2 = F.relu(self.conv8_bn(self.conv8(x2)))
    x2 = F.relu(self.conv9_bn(self.conv9(x2)))
    x2 = F.max_pool2d(self.dropout_2(F.relu(self.conv10_bn(self.conv10(x2)))),2)
    x2 = F.relu(self.conv11_bn(self.conv11(x2)))
    x2 = F.relu(self.conv12_bn(self.conv12(x2)))
    x2 = self.dropout_2(F.relu(self.conv13_bn(self.conv13(x2))))
    x2 = self.avgpool_2(F.relu(self.conv14_bn(self.conv14(x2))))
    x2 = x2.view(-1, 10)
    x2 = torch.cat([x2, u, o, -o], 1)
    x2 = F.relu(self.fc4(x2))
    x2 = F.relu(self.fc5(x2))
    x2 = self.fc6(x2)
    return x1, x2

  def Q1(self, x, u, o, d):
    #u = u/5
    #o = o/180
    u = u/5
    #o = o/180
    x1 = x.view(-1, 1, 28, 28)
    x1 = F.relu(self.conv1_bn(self.conv1(x1)))
    x1 = F.relu(self.conv2_bn(self.conv2(x1)))
    x1 = F.max_pool2d(self.dropout_1(F.relu(self.conv3_bn(self.conv3(x1)))),2)
    x1 = F.relu(self.conv4_bn(self.conv4(x1)))
    x1 = F.relu(self.conv5_bn(self.conv5(x1)))
    x1 = self.dropout_1(F.relu(self.conv6_bn(self.conv6(x1))))
    x1 = self.avgpool_1(F.relu(self.conv7_bn(self.conv7(x1))))
    x1 = x1.view(-1, 10)
    x1 = torch.cat([x1, u, o, -o], 1)
    x1 = F.relu(self.fc1(x1))
    x1 = F.relu(self.fc2(x1))
    x1 = self.fc3(x1)
    return x1

# Building the whole Training Process into a class

class TD3(object):
  
  def __init__(self, state_dim, action_dim, max_action):
    self.actor = Actor(state_dim, action_dim, max_action).to(device)
    self.actor_target = Actor(state_dim, action_dim, max_action).to(device)
    self.actor_target.load_state_dict(self.actor.state_dict())
    self.actor_optimizer = torch.optim.Adam(self.actor.parameters(),lr=1e-4)
    self.critic = Critic(state_dim, action_dim).to(device)
    self.critic_target = Critic(state_dim, action_dim).to(device)
    self.critic_target.load_state_dict(self.critic.state_dict())
    self.critic_optimizer = torch.optim.Adam(self.critic.parameters(),lr=1e-4)
    self.max_action = max_action

  def select_action(self, state, orientation,distance):
    state = torch.Tensor(state.reshape(1, -1)).to(device)
    orientation = torch.Tensor(orientation.reshape(1, -1)).to(device)
    distance = torch.Tensor(distance.reshape(1, -1)).to(device)
    return self.actor(state, orientation,distance).cpu().data.numpy().flatten()

  def train(self, replay_buffer, iterations, batch_size=100, discount=0.99, tau=0.005, policy_noise=0.2, noise_clip=0.5, policy_freq=2):
    
    for it in range(iterations):
      
      # Step 4: We sample a batch of transitions (s, s’, a, r) from the memory
      batch_states, batch_next_states, batch_actions, batch_rewards, batch_dones, batch_orientations, batch_new_orientations,batch_distances, batch_new_distances = replay_buffer.sample(batch_size)
      state = torch.Tensor(batch_states).to(device)
      next_state = torch.Tensor(batch_next_states).to(device)
      action = torch.Tensor(batch_actions).to(device)
      reward = torch.Tensor(batch_rewards).to(device)
      done = torch.Tensor(batch_dones).to(device)
      orientation = torch.Tensor(batch_orientations).to(device)
      new_orientation = torch.Tensor(batch_new_orientations).to(device)
      distance = torch.Tensor(batch_distances).to(device)
      new_distance = torch.Tensor(batch_new_distances).to(device)
      
      # Step 5: From the next state s’, the Actor target plays the next action a’
      next_action = self.actor_target(next_state,new_orientation,new_distance)
      ###print(next_action.shape)
      # Step 6: We add Gaussian noise to this next action a’ and we clamp it in a range of values supported by the environment
      noise = torch.Tensor(batch_actions.astype(np.float32)).data.normal_(0, policy_noise).to(device)
      noise = noise.clamp(-noise_clip, noise_clip)
      next_action = (next_action + noise).clamp(-self.max_action, self.max_action)

      #noise = torch.Tensor(batch_actions.reshape(batch_size, 1)).data.normal_(0, policy_noise).to(device)
      #noise = noise.clamp(-noise_clip, noise_clip)
      ###print(noise.shape)
      
      #next_action = (next_action + noise).clamp(-self.max_action, self.max_action)
      
      # Step 7: The two Critic targets take each the couple (s’, a’) as input and return two Q-values Qt1(s’,a’) and Qt2(s’,a’) as outputs
      ###print("1")
      target_Q1, target_Q2 = self.critic_target(next_state, next_action, new_orientation,new_distance)
      
      # Step 8: We keep the minimum of these two Q-values: min(Qt1, Qt2)
      target_Q = torch.min(target_Q1, target_Q2)
      
      # Step 9: We get the final target of the two Critic models, which is: Qt = r + γ * min(Qt1, Qt2), where γ is the discount factor
      target_Q = reward + ((1 - done) * discount * target_Q).detach()
      ###print("2")
      # Step 10: The two Critic models take each the couple (s, a) as input and return two Q-values Q1(s,a) and Q2(s,a) as outputs
      current_Q1, current_Q2 = self.critic(state, action, orientation,distance)
      
      # Step 11: We compute the loss coming from the two Critic models: Critic Loss = MSE_Loss(Q1(s,a), Qt) + MSE_Loss(Q2(s,a), Qt)
      critic_loss = F.mse_loss(current_Q1, target_Q) + F.mse_loss(current_Q2, target_Q)
      
      # Step 12: We backpropagate this Critic loss and update the parameters of the two Critic models with a SGD optimizer
      self.critic_optimizer.zero_grad()
      critic_loss.backward()
      self.critic_optimizer.step()
      
      # Step 13: Once every two iterations, we update our Actor model by performing gradient ascent on the output of the first Critic model
      if it % policy_freq == 0:
        actor_loss = -self.critic.Q1(state, self.actor(state, orientation,distance), orientation,distance).mean()
        self.actor_optimizer.zero_grad()
        actor_loss.backward()
        self.actor_optimizer.step()
        
        # Step 14: Still once every two iterations, we update the weights of the Actor target by polyak averaging
        for param, target_param in zip(self.actor.parameters(), self.actor_target.parameters()):
          target_param.data.copy_(tau * param.data + (1 - tau) * target_param.data)
        
        # Step 15: Still once every two iterations, we update the weights of the Critic target by polyak averaging
        for param, target_param in zip(self.critic.parameters(), self.critic_target.parameters()):
          target_param.data.copy_(tau * param.data + (1 - tau) * target_param.data)
  
  # Making a save method to save a trained model
  def save(self, filename, directory):
    torch.save(self.actor.state_dict(), '%s/%s_actor.pth' % (directory, filename))
    torch.save(self.critic.state_dict(), '%s/%s_critic.pth' % (directory, filename))
  
  # Making a load method to load a pre-trained model
  def load(self, filename, directory):
    self.actor.load_state_dict(torch.load('%s/%s_actor.pth' % (directory, filename)))
    self.critic.load_state_dict(torch.load('%s/%s_critic.pth' % (directory, filename)))
# Implementing Deep Q Learning


