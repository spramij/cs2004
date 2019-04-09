## [TutorialsPoint video](https://www.tutorialspoint.com/operating_system/os_process_scheduling_algorithms.htm)
- [TutorialsPoint video](#tutorialspoint-video)
- [Main types:](#main-types)
- [Dispatcher](#dispatcher)
- [How to evaluate good CPU scheduling: criterias](#how-to-evaluate-good-cpu-scheduling-criterias)
- [Scheduling algos](#scheduling-algos)
- [Convoy Effect](#convoy-effect)
- [Gantt Charts](#gantt-charts)
- [Thread scheduling](#thread-scheduling)
- [Multiple Processor Scheduling](#multiple-processor-scheduling)
- [Latency](#latency)
- [Little's Formula](#littles-formula)
## Main types:
- preemptive:
    - when a process switches goes `running --> ready` or `waiting --> ready` 
- non-preemptive
    - when process terminates or `running --> waiting`

## Dispatcher
- gives control to CPU to the process selected by short-term sched
    - context-switch
    - switch to user-mode
    - jump to proper location in user program to restart program
    - restart the program
- Dispatch latency: time taken by dispatch to stop one process and starting another

## How to evaluate good CPU scheduling: criterias
|                             Criteria                              | Optimization |
| :---------------------------------------------------------------: | :----------: |
|                 CPU utilization: keep it busy af                  |     TOP      |
|   Throughoutput: # of process that complete per time time unit    |     TOP      |
|    Turnabout time: length of time to execute specific process     |     MIN      |
|              Waiting time: time spent in ready queue              |     MIN      |
| Response time: time between request submission and first response |     MIN      |

## Scheduling algos
- First Come First Serve
- Shortest Job First: `!optimal!`, but hard to predict the length of next CPU request
    - Can be predicted using formula: $t{n+1} = \alpha*t_{n}+(1+\alphq)*t_{n}$ with $\alpha=\frac{1}{2}$ usually, and $t_{n}=length of current process time$
- Shortest remaining time first
- Priority scheduling
    - `Be careful to see if the higher the number the higher the priority or the inverse!`
    - sometimes problem since low priority may starve, `solution`: decrease priority of running process over time
- Round Robin
    - each process runs for a max of `q` time, with no process waiting more than $(1-n)q$ time to be serviced.
    - Gantt time: start by 1st process, lasts for q time, go to next, until all are over.
  -  Wait time: take each cell a process n has, and sum up the difference of each `service time - arrival time`
- Multilevel Queue
    - basically hybrid, and a process moves from one queue to another
- Completely Fair Scheduler
    - quantum is set on CPU proportion, has multiple scheduling classes (default, realtime), 


## Convoy Effect
Better when short processes comes before long processes

## Gantt Charts
Let us assume we have 3 processes, $P_{1}$, $P_{2}$ and $PP_{3}$, lasting 15, 25, 10 times units respectively.

```
 ____________________________________________________
|       P1      |           P2            |    P3    |
|_______15______|___________25____________|____10____|
0               15                        40         50
```
along with:
- Average Waiting time: $\frac{0+15+40}{3} = 18.3$

## Thread scheduling
- separate for user and kernel threads
- when supported, threads are scheduled, not processes

## Multiple Processor Scheduling
- Asymmetric: no data sharing needed, only one processor accesses system data structures
- Symmetric: each processor is self-scheduling, either indiv ready process queue or share one
- Push $ Pull migration: take or give tasks to other processors to keep balanced

## Latency
- Interrupt latency: time from arrival of interrupt to start of interrupt routnine
- Dispatch latency: time for schedule to switch processes around

## Little's Formula
- in steady state, we must have # of processes leaving queue == processes arriving, so $n=\lambda*W$, with $\lambda$=avg arrival rate, $n$ avg queue length, $W$ avg wait time in queue