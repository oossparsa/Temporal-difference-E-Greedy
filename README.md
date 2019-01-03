# Temporal-difference-E-Greedy
implementation of Temporal difference &amp; E-Greedy algorithms of reinforcement learning for an AI agent
The agent starts in state S. When it reaches state G, it will receive a reward of 1000 and the episode ends. When it reaches a state W, it will receive a reward of -250 and the episode ends. Every other step will be rewarded with -1. The agent has eight actions: It can move to an adjacent cell (according to eight-neighborhood). The actions are not deterministic. Only with probability 0.8, the desired action is carried out. With probability 0.1, the agent deviates from the desired direction by one cell to the left or to the right (axis-parallel moves become diagonal moves and vice versa). Actions that would move the agent off the grid are handled by truncating the resulting cell coordinates to valid grid coordinates. Hence, almost all diagonal moves outside the grid (except for moves into cells extending corners) will result in a horizontal or vertical move.  1000 episodes are randomly generated according to this policy:
Move to the right with probability 0.5. Move to the upper right with probability 0.25, move to the lower right with probability 0.25. 

File #1 Computes the state-value for each visited state using TD(0) Policy Evaluation.
File #2 actions are chosen using ε-greedy action selection (ε=0.1). 
*The resulting policy is visualized using arrows.
