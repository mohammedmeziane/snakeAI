# snakeAI
 Training an artificial intelligence to play the famous game Snake.

<h1>Model used : 
<h3>The model used is an instance of the Proximal Policy Optimization (PPO) algorithm, which is a popular reinforcement learning algorithm used for training policies in environments with continuous action spaces.
<br>
Overall, this model configuration that we used aims to train a policy using the PPO algorithm with an MLP-based policy representation, utilizing a learning rate of 1e-3, and providing detailed output during training. The training progress is logged to facilitate analysis using TensorBoard.
 <br>
link to documentation :https://stable-baselines3.readthedocs.io/en/master/modules/ppo.html
<h1>Vision
<h2>The snake can see in 8 directions. In each of these directions the snake looks for 3 things:
 <br>
 - Distance to food
 <br>
 -  Distance to its own body
 <br>
 - Distance to a wall

<h2>3 x 8 directions = 24 inputs. The 4 outputs are simply the directions the snake can move.<h2>

https://github.com/mohammedmeziane/snakeAI/assets/92160568/d21f3a53-ba8e-4404-a96f-5b9eb571b1f5



<h1>Training :
<h3>Each episode, the model is trained for 10,000 timesteps, and at the end of each episode, a version of the model is saved.
 <h2>reward system :</h1>
 <h3>
The agent receives a positive reward when the snake eats an apple, a negative reward when it dies, and a small negative reward when it repeatedly loops in the same position. </h3>
<h3>Models can be saved and loaded in order to test a model in new situations. The weights for each connection are saved in a CSV file. The evolution graph is also saved in order to view the evolution progress of the model.<h3>

<h1>Save & Load
<h3>Models can be saved and loaded in order to test a model. we can use tensorboard to visualize the evolution of the mean  reward and mean length of each episode during training.


