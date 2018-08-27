import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pickle

def load_scores(fn):
    with open(fn, 'rb') as f:
        return pickle.load(f)

dqn_scores = load_scores('./dqn_scores.pickle')
double_dqn_scores = load_scores('./double_dqn_scores.pickle')

# plot the scores
fig = plt.figure()
ax = fig.add_subplot(111)
dqn, = plt.plot(np.arange(len(dqn_scores)), dqn_scores, label='DQN')
ddqn, = plt.plot(np.arange(len(double_dqn_scores)), double_dqn_scores, label='Double DQN')
plt.legend(handles=[dqn, ddqn])
plt.ylabel('Score')
plt.xlabel('Episode #')
plt.savefig('./score_comparison.png')
plt.show()