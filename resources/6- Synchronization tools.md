- [Basics](#basics)
- [Peterson's Algorithm](#petersons-algorithm)
- [Solutions - Read more here](#solutions---read-more-here)


## Basics
- Race conditions: when multiple tasks try to access same resource at the same time
- Critical section: section of code where program is going to change or access values that are shared, and requires the following
    - Mutual Exclusion: no other process can execute critical section if one is executing already
    - Progress: if a process wants to enter critical section and no otehr process is doing so rn, then access cannot be indefinitely postponed
    - Bounded waiting: limit on how many times a process can request resources after being granted access already

## Peterson's Algorithm
- uses 2 flag vars to signify if they are or want to access critical section

## Solutions - [Read more here](https://stackoverflow.com/a/346678)
- Mutex lock
  - requires busy waiting (checking every x time and basically wastes resources) - called a spinlock
  - they ensure only one process uses the resource
- Semaphores
  - a little more advanced / sophisticated
  - they limit the number of processes accessing a resources
- [Monitors](http://www.cs.utexas.edu/users/witchel/372/lectures/08.Semaphore-Monitors.pdf)
  - basically mutex but for any number of processes
  - keeps the vars abstracted under a class, and functions/threads call those to access var (I think)
  - 
