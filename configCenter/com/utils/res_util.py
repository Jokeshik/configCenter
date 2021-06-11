# -*- coding: utf-8 -*-
"""
@file   res_util.py
@author blueuee
@date   2019/7/29
@brief:
        
"""
import json

from datetime import datetime, date, time

from django.core import serializers
from django.db.models import Model, QuerySet
from django.http import HttpResponse

from com.error_code import ErrorCode
# from multiselectfield.db.fields import MSFList


class RespJsonEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(o, date):
            return o.strftime('%Y-%m-%d')
        elif isinstance(o, time):
            return o.strftime('%H:%M:%S')
        # elif isinstance(o, MSFList):
        #     return str(o)
        else:
            return super().default(o)


class RespUtil(object):
    """返回工具类"""

    @classmethod
    def Res(cls, content=None, errorCode=ErrorCode.Success, errorCodeFmtArgs=None):
        """构造res"""
        return cls._BuildResJson(errorCode, content, errorCodeFmtArgs)

    @classmethod
    def GmRes(cls, content=None, errorCode=ErrorCode.Success, errorCodeFmtArgs=None):
        """构造GmRes"""
        return cls._BuildGmResJson(errorCode, content, errorCodeFmtArgs)

    @classmethod
    def Res_Success(cls):
        return cls._BuildResJson(ErrorCode.Success)

    @classmethod
    def Res_NotFound(cls):
        return cls._BuildResJson(ErrorCode.NotFound)

    @classmethod
    def Res_SingDismatch(cls):
        return cls._BuildResJson(ErrorCode.SignDismatch)

    @classmethod
    def Res_UnknownError(cls):
        return cls._BuildResJson(ErrorCode.UnknownError)

    # region 内部实现
    @classmethod
    def _BuildResJson(cls, errorCode, content=None, errorCodeFmtArgs=None):
        obj = {
            'code': errorCode,
            'msg': ErrorCode.GetErrorDesc(errorCode, errorCodeFmtArgs),
        }

        if content is not None:
            obj['content'] = content

        return HttpResponse(json.dumps(obj, separators=(',', ':'), cls=RespJsonEncoder), content_type='application/json')

    @classmethod
    def _BuildGmResJson(cls, errorCode, content=None, errorCodeFmtArgs=None):

        obj = {
            'result': 1 if errorCode == 0 else 0,
            'msg': ErrorCode.GetErrorDesc(errorCode, errorCodeFmtArgs),
        }

        if content is not None:
            obj['data'] = content

        return HttpResponse(json.dumps(obj, separators=(',', ':'), cls=RespJsonEncoder), content_type='application/json')
    # endregion
