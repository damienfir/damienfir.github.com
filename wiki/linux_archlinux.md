### Arch Linux configuration

#### Xorg
If issues with Xorg and window manager, clear cache (~/.cache).


#### Audio
For `pulseaudio` to work, `xfce` must be launched using `xinit`.
Gstreamer problem with `pulseaudio`: need to install gstreamer plugins

#### Power control
Problem of authorization for suspend, shutdown or reboot:
remove  `ck-launch-session` from .xinitrc



#### Windows dual boot
Modify menu.lst to trick Windows into thinking it's on the first hard drive.

Make a bootable USB drive from Windows install iso: use `unetbootin` version
494, `winusb` didn't work.

Dual boot with Windows causes problem with the bootloader. Need to reinstall bootloader if Windows was installed on the same HDD after Linux.

#### Customization
Terminal color generator - http://ciembor.github.com/4bit/
example from domac - https://github.com/domac/archlinux/tree/master/
example from aaron griffin - http://phraktured.net/config/
dot file sharing - http://dotshare.it/
mako config - http://mako.cc/scripts/
xcolors - http://xcolors.net/

ZSH - http://friedcpu.wordpress.com/2007/07/24/zsh-the-last-shell-youll-ever-need/

#### Bluetooth headset
Enable bluetooth in BIOS  
install bluez and blueman  
activate blutooth discovery mode on headset  
pair using blueman-manager  
add the following to /etc/bluetooth/audio.conf under [General]  
	Enable=Socket  
restart bluetooth daemon  
select device in pavucontrol  

---
#### ThinkPad
##### Fan control
Not necessary, there is a hardware controller. This method only allows manual definition of fan speeds for CPU temperatures.

Install `thinkfan` to automatically manage fan speed (and configure your own speed scale). To have it work, write

    options thinkpad_acpi fan_control=1

in `/etc/modprob.d/modprobe.conf`, reload the `thinkpad_acpi` module and restart `thinkfan` with ``rc.d restart thinkfan``.

Temperature location may vary. Also, load sensors (from lm_sensors)_, and
configure with  ̀sensors` to detect them.

##### Video card
Setting up Xorg for dual video cards. In my case, Nvidia NVS 4200M (1GB) and Intel Integrated HD Graphics 3000.

Optimus is not yet supported on Linux. Use Bumblebee to enable GPU utilization in parallel.
The option Nvidia Optimus must be enabled in the BIOS for the `nvidia` module to be loaded.

The monitor settings should be managed by `xrandr`. If a GUI is needed, use `arandr`.

