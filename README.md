# agent-aeronauts-MARL
This repository contains the code and resources for Agent Aeronauts' CS480 Final Year Project:  Multi-Agent Reinforcement Learning for Strategic Network-Level Airport Slot Scheduling

## Team: Agent Aeronauts
- LYE Jian Yi
- Naomi OH
- Padme MAGTALAS
- Regina CHUA
- Sarah HOGAN
- TEOW Khai Soon

## Code 

Currently, 15000 requests are generated for each multi-agent scenario. Each request is an array containing the following information at the respective indexes:

1.index 

2.ts_dep 

3.start_date_dep 

4.num_of_weeks 

5.date_seq_dep e.g. [28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140, 147, 154, 161, 168]

6.origin_airport e.g. [0.0, 1.0, 0.0]

7.destination_airport e.g. [0.0, 0.0, 1.0]

8.fly_time

9.Status_cap_dep

10.ts_arv

11.start_date_arv

12.date_seq_arv

13.status_cap_arv

