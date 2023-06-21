
from stable_baselines3 import A2C
from stable_baselines3 import PPO
from trainenv import snakeenv
import os
env=snakeenv()

models_dir="models/A2C"
logdir="logs"
if not os.path.exists(models_dir):
    os.makedirs(models_dir)
    
if not os.path.exists(logdir):
    os.makedirs(logdir)

time_steps=10000
model = A2C('MlpPolicy', env, verbose=1,learning_rate =1e-3,tensorboard_log=logdir)
for i in range (1,2101):
    model.learn(total_timesteps=time_steps, reset_num_timesteps=False, tb_log_name="A2C")
    model.save(f"{models_dir}/{time_steps*i}")
    env.close()
