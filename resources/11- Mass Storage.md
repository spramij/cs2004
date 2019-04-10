- [Basics](#basics)
- [Definitions](#definitions)

# Basics
## Not very important (i dont think) but nice to have  <!-- omit in toc -->
- [magnetic drives](https://assets.microncpg.com/content/dam/crucial/articles/about-ssd/ssd-vs-hdd-which-is-better-for-you/hard-drive.jpg.transform/large-jpg/img.jpg), are made up of usually multiple (!very sensitive!) platters, stacked on top of each other, with each having their separate read and write heads. They are magnetic and levitate directly on the surface of the drives. 
- Connection link: multiple types, 
    - (most popular) SATA rev3 (called SATA3) with a **theorical** bandwidth of 6Gb/sec, 
    - SATA2 has 3Gb/s
    - PCIe - direct lane to CPU, very very fast. Used now in modern SSD.
    - but also PATA and IDE 
- Sizes: 2.5", but also 3.5" and 1.8"
- Wildly varying sizes, can reach up to [14Tb](https://www.westerndigital.com/products/data-center-drives/ultrastar-dc-hc500-series-hdd)


# Definitions
- Transfer rate: between drive and computer
- Positioning time: also called random access time, is the sum of:
    - seek time: time it takes the head to get to where the data is, commonly of 9ms, ranges approximately from 3ms to 12ms 
    - Rotational latency: time for disk to get under the head
- Effective transfer rate: actual transfer rate, of 1Gb/s on SATA3
- Average latency: `1/2 * latency`
- Access latency: `Average access time =  average seek time + average latency`
- Average IO time: `average access time + controller overhead + (amount to transfer / transfer rate)`

# Solid State Drive - SSD
- flash memory
- nowadays, more reliable than HDD, faster, but more expensive
- has other problems: magnetic drives and tapes can be indefinitely re-written, not flash memory

# Magnetic tape
- very slow random accss time
- but normal sequential read speeds: 140MB/s
- very very reliable (basically will last forever)

# Disk structure
- large 1-D array of logical blocks
- low level formatting creates logical blocks on physical media, and maps to physical sectors on the drive
    - mapping starts from 0, from outermost to innermost
    - each sector can hold metadata, data, and ECC (for error correction)
- translating from logical to physical is usually reaady, its the same, unless there are corrupted blocks

# Storage arrays
- disks can be simply added, 
- provides redundency, and improved efficiency, and very large storage space.

# Storage Area Network (SAN)
- can be accessed by multiple hosts
- connects through Fibre channel, giving low latency
- uses buses typically

# Network Atached Storage (NAS)
- consumer solution
- basically small server with multiple hard drives that you can access anywhere within your local network (possibly extended to the whole Internet)
- uses TCP/IP and UDP

# Disk Scheduling
- makes sure disk is used efficiently
    - minimize seek time
- multiple algos:
    - Shortest Seek Time First: may cause starvation - **Most common**
    - SCAN: from one end of the disk to the other, servicing any request, and again from the end to the beginning
    - C-SCAN: same, but doesn't service requests when returning
    - C-LOOK: instead of going from one end to another, goes from closest to furthest request only
        - Both C-SCAN and C-LOOK are better for heavy loads on HDD

# Disk Management
- can be through OS: makes use of its own strcture (NTFS, FAT32, EXT4)
- or can be raw, like for databases stuff

# Swap space management
- when RAM runs out (when memory runs out) will use main storage as secondary storage
- is very slow compared to main memory

# Redundency
- Allows to have longer mean time to failure, repair, and mean time to data loss
- uses cheap resources (HDD) in a specific structure to have multiple copies of same data in different places, and is able to self-heal in case of data corruption
- but makes it a bit slower, so sometimes coupled with fast memory as cache (NV-RAM, SSD) to temporarily store data before being flushed to the (slower) HDD
- Sometimes has a hot-spare HDD, that is unused but in case of a failure will be put in use
- RAID0: normal, no redundency. Maximises allocable space
- RAID1+0: striped mirror, RAID0+1: mirrorer stripes
    - provides high performance and reliability
    - takes a file and writes a part of it on one drive, the other part to another drive, etc
- RAID4, RAID5, RAID6 uses less redundency, but gives more usable space

# Checksums
- Common in Solaris, using ZFS
- makes checksums of data, is able to recover in case of error
- but is fundamentally different: 
    - disks allocated in pools
    - access to pools is abstracted

# Stable storage
- ensure no data loss at all
- Step 1: multiple nonvolatile storage media
- update (write) in controlled manner to avoid data loss
- Disk writes have 3 outcomes
    - success: correct
    - partial failure: failed in the middle, the written to sectors could be corrupted
    - total failure: never started writing, so sectors are intact
- binds a logical address to 2 physical addresses, and only after writing to the 2 addresses is the write operation called successful