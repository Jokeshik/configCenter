#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@file   port_defs.py
@author Geffrey
@date   2021/4/15
@brief  
"""

# 游戏服默认端口
class GameServerPorts(object):
    MetricsPort = 20010  # 监控端口
    GmPort = 30010  # Gm端口

# Map服默认端口
class MapServerPorts(object):
    ProviderPort = 10011  # 游戏集群端口
    MetricsPort = 20011  # 监控端口
    GmPort = 30011  # Gm端口

# Link服默认端口
class LinkServerPorts(object):
    ProviderPort = 10012  # 游戏集群端口
    MetricsPort = 20012  # 监控端口
    GmPort = 30012  # Gm端口
    Port = 40012 # 对外服务端口
