This is the distribution of pajekpart, a small tool facilitating the preparation
of partition files for Pajek (a network analysis tool). For more information
about Pajek, see http://vlado.fmf.uni-lj.si/pub/networks/pajek/.

pajekpart works both on Linux and Windows.

(c) 2006 Ryszard Szopa <ryszard.szopa@gmail.com>
         http://szopa.tasak.gda.pl/

version 1.02, September 2 2006

What is pajekpart?
==================

pajekpart takes as its input two files: a Pajek .net file and a .cat file. The
former is a standard pajek file, the latter contains information about 
categories to which belong the nodes listed in former. As a result you get a
ready to use pajek partition file (.clu).

pajekpart tries to correct on the fly some minor mistakes. For example, if a 
node seems not to have any category assigned, pajekpart gives a warning to
stderr and puts it in the `unknown' category.

In addition to pajekpart you can find pajekpart-gui, which is a GUI wrapper for
pajekpart.

Installation
============
It is neccessary that you  have installed both Python (http://python.org/) and 
wxPython (http://www.wxpython.org/) for pajekpart to work.

Windows:
Just unpack the archive file where you wish. Enjoy.

Linux: 
Basically, unpacking the archive should be enough. You may consider copying the 
pajekpart directory somewhere to /usr/local/lib and making symbolic links 
somewhere in your path. For example:
    $ su
    # tar -xvzf pajekpart-1.02.tar.gz
    # mv pajekpart-1.02 /usr/local/lib/python/pajekpart
    # cd /usr/local/lib/python/pajekpart
    # ln -s ./pajekpart.py /usr/local/bin/pajekpart
    # ln -s ./pajekpart-gui.py /usr/local/pajekpart-gui
    # exit

List of files:
    - pajekpart.py -- the main file
    - pajekpart-gui.py -- a GUI wrapper for the former
    - README.txt -- this file
    - licence.txt -- the GPL2.

Usage
=====

       pajekpart.py [-o output-file.clu] file.net file.cat
       pajekpart.py --help

If there isn't any output file specified, pajekpart outputs the partition file
to the console. The net and cat files are determined by their extensions.

       pajekpart-gui

The usage of the GUI wrapper is self-explining.

Preparation of the .cat file
============================

The syntax of the category file is very simple. In each line consists of pair:
<node-label from the .net file> <category you wish to assign that node>,
separated with a tab. For example, a file may look like this:
    -------
    dog	mammal
    python	programming language
    squirrel	mammal
    crocodile	reptile
    emu       	bird
    alligator	reptile
    -------

The category file may contain any sign apart from the Tab sign (\t).

Known issues
============

If you create a .clu file on Linux and try to use it in Pajek, it will complain
that the file is corrupted or with Unix end-lines. Open it in a text editor 
(like Wordpad) and save it as a DOS text file. Sometimes (on Windows only) all
dialogs open twice.

Licencing
=======
See licence.txt.
