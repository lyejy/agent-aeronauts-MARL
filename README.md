# Project Description 
This repository contains the code and resources for Agent Aeronauts' CS480 Final Year Project:  Multi-Agent Reinforcement Learning for Strategic Network-Level Airport Slot Scheduling

## Problem 
Increasing demands of air traffic coupled with the limitation of airport infrastructure has led to fight delays, eventually causing substantial financial losses for airlines and contributing to adverse environmental impacts. A supply-side approach is not feasible in the short-term and is capital-intensive as well as limited by available space constraints. Conversely, a demand-side approach which would involve strategically scheduling slots within the existing capacity could be implemented in a relatively shorter timeframe and is a more sustainable solution. 

## Solution 
Using reinforcement learning to carry out network-level slot scheduling 

## Methodology Overview 

## Research Findings 

## Team: Agent Aeronauts
- LYE Jian Yi
- Naomi OH
- Padme MAGTALAS
- Regina CHUA
- Sarah HOGAN
- TEOW Khai Soon

# Code  

## Usage Guidelines 

We opted for using Jupyter Notebook (.ipynb) files exclusively over traditional Python (.py) files to leverage GPU resources efficiently. This approach allowed us to run a single file for each iteration, harnessing the power of GPU acceleration and facilitating seamless experimentation and iteration within a notebook environment.

## Data Sources/Requirements 

## Directory 

### Data Preprocessing & EDA
- [Airport distribution.ipynb](Data-Preprocessing-&-EDA/Airport-distribution.ipynb)
- [Movement graphs.ipynb](Data-Preprocessing-&-EDA/Movement-graphs.ipynb)
- [Request_data.ipynb](Data-Preprocessing-&-EDA/Request_data.ipynb)

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
    - [central-agent-no-solve-36sd.ipynb](MARL/Experiment-4-central-agent-setting-mods/central-agent-no-solve-36sd.ipynb)
    - [central-agent-no-solve-60sd.ipynb](MARL/Experiment-4-central-agent-setting-mods/central-agent-no-solve-60sd.ipynb)
    - [central-agent-sd36-2x4k-new-reward.ipynb](MARL/Experiment-4-central-agent-setting-mods/central-agent-sd36-2x4k-new-reward.ipynb)
    - [central-agent-sd60-2x1.5k-new-reward.ipynb](MARL/Experiment-4-central-agent-setting-mods/central-agent-sd60-2x1.5k-new-reward.ipynb)

- **Experiment 5: Central Agent Stable Baselines**
    - **Setting 1**
        - [central_agent-stable-baselines-setting1.ipynb](MARL/Experiment-5-central-agent-stable-baselines/Setting-1/central_agent-stable-baselines-setting1.ipynb)
    - **Setting 2**
        - [central_agent-stable-baselines-setting2.ipynb](MARL/Experiment-5-central-agent-stable-baselines/Setting-2/central_agent-stable-baselines-setting2.ipynb)
    - **Setting 3**
        - [central_agent-stable-baselines-setting3.ipynb](MARL/Experiment-5-central-agent-stable-baselines/Setting-3/central_agent-stable-baselines-setting3.ipynb)
    - **Setting 4**
        - [central_agent-stable-baselines-setting4.ipynb](MARL/Experiment-5-central-agent-stable-baselines/Setting-4/central_agent-stable-baselines-setting4.ipynb)

### MILP
- [MILP_MAS.ipynb](MILP/MILP_MAS.ipynb)
- [MILP_MAS_real_data.ipynb](MILP/MILP_MAS_real_data.ipynb)
- [MILP.ipynb](MILP/MILP.ipynb)
- [MILP_real_data.ipynb](MILP/MILP_real_data.ipynb)


