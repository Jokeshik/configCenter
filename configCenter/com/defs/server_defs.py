#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@file   server_defs.py
@author Geffrey
@date   2021/4/14
@brief  
"""

class ServerType(object):
    Auth = "Auth"
    ServerList = "ServerList"
    GameServer = "Game"
    MapServer = "Map"
    LinkServer = "Link"
    ServerListControl = "serverListControl"

    __SERVER_TYPE = {
        Auth: 1,
        ServerList: 2,
        GameServer: 3,
        MapServer: 4,
        LinkServer: 5,
        ServerListControl: 6
    }

    @classmethod
    def GetServerTypeId(cls, server_type):
        if server_type not in ServerType.__SERVER_TYPE:
            return False
        return cls.__SERVER_TYPE[server_type]

    @classmethod
    def GetServerTypeDesc(cls, server_id):
        if server_id == 1:
            return cls.Auth
        elif server_id == 2:
            return cls.ServerList
        elif server_id == 3:
            return cls.GameServer
        elif server_id == 4:
            return cls.MapServer
        elif server_id == 5:
            return cls.LinkServer
        elif server_id == 6:
            return cls.ServerListControl
        else:
            return "unknown"