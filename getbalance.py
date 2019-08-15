# ! /usr/bin/env python
# -*- coding: utf-8 -*-
from api import sdk2
if __name__ == '__main__':
    balance = sdk2.getbalance("MgNkZt2vw4eVsz386C27CBg9ve7PMWFdDgU6d8PMLNS346DjFmGTDGi4FFtZRsHtM9udgHVX1LNW99BYy9bkFj25")
    print ("余额:{0}".format(balance))
