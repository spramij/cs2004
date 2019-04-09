- [Operating Systems](#operating-systems)
  - [What they do](#what-they-do)
  - [How it be](#how-it-be)
  - [OS is:](#os-is)
  - [What is](#what-is)
  - [Types of interrupt handling](#types-of-interrupt-handling)
  - [Input / Output](#input--output)
    - [has 2 possibilities](#has-2-possibilities)
  - [Storage](#storage)
    - [Order: from fastest to slowest](#order-from-fastest-to-slowest)
    - [What is:](#what-is)
  - [Multiprocessing](#multiprocessing)
  - [Clustered systems](#clustered-systems)

# Operating Systems
## What they do
- execute user programs & makes solving problems easier
- makes the system conveninent to use
- makes optimal use of available resources

## How it be
- Batch system:
    - multiprogramming to keep CPU busy, does more things, uses `job scheduling` to organize
- Multitasking
    - switches job so fast that user can interact with everything
- Interrupt driven
- runs in dual-mode
    - User mode & Kernel mode
    - uses `Mode bit` to differentiate
- Process management:
    - avoid deadlocks
    - creating, ending, pausing, resuming processes
    - provides mechanisms for process synch and comms
## OS is:
- resource allocator
- control program

## What is 
- a bootstrap program?
    - one that is loaded in memory at boot time
- a kernel?
    - piece of code that is what runs at the lowest level, 
- an interrupt?
    - an operation that indicates to the OS that something somehwere requires attention
- an interrupt vector?
    - an interrupt that contains the addresses of all service routines
- a trap / exception?
    - an interrupt that is raised from a program
- a context-switch?
    - an operation that saves the current registers and program counter of a running process / program
- Program counter (PC)
    - specifies the location of the next instruction to execute for a program

## Types of interrupt handling
- polling:
    - whenever an interrupt is raised/detected, every hardware device in the system is polled to find which one requires attention
- vectored:
    - whenever an interrupt is raided/detected, knows where to go - what device needs attention

## Input / Output
### has 2 possibilities
- must wait for input to end before giving control back to program
    - idles the CPU until next interrupt
    - induces a wait loop
- doesn't wait for IO completion before giving control back to program
    - requests OS to allow user to finish IO thanks to a `System Call`
    - the `Device-status table` contrains entries for I/O devices along with type, address and state

## Storage
### Order: from fastest to slowest
`Register -> Cache -> Main memory -> SSD -> HDD -> Optical drive -> Magnetic tape`

### What is:
- caching?
    - copying from `slow` to `fast` medium for faster access and all
    - raises question in terms of resource management, since it is valuable, so needs to be well managed

## Multiprocessing
- Allows for 
    - increased throughoutput
    - economy of scale
    - increased reliability
- 2 types:
    - Symmetric: every processor does the same thing
    - Asymmetric: every processor does a different task

## Clustered systems
- basically `f a n c y ` multiprocessing, with entire systems instead of processors
- often share resources like storage through SAN
- 2 types:
    - SymmetricL multiple nodes running tasks, monitoring each other
    - Asymmetric: one machine in master, others in slave
    - 

- Types of computing environments:
    - traditional
    - mobile
    - distributed (Internet)
    - client/server
    - p2p
    - virtualization
    - cloud
    - real-time embedded