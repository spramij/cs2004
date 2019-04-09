- [Operating systems](#operating-systems)
  - [System calls](#system-calls)
  - [Parameter passing](#parameter-passing)
    - [can be done in diferent ways, from simplest to most complex](#can-be-done-in-diferent-ways-from-simplest-to-most-complex)
  - [Multiple structures](#multiple-structures)
    - [From simplest to most bs](#from-simplest-to-most-bs)
  - [Program execution](#program-execution)


# Operating systems
- do the following:
    - UI : graphical or commandline
    - program execution
    - I/O operations
    - file-sysyem manipulation
    - communications
    - error detection
    - resources allocator
    - accounting of usage
    - protection & security

## System calls
- are a programming interface for services offered by an OS
    - POSIX, Win32, Java API

## Parameter passing
### can be done in diferent ways, from simplest to most complex
- passing parameters in registers
- stored in table/block of memory, and its location sent as a paramter (through register)
- through a stack, pushed on one end and pushed on the other

## Multiple structures
### From simplest to most bs
- Windows: Win32
    - most functionality under least space
- Unix
    - separates programs and kernel
- Layered:
    - layer `n` on top of layer `n-1` and can only call functions from layer directly underneath
- Microkernel:
    - least populat, gfreat on paper but was crap. Required too much latency to switch form one to another but makes testing a lot easier

## Program execution
- task control block keeps track of all running processes

