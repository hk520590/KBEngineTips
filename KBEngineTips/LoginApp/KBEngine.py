#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File Created: 2019-03-22 19:08:07
# Author: Jacky (jackylvm@foxmail.com>)
# -----
# Last Modified: 2019-03-22 19:08:07
# Modified By: Jacky (jackylvm@foxmail.com>)
# -----
# Copyright 2018 上海火刀石网络科技有限公司
# -----
# HISTORY:
# Date      			By			Comments
# --------------------	---------	-------------------
#
# -----------------------------------------------------
# Loginapp进程主要负责处理实体的注册与登陆请求。
# 注意：该进程脚本实现在scripts/login目录中。

# ----------------服务器定义的常量--------------------------------------------
SERVER_SUCCESS = 0  # 成功。
SERVER_ERR_SRV_NO_READY = 1  # 服务器没有准备好。
SERVER_ERR_SRV_OVERLOAD = 2  # 服务器负载过重。
SERVER_ERR_ILLEGAL_LOGIN = 3  # 非法登录。
SERVER_ERR_NAME_PASSWORD = 4  # 用户名或者密码不正确。
SERVER_ERR_NAME = 5  # 用户名不正确。
SERVER_ERR_PASSWORD = 6  # 密码不正确。
SERVER_ERR_ACCOUNT_CREATE_FAILED = 7  # 创建账号失败（已经存在一个相同的账号）。
SERVER_ERR_BUSY = 8  # 操作过于繁忙(例如：在服务器前一次请求未执行完毕的情况下连续N次创建账号)。
SERVER_ERR_ACCOUNT_LOGIN_ANOTHER = 9  # 当前账号在另一处登录了。
SERVER_ERR_ACCOUNT_IS_ONLINE = 10  # 你已经登录了，服务器拒绝再次登录。
SERVER_ERR_PROXY_DESTROYED = 11  # 与客户端关联的proxy在服务器上已经销毁。
SERVER_ERR_ENTITYDEFS_NOT_MATCH = 12  # entityDefs不匹配。
SERVER_ERR_IN_SHUTTINGDOWN = 13  # 服务器正在关闭中
SERVER_ERR_NAME_MAIL = 14  # email地址错误。
SERVER_ERR_ACCOUNT_LOCK = 15  # 账号被冻结。
SERVER_ERR_ACCOUNT_DEADLINE = 16  # 账号已过期。
SERVER_ERR_ACCOUNT_NOT_ACTIVATED = 17  # 账号未激活。
SERVER_ERR_VERSION_NOT_MATCH = 18  # 与服务端的版本不匹配。
SERVER_ERR_OP_FAILED = 19  # 操作失败。
SERVER_ERR_SRV_STARTING = 20  # 服务器正在启动中。
SERVER_ERR_ACCOUNT_REGISTER_NOT_AVAILABLE = 21  # 未开放账号注册功能。
SERVER_ERR_CANNOT_USE_MAIL = 22  # 不能使用email地址。
SERVER_ERR_NOT_FOUND_ACCOUNT = 23  # 找不到此账号。
SERVER_ERR_DB = 24  # 数据库错误(请检查dbmgr日志和DB)。
SERVER_ERR_USER1 = 25  # 用户自定义错误码1
SERVER_ERR_USER2 = 26  # 用户自定义错误码2
SERVER_ERR_USER3 = 27  # 用户自定义错误码3
SERVER_ERR_USER4 = 28  # 用户自定义错误码4
SERVER_ERR_USER5 = 29  # 用户自定义错误码5
SERVER_ERR_USER6 = 30  # 用户自定义错误码6
SERVER_ERR_USER7 = 31  # 用户自定义错误码7
SERVER_ERR_USER8 = 32  # 用户自定义错误码8
SERVER_ERR_USER9 = 33  # 用户自定义错误码9
SERVER_ERR_USER10 = 34  # 用户自定义错误码10
SERVER_ERR_LOCAL_PROCESSING = 35  # 本地处理，通常为某件事情不由第三方处理而是由KBE服务器处理
SERVER_ERR_ACCOUNT_RESET_PASSWORD_NOT_AVAILABLE = 36  # 未开放账号重置密码功能。
SERVER_ERR_ACCOUNT_LOGIN_ANOTHER_SERVER = 37  # 当前账号在其他服务器登陆了
SERVER_ERR_MAX = 38  # 请把这条放在所有错误的最后面，这本身不是一个错误标识，仅表示一共有多少条错误定义


# ----------------KBEngine模块的成员函数--------------------------------------
def addTimer(initialOffset, repeatOffset=0, callbackObj=None):
    """
    功能说明：
        注册一个定时器，定时器由回调函数callbackObj触发，回调函数将在"initialOffset"秒后被执行第1次，而后将每间隔"repeatOffset"秒执行1次。
        例子:
        # 这里是使用addTimer的一个例子
            import KBEngine

            # 增加一个定时器，5秒后执行第1次，而后每1秒执行1次，用户参数是9
            KBEngine.addTimer( 5, 1, onTimer_Callbackfun )

            # 增加一个定时器，1秒后执行，用户参数缺省是0
            KBEngine.addTimer( 1, onTimer_Callbackfun )

        def onTimer_Callbackfun( id ):
            print "onTimer_Callbackfun called: id %i" % ( id )
            # if 这是不断重复的定时器，当不再需要该定时器的时候，调用下面函数移除:
            #     KBEngine.delTimer( id )
    参数:
    :param initialOffset:float，指定定时器从注册到第一次回调的时间间隔（秒）。
    :param repeatOffset:float，指定第一次回调执行后每次执行的时间间隔（秒）。必须用函数delTimer移除定时器，否则它会一直重复下去。值小于等于0将被忽略。
    :param callbackObj:function，指定的回调函数对象。
    :return:integer，该函数返回timer的内部id，这个id可用于delTimer移除定时器。
    """
    pass


