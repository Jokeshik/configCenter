#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@file   settingdb_router.py
@author Geffrey
@date   2021/4/14
@brief  
"""

from configCenter.settings import DATABASE_ROUTER_MAPPING

class SettingDBRouter(object):
    """设置数据库Router"""

    def db_for_read(self, model, **hints):
        """"Point all read operations to the specific database."""
        if model._meta.app_label in DATABASE_ROUTER_MAPPING:
            return DATABASE_ROUTER_MAPPING[model._meta.app_label]
        return None

    def db_for_write(self, model, **hints):
        """Point all write operations to the specific database."""
        if model._meta.app_label in DATABASE_ROUTER_MAPPING:
            return DATABASE_ROUTER_MAPPING[model._meta.app_label]
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """Allow any relation between apps that use the same database."""
        db_obj1 = DATABASE_ROUTER_MAPPING.get(obj1._meta.app_label)
        db_obj2 = DATABASE_ROUTER_MAPPING.get(obj2._meta.app_label)
        if db_obj1 and db_obj2:
            if db_obj1 == db_obj2:
                return True
            else:
                return False
        return None

    def allow_syncdb(self, db, model):
        """Make sure that apps only appear in the related database."""

        if db in DATABASE_ROUTER_MAPPING.values():
            return DATABASE_ROUTER_MAPPING.get(model._meta.app_label) == db
        elif model._meta.app_label in DATABASE_ROUTER_MAPPING:
            return False
        return None

    def allow_migrate(self, db, app_label, model=None, **hints):
        """
        Make sure the auth app only appears in the 'auth_db'
        database.
        """
        if db in DATABASE_ROUTER_MAPPING.values():
            return DATABASE_ROUTER_MAPPING.get(app_label) == db
        elif app_label in DATABASE_ROUTER_MAPPING:
            return False
        return None