#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@file   error_code.py
@author Geffrey
@date   2021/4/8
@brief  
"""

class ErrorCode(object):
    # region 错误码定义
    Success = 0

    # region 通用错误[1, 100]
    NotFound = 1  # 未发现
    SignDismatch = 2  # 签名不匹配
    NotAllow = 3  # 不允许
    HttpRequestTimeOut = 4  # Http请求超时
    HttpResponseError = 5  # Http失败应答
    HttpResponseContentFormatError = 6  # Http应答内容格式非法
    # endregion

    # region GM[201, 400]
    NotMatchCmd = 201
    ErrParam = 202
    ExecuteFailed = 203
    TimeoutToSend = 204
    HttpResponseErr = 205
    RepeatedReq = 206
    UidHasBlocked = 207
    DeviceHasBlocked = 208
    GameRecordNotExist = 209
    GameRecordHasClosed = 210
    NotFoundServer = 211
    NotFoundServerType = 212
    RepeatedOp = 213
    ErrorServer = 214
    NotFoundRegion = 215
    ErrorServerType = 216

    # endregion

    UnknownError = -1
    # endregion
    
    @classmethod
    def GetErrorDesc(cls, errorCode, kwargs=None):
        errDesc = cls.__ErrorDescs.get(errorCode)
        if not errDesc:
            return cls.__ErrorDescs[cls.UnknownError]

        if kwargs:
            return errDesc.format(**kwargs)
        else:
            return errDesc
        
    # region 内部实现
    __ErrorDescs = {
        Success: 'Success',

        # region 通用错误[1, 100]
        NotFound: 'Not found',
        SignDismatch: 'Sign dismatch',
        NotAllow: 'Not allow',
        HttpRequestTimeOut: 'http request time out',
        HttpResponseError: 'http response failed, code{param}',
        HttpResponseContentFormatError: 'http response content format error',
        # endregion

        # region GM[201, 400]
        NotMatchCmd: 'Not Match cmd',
        ErrParam: "error param",
        ExecuteFailed: 'execute failed',
        TimeoutToSend: 'timeout to send',
        HttpResponseErr: 'httpResponse err',
        RepeatedReq: 'repeated req',
        UidHasBlocked: 'uid has blocked',
        DeviceHasBlocked: "device Has blocked",
        GameRecordNotExist: "game announce record not exist, err id",
        GameRecordHasClosed: "game announce record has closed",
        NotFoundServer: 'server not found',
        NotFoundServerType: 'server type not found',
        RepeatedOp: 'repeated operate',
        ErrorServer: 'error server, {param}',
        NotFoundRegion: 'region not found',
        ErrorServerType: 'error server type',
        # endregion

        UnknownError: 'Unknown error',
    }
    # endregion