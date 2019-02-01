# Python References
Consolidated repository of Python references collected over time - done with Jupyter Notebooks (mostly).

### Synopsis
This project is a "living" repository of basic/intermediate/(possibly) advanced Python coding examples and patterns.  All examples have a corresponding Jupyter Notebook (at a minimum) and some "regular" Python (*.py) files for further examples.  Everything can be demo'ed out of [binder](https://mybinder.org/).

### Motivation
I've gathered several repositories of simple references and desired to have a consolidated Python reference which could run without cloning the repository (hence Jupyter and binder).  This is, by no means definitive or ever finished.  Additionally, it will (more than likely) lack a lot of "simpler" patterns, design concepts, and methods that can be found with a simple search.

### Installation
Note:  I make A LOT of assumptions here - I know what I know and not what you (the reader) know.  Should something seem to be lacking please feel free to let me know!  Also, originally created using Python 3.7.2.

Should you desire to use from a machine (as opposed to using binder):

1.  Clone the repository

2.  Create a virtual environment

    * Note: If you've not used virtual environments before, immediately below is the briefest of primers

	```C:\> python -m pip install virtualenv```

	* In the desired directory

	```C:\my\code\repo> python -m virtualenv .```

	```C:\my\code\repo> .\Scripts\activate```

	* "Quit" the virtual environment

	```(virt env name) C:\my\code\repo> deactivate```

3.  Install the requirements

```(virt env name) C:\my\code\repo> python -m pip install -r requirements.txt```

3.  Start up Jupyter Notebook

```(virt env name) C:\my\code\repo> jupyter notebook```

### Contributors
Most of the code herein has (in some form or fashion) come from YouTube or Stack Overflow.  Most of it I have since forgotten the origin so I emphatically appologize if I did not give credit where due!  A lot of the exmaples I have "fleshed-out" further than the original but do not claim a majority of this work as my own.

### License
This repository has been created under the GNU General Publice License v3.0.  We've all benefitted from the open knowledge on the internet and I am (attempting) to give back with this.
