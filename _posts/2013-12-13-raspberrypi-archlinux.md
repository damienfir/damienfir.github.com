---
layout: post
title: Raspberry Pi with Arch Linux ARM
date: 2013-12-13
category: linux
---

### Installation

The installation process involves the following steps:

- Downloading the Arch Linux ARM image for Raspberry Pi from the [homepage](http://archlinuxarm.org/platforms/armv6/raspberry-pi), under the `Installation tab`
- Extracting and copying the image onto your SD Card with `dd`:
    dd bs=1M if=/path/to/archlinux-hf-*.img of=/dev/sdX
- Booting your Raspberry Pi with the SD Card

If you want to configure the Rasperry Pi remotely, it is directly accessible through `ssh` under user `root` and password `root`. Use `nmap` to find the local IP of the Raspberry Pi.

#### Resizing the partition
The SD Card might be larger than 2GB, in which case it is recommended to resize the main partition to take full advantage of the extra space. The steps are:

- From the Raspberry Pi, invoke the partition manager `fdisk`:  
```
fdisk /dev/mmcblk0
```
- If there is 3 partitions, delete the partition 2 with the command `d` (the last partition will be deleted too because it is contained into partition 2)
- Add a partition with the command `n`, type Extended, with default block values.
- Add another partition, type Logical, with default block values.
- Save to disk with the command `w`
- Reboot by typing `reboot` (you may have to unplug and re-plug the power cord)
- Resize the partition with `resize2fs /dev/mmcblk0p5`

Thanks to [Jan](http://jan.alphadev.net/post/53594241659/growing-the-rpi-root-partition) for the additional instructions about resizing the partition.


### XBMC

Using `pacman`, install the package `xbmc-rbp`.
