- [How it be:](#how-it-be)
- [Multiple states](#multiple-states)
- [Queuing algorithms](#queuing-algorithms)
- [What the OS do for processes](#what-the-os-do-for-processes)
- [Process communications](#process-communications)
- [Producer / Consumer problem](#producer--consumer-problem)
- [Synchronization](#synchronization)
- [Buffering](#buffering)
- [Sockets](#sockets)
- [Pipes](#pipes)


# Processes  <!-- omit in toc -->
## How it be:
- when it is a live program, called process
- prgram code called text sections
- stack represents temporary data
- heap contains memory dynamically assinged 

## Multiple states
- new: spawned
- running: execution
- waiting: awaiting 
- ready: waiting to run on processor
- terminated: done

## Queuing algorithms
- short-term scheduler: selects process to load and allocates CPU
- long-term schedular: selects processes to be brought to ready queue
- i/o bound process: process that relies more on i/o
- CPU bound process: process that relies more on computation
- Medium term scheduling: swapping processes 

## What the OS do for processes
- provides mechanisms for 
    - process creation
        - sets param such as resources settings: share memory? run at the same time ?
    - process termination
        - kills it either waiting for it to finish, aborting, and retrieves resources allocated

## Process communications
- useful for: process cooperation
    - computational speedup
    - modularity
    - convenience
    - info sharing
  
|             Message passing              |              Shared memory              |
| :--------------------------------------: | :-------------------------------------: |
|               independant                |                dependent                |
|           easier to manage but           | harder to implement: how to synchronize |
| has to establish a link and message size |                                         |

|              Direct              |                       Indirect                       |
| :------------------------------: | :--------------------------------------------------: |
|      must name explicitely       |                use mailbox like thing                |
|    links are established auto    |          link only if process share mailbox          |
| can be `uni` or `bi` directional |                         same                         |
|        1 link for 1 pair         | each pair of processes can share multiple comms link |

## Producer / Consumer problem
- one creates what is consumed by the other
- how do you manage the buffer?
    - bounded buffer: limited
    - unbounded: unlimited

## Synchronization
- blocking:synchronous
  - each blocks the other until confirmation of space available
- non-blocking:synchronous
  - keep send
- greatly simplifies Producer / Consumer problem

## Buffering
- zero capacity: no messsages are queued, must wait for rendez-vous
- bounded capacity: fiinite length of n messages, must wait if full
- unbounded cap: never waits
  
## Sockets
- COMP2k6 stuff
- network, IP and socket, TCP or UDP
- big endian or little endian
  
## Pipes
  - named: access at any time by anyone, bidierctional
  - ordinary (or anonymous): between 2 processes only