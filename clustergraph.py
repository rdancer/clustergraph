# clustergraph.py -- graph clustered data points
#encoding:UTF-8

"""
Copyright © 2010 Jan Minář <rdancer@rdancer.org>

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


def drawGraph(clusters):
    """Draw a Cartesian graph on screen; each cluster has a different colour."""
