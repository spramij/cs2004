- [Types of multicore programming](#types-of-multicore-programming)
- [Amdahl's Law](#amdahls-law)
- [Types of threads](#types-of-threads)
- [Multithreaded modes](#multithreaded-modes)
- [Implicit threading](#implicit-threading)

## Types of multicore programming
- Data parallelism: subset of data across many cores doing the same thing
- Task parallelism: data across cores doing different things

## Amdahl's Law
Speedup $\frac{1}{S+\frac{1-S}{N}}$
    with N: number of threads; S: serial portion

## Types of threads
- User threads
    - mainly made from: `POSIX Pthreads`, `Windows Win32`, `Java threads`
- Kernel threads
    - supported by the kernel

## Multithreaded modes
| User threads |       | Kernel threads |
| :----------: | :---: | :------------: |
|     Many     |  to   |      One       |
|     One      |  to   |      Many      |
|     Many     |  to   |      Many      |

- many to one implies that if a threads halts, the others cannot pursue. also, they aren't truly independant as only one can run its code on the system at a time
- Lastly, Two-Level Model, like M:M but a user thread is bound to a kernel thread

## Implicit threading
- growing since it becoming harder to manage, so let compiler/run-time do the work instead of programmer
- 3 main methods
    - Thread Pools
    - OpenMP: recognizes blocks of code that can be parallelized
    - Grand Central Dispatch
        - serial dispatch queue: blocks removed in FIFO, one by one
        - concurrent: FIFO, but multiple at a time

