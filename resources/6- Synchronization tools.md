## Basics
- Race conditions: when multiple tasks try to access same resource at the same time
- Critical section: section of code where program is going to change or access values that are shared, and requires the following
    - Mutual Exclusion: no other process can execute critical section if one is executing already
    - Progress: if a process wants to enter critical section and no otehr process is doing so rn, then access cannot be indefinitely postponed
    - Bounded waiting: limit on how many times a process can request resources after being granted access already

## Peterson's Algorithm
- uses 2 flag vars to signify if they are or want to access critical section