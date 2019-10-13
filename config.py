# -*- coding: utf-8 -*-
"""
Configuration file containing globally available variables that can be
imported into modules and classes to change settings.  e.g.

import config

if config.DEBUG_MODE:
    # do something different for developers
    pass

"""
from enum import Enum
__author__ = 'john.stevenson, colin.wright'

DEBUG_MODE = True


# Enumeration for Additional Street Data tables used in SRWR
class AsdTableEnum(Enum):
    MAINTENANCE = 1
    REINSTATEMENT = 2
    SPECIAL_DESIGNATION = 3


class RnReportFormat(Enum):
    CSV = 1
    TXT = 2
