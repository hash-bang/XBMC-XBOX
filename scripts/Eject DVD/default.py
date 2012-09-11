# A script to eject a DVD or CD drive under Linux
#
# Written By Matt Carter <m@ttcarter.com>

__scriptname__ = "Eject DVD"
__version__ = 'v1.00'
__author__ = 'Matt Carter [m@ttcarter.com]'
__date__ = '2010-05-14'

#import xbmc, xbmcgui
#xbmc.output("loading script: " + __scriptname__ + " Version: " + __version__ + " Date: " + __date__)
import os

if __name__ == '__main__':
	os.system('sudo eject /dev/cdrw2')
