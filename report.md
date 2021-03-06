# Learning Algorithm
I trained two agents
1. A vanilla DQN agent
2. A double DQN agent that does an argmax over the local Q network to get the actions following the next states. 
   
I used the same hyper-parameters for both:

* BUFFER_SIZE = int(1e5) (replay buffer size)
* BATCH_SIZE = 64        (minibatch size)
* GAMMA = 0.99           (discount factor)
* TAU = 1e-3             (for soft update of target parameters)
* LR = 5e-4              (learning rate)
* UPDATE_EVERY = 4       (how often to update the network)


# Q-Function Model Description
The Q function model is a feedforward neural network with 37 input units with two hidden layers of 64 units and relu activations and a final linear output layer of 4 outputs.

# Plot of Rewards (DQN vs Double DQN)
![](score_comparison.png)

# Ideas for Future Work
Double DQN does not seem to affect performance significantly on this toy problem. I suspect it may help more with the pixel version and I plan to try that. I'd also like to compare these results with a dueling-DQN model.