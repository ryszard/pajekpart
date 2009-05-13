#! /usr/bin/python2.4
# pajekpart -- a partition maker for Pajek (a program for network analysis)
#
#  Copyright (c) 2005 Ryszard Szopa
#
#  Author: Ryszard Szopa <ryszard (dot) szopa (at) gmail (dot) com>
#              http://szopa.tasak.gda.pl/
#              http://szopa.wordpress.com/
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License as
#  published by the Free Software Foundation; either version 2 of the
#  License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307
#  USA


"""
pajekpart automates preparing partitions for Pajek. It takes two files, a pajek *.net
file and the categories file (with a .cat extension) and outputs a partition file.

The categories file has a very simple syntax: it consists of pairs <node label> <category>,
separated by a tab, each in a new line. The labels should be the same as in the .net
file.

For more information about Pajek see http://vlado.fmf.uni-lj.si/pub/networks/pajek/.
"""


from sets import Set
import re
import sys


__version__ = '1.02'
__date__ = 'September 2, 2006'
__author__= 'Ryszard Szopa'
__help__ = """
pajekpart automates preparing partitions for Pajek. It takes two files, a pajek *.net
file and the categories file (with a .cat extension) and outputs a partition file.

The categories file has a very simple syntax: it consists of pairs <node label> <category>,
separated by a tab, each in a new line. The labels should be the same as in the .net
file.

For more information about Pajek see http://vlado.fmf.uni-lj.si/pub/networks/pajek/.
"""
__usage__ = """
usage: pajekpart.py [-o file.clu] file.net file.cat
       pajekpart.py --help
       
"""

class NoFilesError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class CorruptedNet(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
        
def importNodesFromNet(filename):
    """importNodesFromNet(filename) -> list
    
    Returns a list of node labels from the .net file, in the right order. See pajek's files specification."""
    if not filename:
        raise NoFilesError("You haven't specified a NET file.")
    #this is no good or bug nets:
    #nodesTable = file(filename).readlines()
    nodesFile = file(filename)
    match = re.search('\*Vertices (.+)', nodesFile.readline())
    if not match:
        raise CorruptedNet('Your NET file seems to be corrupted')
        
    nodes = []    
    for i in range(int(match.group(1))):
        regNaz = re.search('\A\d+ "(.+)"', nodesFile.readline())
        #it isn't really neccessary, but let's keep it in case the file is a bit corrupted
        if regNaz:
            nodes.append(regNaz.groups()[0])
    return nodes

##    for node in nodesTable:
##        regNaz = re.search('\A\d+ "(.+)"', node)
##        if regNaz:
##            nodes.append(regNaz.groups()[0])
##    return nodes



def importCategories(filename):
    """importCategories(filename) -> (hash, list)

    Returns a hash with node-labels as keys and the assigned categories as values and the et of categories (without duplicates)."""
    if not filename:
        raise NoFilesError("You haven't specified a CAT file.")
    categoriesTable = file(filename).readlines()

    category = {}
    for i in categoriesTable:
        # the fields of the record are separated by tabs
        datum = i.strip().split('\t')
        category[datum[0]] = datum[1]
        
    categories = list(Set(category.values()))
    return (category, categories)



def makePartition(nodes, category, categories, err=sys.stderr):
    partycja = []
    for i in nodes:
        try:
            partycja.append(categories.index(category[i]))
        except KeyError:
            # not sys.stderr because it doesn't play nice with the gui logs
            print >> err, "Warning: Something wrong with '%s'.\n         Maybe it hasn't been assigned a category? I added it to `Unknown.'"%(i)
            partycja.append(len(categories)+1)
    return partycja



if __name__=='__main__':

    print >> sys.stderr, "This is pajekpart, a Pajek partition maker, version %s (%s)."%(__version__, __date__)
    print >> sys.stderr, "(c) 2006 Ryszard Szopa."
    
    if '--help' in sys.argv:
        print >> sys.stderr, __help__
        sys.exit(0)
    
    nazwaNet = ''
    nazwaAf = ''
    if '-o' in sys.argv:
         minusO = sys.argv.index('-o')
         sys.stdout = open(sys.argv[minusO+1], "w")
         del sys.argv[minusO:minusO+2]
        
    for arg in sys.argv:
        if re.search('.net\Z', arg):
            nazwaNet = arg
        if re.search('.cat\Z', arg):
            nazwaAf = arg

    if not nazwaNet or not nazwaAf:
       print >> sys.stderr, __usage__
        
       sys.exit(1)
       
   
    
    nazwiska = importNodesFromNet(nazwaNet)
    
    afiliacja, afiliacje = importCategories(nazwaAf)

    partycja =makePartition(nazwiska, afiliacja, afiliacje)

    print "*Vertices %s \r\n"%(len(partycja))
    for i in partycja:
        print i

    sys.exit(0)
