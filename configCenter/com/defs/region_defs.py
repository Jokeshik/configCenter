#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@file   region_defs.py
@author Geffrey
@date   2021/4/13
@brief  
"""

class RegionType(object):
    """大区ID"""
    Asia = 'Asia' # 亚洲区
    America = 'America' # 美洲区
    Europe = 'Europe' # 欧洲区

    __REGION_TYPE = {
        Asia: 1,
        America: 2,
        Europe: 3
    }


    @classmethod
    def GetRegionId(cls, region):
        if region not in RegionType.__REGION_TYPE:
            return False
        return cls.__REGION_TYPE[region]

    @classmethod
    def GetRegionDesc(cls, regionId):
        if regionId == 1:
            return cls.Asia
        elif regionId == 2:
            return cls.America
        elif regionId == 3:
            return cls.Europe
        else:
            return 'Unknown'

class ContinentType(object):
    """大洲类型"""
    Asia = 'Asia'  # 亚洲
    Europe = 'Europe'  # 欧洲
    NorthAmerica = 'North America'  # 北美洲
    SouthAmerica = 'South America'  # 南美洲
    Oceania = 'Oceania'  # 大洋洲
    Africa = 'Africa'  # 非洲
    Antarctica = 'Antarctica'  # 南极洲