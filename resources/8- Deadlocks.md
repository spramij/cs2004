- [What is it ?](#what-is-it-)
- [How does it occur?](#how-does-it-occur)
- [Resource allocation graph](#resource-allocation-graph)
  - [Deadlock prevention](#deadlock-prevention)
  - [Deadlock avoidance](#deadlock-avoidance)
  - [Safe state](#safe-state)
  - [Banker's algo (long video), (short video)](#bankers-algo-long-video-short-video)
- [Deadlock detection](#deadlock-detection)
- [Deadlock recovery](#deadlock-recovery)

# What is it ?
- when multiple processes are indefinitely waiting on a resource being freed

# How does it occur?
- hold & wait: one process holds one resource and tries to get some other, keeping the hold on the initial resources
- circular wait: process $p_{n}$ waits for process $p_{n+1}$ 
- resource can only be released volunterringly by process: **no pre-emption**
- during MutEx lock (one process waits indefinitely for another to release) 

# Resource allocation graph
- basically, look at the slides. You have `R`esources and `P`rocesses, a process requests resources, resource is granted and orientation of arrows inversed.
- if there is a cycle, then possibility of a deadlock
    - you see if the allocation of a resources depends on something else that comes back to the same process, ie if $p_{1}$ has $r_{2}$ and wants $r_{1}$ but $p_{2}$ has $r_{1}$ and is asking for $r_{2}$, then deadlock.

## Deadlock prevention
- No preemtion: if process has resource and requests more, and cant get more, then relinquish all other already held

## Deadlock avoidance
- simplest: each process state their maximum memory allocation 

## Safe state
- state where any process can still receive resources that are requested
- how to ?
  - is Request $\le$ Need?
  - is Request $\le$ Available?
  - update:
    - Available -= Request
    - Allocated += Request
    - Need -= Request
  
## Banker's algo ([long video](https://www.youtube.com/watch?v=-VoZvNvYt-A)), ([short video](https://www.youtube.com/watch?v=lMNrmDUJ3GY))

|  Process  | Allocated |   Max    | Available |      Need       |
| :-------: | :-------: | :------: | :-------: | :-------------: |
|  $P_{n}$  | x amount  | y amound |  system   | Max - Allocated |
| $P_{n+1}$ | x amount  | y amound |           | Max - Allocated |
etc

- Running it
    - iterate through processes
    - is Need $\le$ Available?
      - Available = Available + Allocated (because it runs and finishes, relinquinshing all resources)
    - go to next process
  
# Deadlock detection
- periodic algo that checks if there are cycles in a graph or resource allocation, **but** possibly very slow (i think)

# Deadlock recovery
- just fucking kill processes until it be gone
- usually follows order depending on:
  - priority, time spent, resources used, computation time left, # of processes to termination, interactive or batch process
- or, Resource Preemption
  - select victim
  - rollback to safe state, restart process
    - but, maybe starvation here (always same rolled-back)
    - 