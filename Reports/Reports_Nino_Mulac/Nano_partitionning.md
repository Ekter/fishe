# Jetson Nano partitionning problems

The Jetson Nano has an internal storage of 16GB, but it is not enough to store all the data we need.
So we use an external storage, a microSD card, to store the data we need.

But the storage, defined in partitions of filesystems, is not well configurated.
The root partition is occupying all the space on the nano, and there is no partition for the data we need on the sd card.
The installation should have been done another way, with a root partition (`/`) on the nano and a data partition on the sd card (`/home`).
This way, we could store more data.
But the biggest part of space used is the software used on the Nano.
For example, it has pytorch, tensorflow, and openGL, which are IA packages, each of them taking around 4GB of space.
So the root partition is already almost full, and it will be hard to install more software on it, including the dependancies we may need.
One solution may be to use only the bare ubuntu image for jetson nano, provided on their installation page.
Or we could try to install software on the `/home` partition, maybe with `snap` for example, but it isn't possible for all softwares.
Plus, we still need to reinstall the OS to change the `/home` location to the sd card, since it was not configured this way when it was first installed.
But I didn't manage to do it, altough I  have a lot of experience with ubuntu installation.
