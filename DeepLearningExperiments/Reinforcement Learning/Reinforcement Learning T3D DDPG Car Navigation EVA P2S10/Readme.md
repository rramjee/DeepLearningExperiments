# EVA Phase 2 Session 10 End Game Assignment

Youtube link - https://youtu.be/IEgZx8cdL9c


## Environment Stack
- Kivy (map.py and car.kv) - for the city map, car and define other environment conditions
- Pytorch (The T3D Model) ai.py file

#### The Goal of the assignment is to :

1. Train a car to move around the city and reach a defined destination.
2. Car should follow the road and not hit sand or walls or water bodies.

## Parameters Used
1. State Parameters to the CNN

  1. **Observation Space** - I'm using image of the car moving in the map as the observation space or state. The car location is know by car.x and car.y and surrounding pixels are cropped (80*80) of the sand image. Later image is resized before passing to actor and critic models *(Initially, tried to add the car rotation in the image using orientation and angle but facing an issue of car rotating around a same place. Also, most of the times the program is crashing my laptop. FInally, today ran it on my friend's laptop with GPU. Able to train. Now model is going between target A to Target B but still not taking roads. Need to train further to improve my model)*

  2. **Orientation**: Positive and negative orientation are concatenated as input to actor and critic models

  3. **Action** - Action value is concatenate and passed as input to critic mode

    

### Replay Buffer

Replay buffer contains

1. **Current observation** - The current state of the car in the road
2. **New observation** - The state of the car after taking a particular action. 
3. **Action** - The action taken through following steps
	random.randrange(-5,5)*random.random() until start time steps
	policy.select_action(np.array(observationspace)) after start time steps.after sufficient memory is built.
	The selected action is passed through self.step(action,last_distance) function, make the necessary action on the environment/game and get new_obs, reward and done flags.
4. **Reward**. - The Reward for taking the specific action in the environment. Tried various combination of rewards but so far no success with accomplishing the goal of the assignment
5. **Done** -  Flag to specify if the taking a particular action resulted in end of an episode or not. In the assignment environment, reaching the goal, reaching the walls or reaching a certain number of steps without any achievement of goal are considered as done = True.
6. **Current Orientation**: Current orientation of the car towards the goal. (added it as I removed the car image from the cropped image)
7. **Next Orientation:** Next orientation of the car toward the goal after taking the required action or moving to new state.
8. **current distance**: current distance of the car from the goal *(not being used in the model now as it is not helping to overcome car rotation issue)* 
9. **next distance**: distance of the car after taking the action.*(not being used in the model now as it is not helping to overcome car rotation issue)*

### Issues faced:

1. TAfter the latest training today, the car is going from target A to target B but not taking roads. 

#### Things tried to fix car rotation issue: 


1. Adding orientation with state as input actor and critic models.
2. Played around with learning rate, max episode steps, reward values but nothing seem to work.

### Thanks Note:
Thanks a lot Rohan Shravan for this wonderful journey. This has been a fantastic learning experience. Thanks again for inspiration and motivation to learn AI.



