
from stable_baselines3 import PPO
from testenv import snakeenv
import os
env=snakeenv()

# check_env(env)
models_dir="models/PPO"
logdir="logs"
if not os.path.exists(models_dir):
    os.makedirs(models_dir)
    
if not os.path.exists(logdir):
    os.makedirs(logdir)
eps=input("episode :")
time_steps=10000
model = PPO('MlpPolicy', env, verbose=1,learning_rate =1e-3,tensorboard_log=logdir)
model_path=f"{models_dir}/{str(eps)}0000.zip"
model = PPO.load(model_path,env=env)

for i in range(10):
    env=snakeenv()
    obs = env.reset()
    while True :
        action, _state= model.predict(obs)
        obs, rewards, done, info = env.step(action)
        if done :
            break


