# Description
This repo trains a DQN agent to solve the Banana environment. The agent's goal is to collect as many yellow bananas as possible while avoiding the blue bananas. The environment is considered solved once the agent earns an average score of 13 over 100 consecutive episodes. 

# Setup Instructions

1. Install the python dependencies
   ```
   pip install -r requirements.txt
   ```

2. Download the the Unity environment file https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana.app.zip to the root folder and unzip. If not using MacOS, you'll need to edit train.py by replacing "Banana.app" with the appropriate file path. 


# Training the agent
```
python train_double_dqn.py
```