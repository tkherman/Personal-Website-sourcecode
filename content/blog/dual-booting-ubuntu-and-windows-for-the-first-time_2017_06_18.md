Title: Dual-booting Ubuntu and Windows for the first time
Date: 2017-6-18 12:05
slug: dual-booting-ubuntu-and-windows-for-the-first-time

In short, this was a somewhat fun but extremely frustrating experience. Going
into this dual-booting adventure, I had some experience with Linux command line
having learnt them in my course but almost none with Linux the operating system.
So of course, Google became my best friend as I ventured this journey.


##<center>**THE WHY**</center>
I have had my Macbook Air (with the lowest hardware setup) for 4 years and when
it started to lag when "a few" tabs are opened on Chrome along with Spotify,
Calendar and Terminal, I knew that it was a time to upgrade because it was
somewhat affecting my productivity.

I have always liked the MacOS because I can easily do school work or side
projects on the Terminal and desktop environment is plain and simple which is
what I like. But looking at the price tag on the new 2017 MacBook Pro, it was
simply not in my budget. After some Googling, I found that the Dell XPS 15 9560 
seems pretty good and more importantly, it's much cheaper for the similar 
build quality and hardware. However, I still wanted a somewhat similar dekstop
environment and access to Linux like Terminal so that's when I decided to do
dual-boot linux. In addition, now I can play some video games in Windows that I
couldn't play in Mac, yay!

As for the Linux distro, I chose Kubuntu because Ubuntu community seems to be
the most active and I can get a lot of information and help by simply Googling.
I chose the KDE Plasma desktop environment simply because it looks nice (it is
very important to me especially coming from MacOS) and the intuitive desktop
behavior allows me to split the screen into 2, 3, or 4 windows by dragging the
windows to 4 corner which is something I do very often.

<center>![Alt Text]({filename}/images/splitscreen.png)</center>

<center>**THE HOW**</center>
The installation really wasn't that difficult. There are tons of guides out
there on how to dual-boot. I simply followed
https://ubuntuforums.org/showthread.php?t=2317843 because it's specifically for
the Dell XPS 15 even though it's for 9550 not 9560. Big thanks to
__Javier_Macias-Guar__.

In short, I did:

1. Boot in Windows and create a recovery disk on an USB using Windows built
in software
2. Use __Rufus__ to create a bootable USB drive with the Kubuntu iso on it
3. Partition my SSD
    - 100GB for the Ubuntu OS
    - ~130GB left for Windows
4. Disable fast boot option in Windows
5. Boot Windows in __Safe Mode__
6. Enter BIOS to turn off Secure Boot and changed SATA Operation from __RAID__ to
__AHCI__ then reboot
7. Disable __Safe Mode__ and then reboot again
8. Insert the USB drive with Kubuntu 17.04 while holding F12 and run the
installation with the following partition
    - 2GB for swap
    - 20GB for /
    - 75GB for /home
        - read online that this make upgrading or changing desktop etc easier
          since the home partition is separted and won't be affected when
          upgrading
        - this actually came in clutch when I reinstalled like 5 times after I
          mess something up later

This worked great, everything was working wifi, touchpad, sleep, shutdown and
boot. Grub was working and I could switch between Ubuntu and Windows easily by
rebooting. I then spent sometime customizing the Desktop because KDE offers so
much customization and it's really great. I also installed tlp which is a
battery manager. Installing and using it was simple (I didn't change any of the
setting):

```bash
sudo add-apt-repository ppa:linrunner/tlp
sudo apt-get update
sudo apt-get install tlp
sudo tlp start
```

This worked pretty well as it imporved the battery life from 4-5 to around 9-10
hours. How this works, no idea but it works! lol

It was all good until one day, I felt my labtop burning through the backpack to
the point where it was almost too hot to touch. It absolutely freaked me out
thinking that I've already broke my new labtop.

<center>**THE PROBLEMS**</center>
Before I put the labtop in my computer, I simply closed the lid assuming that it
would go into suspend. Turns out what happened was that after an update,
suspend, reboot and shutdown didn't seem to work which I had no idea why because
it worked fine.

What I think happened was that the computer didn't fully go into suspend with
many processes still running in the background. However, the fan is turnt off so
heat just kept building up until it was too hot. After hours and hours of
Googling and messing around witht the system, including a few times of
reinstalling the system, I think I've finally fixed it.

By default, Nouveau graphic driver is used when Ubuntu is installed. I think
after some update, there was some bug with problem with the driver with the
kernel. (Don't really know what or if I'm right or wrong) To fix that, I
installed the Nvidia driver, updated the kernel. I followed this guide
https://gist.github.com/whizzzkid/37c0d365f1c7aa555885d102ec61c048 by
__whizzkid__ and everything works perfectly now, well at least for now.

Essentially, when I'm using Kubuntu for daily usage, I use the integrated Intel
GPU because it's much less power intensive than using the Nvidia GPU. The
switching could be done by using prime-select (nvidia/intel) command. Since I
only game on Windows, I can keep the integrated Intel GPU by default.
