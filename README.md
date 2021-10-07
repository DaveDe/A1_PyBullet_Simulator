#A1 Robot Simulation Setup

The goal is to simulate an A1 robot taking random actions.

I followed [this link](https://medium.com/@apoddar573/making-your-own-custom-environment-in-gym-c3b65ff8cdaa) to make a template for a custom RL gym environment.
First, run

```
pip3 install -e .
```

to install the gym environment.

Implement step(action) and reset() functions in a1_env.py

step(action) should take a step in the pybullet simulator via the given action. In our case, action should be a vector specifying 12 target joint angles.

reset() should set the environment back to initial conditions.

To load and interact with the environment, run

```
python3 run_simulation.py
```

You will need to call step() and reset() from run_simulation.py
In a1_env.py you will send commands to the PyBullet simulator.

It's fine to use DIRECT mode in PyBullet for now (no robot visualization). 
To visualize the robot, you need to use GUI mode and you must have a GPU.

[OpenAI Gym] (https://gym.openai.com/)

[PyBullet Quickstart Guide] (https://docs.google.com/document/d/10sXEhzFRSnvFcl3XxNGhnD4N2SedqwdAvK3dsihxVUA/edit#heading=h.2ye70wns7io3)

[Example loading A1 robot in PyBullet] (https://github.com/bulletphysics/bullet3/blob/master/examples/pybullet/gym/pybullet_data/a1/a1.py)

If you have any questions, please contact me! Email: ddefazi1@binghamton.edu