def delTimer(id):
    """
    功能说明：
        函数delTimer用于移除一个注册的定时器，移除后的定时器不再执行。只执行1次的定时器在执行回调后自动移除，不必要使用delTimer移除。如果delTimer函数使用一个无效的id（例如已经移除），将会产生错误。
        到KBEngine.addTimer参考定时器的一个使用例子。
    参数:
    :param id:integer，它指定要移除的定时器id。
    :return:
    """
    pass


def urlopen(url, callback=None, postData="", headers=None):
    """
    功能说明：
    这个脚本函数在提供对外HTTP/HTTPS异步请求。
    参数： url 有效的HTTP/HTTPS网址，字符串类型。
    callback 可选参数，带有请求执行结果的回调对象（比如说是一个函数）。这个回调带有5个参数：HTTP请求返回码（如：200)，返回的内容，返回的HTTP协议头，是否成功，请求的网址。
    声明样例：
        def onHttpCallback(httpcode, data, headers, success, url):
                print(httpcode, data, headers, success, url)
        如同上面的例子所示:
        httpcode:参数对应的就是“HTTP请求返回码”，这个结果集合参数是一个整形值。
        data:参数则是“返回的内容”，它是一个字符串。
        headers:参数是“服务器返回的HTTP协议头”，如：{"Content-Type": "application/x-www-form-urlencoded"}，它是一个字典。
        success:则对应了“执行是否成功”，当请求执行有错误时，为False，可以通过httpcode进一步判断错误信息。
        url:是“请求所用的网址。
    postData 可选参数，默认是GET方式请求服务器，如果需要POST方式请提供需要POST的内容，引擎将自动使用POST方式请求服务器，它是一个bytes。
    headers 可选参数，请求时使用的HTTP头，如：{"Content-Type": "application/x-www-form-urlencoded"}，它是一个字典。
    :param url:
    :param callback:
    :param postData:
    :param headers:
    :return:
    """


def onLoginAppReady():
    """
    功能说明：
        当前进程已经准备好的时候回调此函数。
        注意：该回调接口必须实现在入口模块(kbengine_defs.xml->entryScriptFile)中。
    :return:
    """
    pass


def onLoginAppShutDown():
    """
    功能说明：
        进程关闭会回调此函数。
        注意：该回调接口必须实现在入口模块(kbengine_defs.xml->entryScriptFile)中。
    :return:
    """
    pass


def onReuqestLogin(loginName, password, clientType, datas):
    """
    功能说明：
        客户端请求服务器登陆账号时回调。
        此处可以对用户登陆做一些管理控制，例如：
        利用该接口可以在此截断用户的登陆，将请求记录下来进行排队并返回一个错误码告诉客户端排队状态，客户端通过不断登陆从此处获得状态。
        注意：该回调接口必须实现在入口模块(kbengine_defs.xml->entryScriptFile)中。
    :param loginName::string，登陆时提交的账号名称。
    :param password::string，MD5密码。
    :param clientType::integer，客户端类型，客户端登陆时给出。
    :param datas::bytes，客户端请求时所附带的数据，可将数据转发第三方平台。
    :return:
        Tuple，返回值分别为（错误码，真实账号名，密码，客户端类别，客户端提交的数据datas），
        如果没有任何需要扩展修改的则通常返回值为毁掉传入的值（KBEngine.SERVER_SUCCESS, loginName, password, clientType, datas）。o
    """
    pass


def onLoginCallbackFromDB(loginName, accountName, errorno, datas):
    """
    功能说明：
        客户端请求服务器登陆账号后由dbmgr返回的回调。
        注意：该回调接口必须实现在入口模块(kbengine_defs.xml->entryScriptFile)中。
    :param loginName:string，登陆时提交的账号名称。
    :param accountName:string，真实的账号名称（由dbmgr处查询获得）。
    :param errorno:integer，错误码，如果非KBEngine.SERVER_SUCCESS则表示登陆失败。
    :param datas:bytes，可能是任何数据，例如：第三方平台返回的数据或者由dbmgr以及interfaces中处理登陆时返回的数据。
    :return:
    """
    pass


def onRequestCreateAccount(accountName, password, data):
    """
    功能说明：
        客户端请求服务器创建账号时回调。
        注意：该回调接口必须实现在入口模块(kbengine_defs.xml->entryScriptFile)中。
    :param accountName:string，客户端提交的账号名称。
    :param password:string，MD5密码。
    :param data:bytes，客户端请求时所附带的数据，可将数据转发第三方平台。
    :return:
        Tuple，返回值分别为（错误码，真实账号名，密码，客户端提交的数据datas），
        如果没有任何需要扩展修改的则通常返回值为毁掉传入的值（KBEngine.SERVER_SUCCESS, loginName, password, datas）。
    """
    pass


def onCreateAccountCallbackFromDB(accountName, errorno, datas):
    """
    功能说明：
        客户端请求服务器创建账号后由dbmgr返回的回调。
        注意：该回调接口必须实现在入口模块(kbengine_defs.xml->entryScriptFile)中。
    :param accountName:string，客户端提交的账号名称。
    :param errorno:integer，错误码，如果非KBEngine.SERVER_SUCCESS则表示登陆失败。
    :param datas:bytes，可能是任何数据，例如：第三方平台返回的数据或者由dbmgr以及interfaces中处理登陆时返回的数据。
    :return:
    """
    pass
