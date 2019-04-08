- [Intro](#intro)
- [CPU scheduling:](#cpu-scheduling)
- [Process synchornization](#process-synchornization)
- [Deadlocks](#deadlocks)
- [Memory](#memory)
- [Virtual memory](#virtual-memory)


# Intro
- go back to lecture recording of midterm for first half
- remember Amdahl's law & signal handling

# CPU scheduling: 
- scheduling algo
    - burst time
- assessing sched algo
- multiprocessor sched
- real-time sched
- C.F.S.

# Process synchornization
- tools & background
- raw conclusion
- critical section
- pid manager & manager
- 3 Criteria to solve
- mutual exclusion
- progress
- bounded waiting
- Peterson's solution
- hardware support
- atomic vars & operations
- Tools
- MUTEX
- Semaphores
- requires programmers to correctly implement
- Deadlocks
- resource contention
- priority inversion
- Problems & Solutions
- bounded buffer pb
- readers-writers pb
- Dining philosophers pb **`--> vvv important`**

# Deadlocks
- contention for resource
- multiprogrammed env
- defined deadlocks
- how programs use resources
- liveClock
- 4 conditions requires for deadlock to occur
- ressource alltocation graph
    - cycle in graph
- safe state
- 3 methods for dealing with deadlocks
    - ignore
    - avoid
    - recover
- Bankers algo
    - deadlock recovery

# Memory
- memory allocation
- paging
- page table & management
- fragmentation
    - external & internal
- translation lookaside buffer 
    - what its used for & what good for
- swapping
    - not virtual memory (thats in next chap)
- alternative page table impl
    - hierarchical
    - hashed
- Interl PAE

# Virtual memory
- page faults
- algs to deal with page faults
    - optimal algo is the one that we will compare all other against
- demand page
- CopyOnWrite
- page replacement alg