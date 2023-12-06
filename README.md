# Project Description 
This repository contains the code and resources for Agent Aeronauts' CS480 Final Year Project:  Multi-Agent Reinforcement Learning for Strategic Network-Level Airport Slot Scheduling

## Team: Agent Aeronauts
- Duy-Anh NGUYEN
- LYE Jian Yi
- Naomi OH
- Padme MAGTALAS
- Regina CHUA
- Sarah HOGAN
- TEOW Khai Soon

## Problem 
Increasing demands of air traffic coupled with the limitation of airport infrastructure has led to fight delays, eventually causing substantial financial losses for airlines and contributing to adverse environmental impacts. A supply-side approach is not feasible in the short-term and is capital-intensive as well as limited by available space constraints. Conversely, a demand-side approach which would involve strategically scheduling slots within the existing capacity could be implemented in a relatively shorter timeframe and is a more sustainable solution. 

## Solution 
The end goal is to develop a reinforcement learning model that is able to optimally carry out network-level slot scheduling. The solution includes the following components:

1. A simulator to emulate the complexities of the multi-airport slot scheduling problem and serve as the learning environment for the agent/agents. 
2. Benchmark algorithms - MILP and MDP - to provide a reference point to assess the performance of the RL model in addressing the collaborative airport scheduling problem  

## Methodology Overview 

<p align="center">
  <img width="940" alt="Screenshot 2023-12-05 at 10 25 29 AM" src="https://github.com/lyejy/agent-aeronauts-MARL/assets/80668328/f163235e-88ec-4742-821f-8f2234b70e32">
</p><p align="center">
  Figure 1: Concept Diagram of MARL to carry out Network-Level Slot Allocation
</p>

1. For the purpose of simulations, scenarios are generated with reference to the data distribution of historical real-world data obtained during the initial phase of study hence, the scenarios can emulate the high slot demands and limited airport capacities.
2. At the start of the scenario, each airport has already independently allocated flight requests to slots but coherency of these individual slot schedules at a wider network scale cannot be guaranteed. 
3. To form a consolidated multi-airport schedule, airport agents engage in coordination using Reinforcement Learning. These airport agents will be trained to interact with the learning environment in order to optimally schedule slots at the network-level in a simulator. The simulator is designed based on our formulation of the Markov Decision Problem (MDP), our design of the observation framework and reward structure. 
4. Experiments are conducted to assess the impact of key parameters on learning with systematic variation of number of agents, different temporal scopes i.e. the number of days considered, the reward structure and the observation framework. These experiments are conducted with the goal of identifying the optimal combination of key parameters and settings. 
5. The model’s performance is then evaluated against the performance of benchmark algorithms such as Multi-Integer Linear Programming (MILP) and MDP methodologies. 

# Code  

## Usage Guidelines 

Depending on which combination of parameters you want to test for the simulator, please choose the Jupyter Notebook file accordingly and run using either Google Colab or a GPU cluster where available. 

We opted for using Jupyter Notebook (.ipynb) files exclusively over traditional Python (.py) files to leverage GPU resources efficiently. This approach allowed us to run a single file for each iteration, harnessing the power of GPU acceleration and facilitating seamless experimentation and iteration within a notebook environment.

## Data Sources/Requirements 

Due to data privacy issues, any files containing data from Official Airline Guide (OAG) were not uploaded. Hence, in order to run the files below, please liaise with the contributers to obtain the corresponding data folders/files. 

- Airport_distribution.ipynb, Movement_graphs.ipynb, MILP_MAS_real_data.ipynb, MILP_real_data.ipynb - ASEAN_2018D and ASEAN_2019D folders 

- Request_data.ipynb - ASEAN_2013D, ASEAN_2014D, ASEAN_2015D, ASEAN_2016D, ASEAN_2017D,ASEAN_2018D and ASEAN_2019D folders 


## Directory 

