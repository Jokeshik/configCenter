# -*- coding: utf-8 -*-
"""
@file   crypter.py
@author blueuee
@date   2019/7/29
@brief:
        
"""
import hashlib
import hmac
import urllib.parse


class SignUtil(object):
    """签名验证工具"""
    HMAC_SHA1 = 1
    HMAC_SHA256 = 2
    HMAC_MD5 = 3
    MD5 = 4

    @classmethod
    def Sign(cls, msg, signKey, algo=MD5):
        """执行签名"""
        if algo == cls.MD5:
            msg = msg.encode('utf-8') + b'&' + signKey
            return hashlib.md5(msg).hexdigest()
        else:
            hashAlgo = hashlib.sha256 if algo == cls.HMAC_SHA256 else \
                (hashlib.sha1 if algo == cls.HMAC_SHA1 else cls.HMAC_MD5)
            return hmac.new(signKey, msg, hashAlgo).hexdigest()

    @classmethod
    def GmSign(cls, msg, signKey):
        msg = msg.encode('utf-8') + signKey
        return hashlib.md5(msg).hexdigest()

    @classmethod
    def ValidateRequestSign(cls,
                            contentObj,
                            signKey,
                            algo=MD5,
                            excludeFields=None,
                            needQuote=False,
                            quoteMeth=urllib.parse.quote_plus,
                            signFieldName='sign'):
        """验证请求签名"""
        keys = [key for key in contentObj.keys() if key != signFieldName and key not in (excludeFields or ())]
        keys.sort()

        willSign = ''
        for key in keys:
            if willSign:
                willSign += '&'
            willSign += '{}={}'.format(key, cls._GetFieldValue(contentObj, key, needQuote, quoteMeth))

        calcSign = cls.Sign(willSign, signKey, algo)
        return calcSign == contentObj[signFieldName], contentObj[signFieldName], calcSign

    # region 内部实现
    @staticmethod
    def _GetFieldValue(contentObj, key, needQuote, quoteMeth):
        value = contentObj[key]
        if not needQuote:
            return value

        return quoteMeth(value)
    # endregion
