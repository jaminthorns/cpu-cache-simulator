# CPU Cache Simulator

This is a simulator for a CPU cache that I wrote for a college course. It's
meant to demonstrate some of the different
[replacement](https://en.wikipedia.org/wiki/CPU_cache#Replacement_policies),
[write](https://en.wikipedia.org/wiki/CPU_cache#Write_policies), and [mapping
policies](https://en.wikipedia.org/wiki/CPU_cache#Associativity) that CPUs can
implement.


To run the CPU cache simulator:

    simulator.py [-h] MEMORY CACHE BLOCK MAPPING REPLACE WRITE


Once you start the simulator, you can enter commands to modify and read from the
memory (which is randomized on initilization), and therefore indirectly modify
the cache. You can also print the contents of the memory and cache, as well as
view statistics about the cache's performance.

The arguments and commands, along with their descriptions, are listed below.


### Arguments

**MEMORY** - size of main memory in 2^N bytes

**CACHE** - size of the cache in 2^N bytes

**BLOCK** - size of a block of memory in 2^N bytes

**MAPPING** - mapping policy for cache in 2^N ways
*   0 - direct mapping
*   \>0 - 2^N way associative

**REPLACE** - replacement policy for cache
*   LRU - least recently used
*   LFU - least frequently used
*   FIFO - first-in, first-out
*   RAND - random

**WRITE** - write policy for cache
*   WB - write back
*   WT - write through


### Commands

**read** ADDRESS - read byte from memory

**write** ADDRESS BYTE - write random byte to memory

**randread** AMOUNT - read byte from random location in memory AMOUNT times

**randwrite** AMOUNT - write random byte to random location in memory AMOUNT
times

**printcache** START LENGTH - print LENGTH lines of cache from START

**printmem** START LENGTH - print LENGTH blocks of memory from START

**stats** - print out hits, misses, and hit/miss ratio

**quit** - quit the simulator

## Example

Here is an example run:

    python simulator.py 10 7 3 2 LRU WT

This creates a simulation with 2^10 bytes of memory, 2^7 bytes of cache, uses
8-way (2^3) associate mapping, least-recently used replacement policy, and
write-through write policy.