### Data Preprocessing & EDA
- [Airport_distribution.ipynb](Data-Preprocessing-&-EDA/Airport_distribution.ipynb)
- [Movement_graphs.ipynb](Data-Preprocessing-&-EDA/Movement_graphs.ipynb)
- [Request_data.ipynb](Data-Preprocessing-&-EDA/Request_data.ipynb)
### Evaluation
- [central_agent-stable-baselines-common-sd36.ipynb](Evaluation/central_agent-stable-baselines-common-sd36.ipynb)
- [central_agent-stable-baselines-common-sd64.ipynb](Evaluation/central_agent-stable-baselines-common-sd64.ipynb)
### MARL
- **Experiment 1: Different Observation Space**
    - [DQN_7days.ipynb](MARL/Experiment-1-diff-obs-space/DQN_7days.ipynb)
    - [Multi-Airport_SchedEnv_SMU.ipynb](MARL/Experiment-1-diff-obs-space/Multi-Airport_SchedEnv_SMU.ipynb)
    - [sim2_1day.ipynb](MARL/Experiment-1-diff-obs-space/sim2_1day.ipynb)

- **Experiment 2: Multi-Agent Different Reward Design**
    - [sim2_1day_test.ipynb](MARL/Experiment-2-multi-agent-diff-reward-design/sim2_1day_test.ipynb)

- **Experiment 3: Central Agent**
    - [sim2_1day_central_agent.ipynb](MARL/Experiment-3-central-agent/sim2_1day_central_agent.ipynb)
    - [test_sim2_1day_central_agent.ipynb](MARL/Experiment-3-central-agent/test_sim2_1day_central_agent.ipynb)

- **Experiment 4: Central Agent Setting Modifications**
    - [central_agent_no_solve_36sd.ipynb](MARL/Experiment-4-central-agent-setting-mods/central_agent_no_solve_36sd.ipynb)
    - [central_agent_no_solve_60sd.ipynb](MARL/Experiment-4-central-agent-setting-mods/central_agent_no_solve_60sd.ipynb)
    - [central_agent_sd36_2x4k_new_reward.ipynb](MARL/Experiment-4-central-agent-setting-mods/central_agent_sd36_2x4k_new_reward.ipynb)
    - [central_agent_sd60_2x1.5k_new_reward.ipynb](MARL/Experiment-4-central-agent-setting-mods/central_agent_sd60_2x1.5k_new_reward.ipynb)

- **Experiment 5: Central Agent Stable Baselines**
    - **Setting 1**
        - [central_agent_stable_baselines_setting1.ipynb](MARL/Experiment-5-central-agent-stable-baselines/Setting-1/central_agent_stable_baselines_setting1.ipynb)
    - **Setting 2**
        - [central_agent_stable_baselines_setting2.ipynb](MARL/Experiment-5-central-agent-stable-baselines/Setting-2/central_agent_stable_baselines_setting2.ipynb)
    - **Setting 3**
        - [central_agent_stable_baselines_setting3.ipynb](MARL/Experiment-5-central-agent-stable-baselines/Setting-3/central_agent_stable_baselines_setting3.ipynb)
    - **Setting 4**
        - [central_agent_stable_baselines_setting4.ipynb](MARL/Experiment-5-central-agent-stable-baselines/Setting-4/central_agent_stable_baselines_setting4.ipynb)

### MILP
- [MILP_MAS.ipynb](MILP/MILP_MAS.ipynb) (Using MILP to solve a single-airport scheduling problem with generated scenarios)
- [MILP_MAS_real_data.ipynb](MILP/MILP_MAS_real_data.ipynb) (Using MILP to solve a single-airport scheduling problem with actual data) 
- [MILP.ipynb](MILP/MILP.ipynb) (Using MILP to solve a multi-airport scheduling problem with generated scenarios)
- [MILP_real_data.ipynb](MILP/MILP_real_data.ipynb)(Using MILP to solve a multi-airport scheduling problem with actual data)


