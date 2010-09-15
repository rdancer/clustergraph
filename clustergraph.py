# clustergraph.py -- graph clustered data points
#encoding:UTF-8

"""
Copyright © 2010 Jan Minář <rdancer@rdancer.org>
Copyright Gerald Kaszuba 2008

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License version 3 (three),
as published by the Free Software Foundation.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""

__version__ = "0.0.3"
__author__ = "Jan Minář <rdancer@rdancer.org>"

#
# Usage
#
# Copy the “clustergraph.py” file into the directory alongside the python
# script.  Use the ‘import’ stanza, and then simply call
# clustergraph.drawGraph():
#
#   import clustergraph 
#   clustergraph.drawGraph([[1.0, 1.1], [1.2, 1.3, 1.4], [1.5]])
#

import os
import sys
import math

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ROOT, '..'))

from pygooglechart import ScatterChart

#import settings
#import helper


def drawGraph(clusters):
    """Draw a Cartesian graph on screen; each cluster has a different colour."""

    width = 250
    height = width
    padding = 30
    xlist = []
    ylist = []
    coords = []
    i = 0
    j = 0
    length = 0

    for cluster in clusters:
	length += 1
	for point in cluster.points:
	    dimension = point.n
	    for i in xrange(dimension):
		coords.append([])
	    break
	break
    coords.append([]) # For the z-axis/colors/point size

    clusterNumber = 30
    for cluster in clusters:
	for point in cluster.points:
	    for i in xrange(point.n):
		coords[i].append(point.coords[i])
	    coords[2].append(clusterNumber)
	clusterNumber += 30


    xlist = coords[0]
    ylist = coords[1]
    zlist = coords[2]

    chart = ScatterChart(width, height, 
                         x_range=(min(xlist) - padding, max(xlist) + padding),
                         y_range=(min(ylist) - padding, max(ylist) + padding))
    chart.add_data(xlist)
    chart.add_data(ylist)
    chart.add_data(zlist)
    chart.set_axis_range('x', min(xlist) - padding, max(xlist) + padding)
    chart.set_axis_range('y', min(ylist) - padding, max(ylist) + padding)
    chart.download('clusters.png')
