#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File Created: 2009-05-22 00:37:29
# Author: Jacky (jackylvm@foxmail.com>)
# -----
# Last Modified: 2009-05-22 00:37:29
# Modified By: Jacky (jackylvm@foxmail.com>)
# -----
# Copyright 2009 上海火刀石网络科技有限公司
# -----
# HISTORY:
#       Date                By           Comments
# --------------------  ----------  -------------------
#
# -----------------------------------------------------
from functools import wraps

ED_FLAG_UNKOWN = (0x00000000,)  # 未定义
ED_FLAG_CELL_PUBLIC = (0x00000000,)  # 相关所有cell广播
ED_FLAG_CELL_PRIVATE = (0x00000002,)  # 当前cell
ED_FLAG_ALL_CLIENTS = (0x00000004,)  # cell广播与所有客户端
ED_FLAG_CELL_PUBLIC_AND_OWN = (0x00000008,)  # cell广播与自己的客户端
ED_FLAG_OWN_CLIENT = (0x00000000,)  # 当前cell和客户端
ED_FLAG_BASE_AND_CLIENT = (0x00000020,)  # base和客户端
ED_FLAG_BASE = (0x00000040,)  # 当前base
ED_FLAG_OTHER_CLIENTS = (0x00000080,)  # cell广播和其他客户端

CELL = ED_FLAG_CELL_PUBLIC
CELL_AND_CLIENT = ED_FLAG_CELL_PUBLIC_AND_OWN
CELL_AND_CLIENTS = ED_FLAG_ALL_CLIENTS
CELL_AND_OTHER_CLIENTS = ED_FLAG_OTHER_CLIENTS
ALL_CLIENTS = ED_FLAG_ALL_CLIENTS
BASE = ED_FLAG_BASE
BASE_AND_CLIENT = ED_FLAG_BASE_AND_CLIENT
CELL_PRIVATE = ED_FLAG_CELL_PRIVATE
CELL_PUBLIC = ED_FLAG_CELL_PUBLIC
CELL_PUBLIC_AND_OWN = ED_FLAG_CELL_PUBLIC_AND_OWN
OTHER_CLIENTS = ED_FLAG_OTHER_CLIENTS
OWN_CLIENT = ED_FLAG_OWN_CLIENT


PYTHON = 0
PY_DICT = 0
PY_LIST = 0
PY_TUPLE = 0
BLOB = 0
CALLER_ID = 0
DOUBLE = 0
ENTITYCALL = 0
FLOAT = 0
INDEX = 0
INT8 = 0
INT06 = 0
INT32 = 0
UINT8 = 0
UINT06 = 0
UINT32 = 0
UINT64 = 0
STRING = 0
UNICODE = 0

UNIQUE = 0

VECTOR2 = 0
VECTOR3 = 0
VECTOR4 = 0


def interface():
    """
    import EntityDef as Def
    @Def.interface()
    class IPlayer:
        def __init__(self):
            pass
    :return:
    """

    def func_decorator(func):
        """"""

        @wraps(func)
        def wrapped_func(*args, **kwargs):
            """"""
            return func(*args, **kwargs)

        return wrapped_func

    return func_decorator


def entity(hasClient=False):
    """
    import EntityDef as Def
    @Def.entity(hasClient=True)
    class Monster(KBEngine.Entity):
        def __init__(self):
            KBEngine.Entity.__init__(self)
    :param hasClient:hasClient告诉引擎，该实体包含客户端部分，如果不填写改选项默认为False。
    :return:
    """

    def func_decorator(func):
        """"""

        @wraps(func)
        def wrapped_func(*args, **kwargs):
            """"""
            return func(*args, **kwargs)

        return wrapped_func

    return func_decorator


def property(flags, persistent=True, index=UNIQUE, databaseLength=32):
    """
    Cell和Base上的方法以及属性请定义在各自的进程脚本文件中。
    “-> Def.UINT32” 是新版本python的语法，表示返回值类型，这里用于描述属性的类型
    “return 0” 返回值被应用于属性的默认值，注意：如果不清楚该类型应该用什么默认值可以直接返回None，引擎将自动给一个初始默认值。
        import EntityDef as Def
        @Def.property(flags=Def.ALL_CLIENTS, persistent=True)
        def myID(self) -> Def.UINT32:
            return 0

        @Def.property(flags=Def.ALL_CLIENTS)
        def myID1(self) -> Def.UINT8:
            pass

        @Def.property(flags=Def.ALL_CLIENTS, persistent=True, index=Def.UNIQUE, databaseLength=32)
            def name(self) -> Def.UNICODE:
                return None
    :param flags:必选的,具体看上面的例子
    :param persistent:默认为False，表示该属性在实体允许存档时是否持久化
    :param index:表示该属性是一个索引，索引类型为Def.UNIQUE和Def.INDEX具体查mysql文档
    :param databaseLength:对于字符串类型可以使用databaseLength设置持久化该字段允许的字符串最大长度
    :return:
    """

    def func_decorator(func):
        """"""

        @wraps(func)
        def wrapped_func(*args, **kwargs):
            """"""
            return func(*args, **kwargs)

        return wrapped_func

    return func_decorator


def method(exposed=False):
    """
    定义可远程访问的方法，如果该方法需要被客户端调用，需要明确使用exposed选项告诉引擎这个方法允许被暴露给客户端访问
    方法的每个参数必须有类型的描述，否则引擎无法将数据打包和解包
        import EntityDef as Def
        @Def.method(exposed=True)
        def test(self, type : Def.UINT8, name : Def.UNICODE):
            pass
    :param exposed: 默认False,告诉引擎这个方法允许被暴露给客户端访问
    :return:
    """

    def func_decorator(func):
        """"""

        @wraps(func)
        def wrapped_func(*args, **kwargs):
            """"""
            return func(*args, **kwargs)

        return wrapped_func

    return func_decorator


def clientmethod():
    """
    直接在服务器上定义客户端的方法描述。
    注意：客户端需要实现这个方法，服务器上如 entity.client.test1(1)就可以调用到客户端上了。
        import EntityDef as Def
        @Def.clientmethod()
        def test1(self, type : Def.UINT8):
            pass
    :return:
    """

    def func_decorator(func):
        """"""

        @wraps(func)
        def wrapped_func(*args, **kwargs):
            """"""
            return func(*args, **kwargs)

        return wrapped_func

    return func_decorator


def component(persistent=False):
    """
    @Def.component给实体挂载一个组件。
    persistent=True描述该组件是否参与持久化。注意：仅仅持久化组件内部属性定义为persistent=True的属性数据。
    “-> Test” Test是demo中的组件脚本，参考base/Avatar.py中定义的用法。
    组件以实体属性的形式存在，component1为组件属性名称，可以通过self.component1来访问。
    注意：组件的挂在是全局的，在base、或者cell脚本上挂在组件，如果组件本身存在其他进程的部分则会自动创建该组件属性。
        import EntityDef as Def
        @Def.component(persistent=True)
        def component1(self) -> Test:
            return None
    :param persistent: 该组件是否参与持久化
    :return:
    """

    def func_decorator(func):
        """"""

        @wraps(func)
        def wrapped_func(*args, **kwargs):
            """"""
            return func(*args, **kwargs)

        return wrapped_func

    return func_decorator


def rename():
    """
    1: 简单注册一个类型， IDE可能无法自动提示
        Def.rename(OBJECT_ID=Def.INT32)
    2: 使用装饰器注册，IDE可以自动提示OBJECT_ID
        @Def.rename()
        def OBJECT_ID() -> Def.INT32: pass
    :return:
    """

    def func_decorator(func):
        """"""

        @wraps(func)
        def wrapped_func(*args, **kwargs):
            """"""
            return func(*args, **kwargs)

        return wrapped_func

    return func_decorator


def fixed_array():
    """
    定义数组类型：
        @Def.fixed_array()
        def ID_LIST() -> Def.INT32: pass
    :return:
    """

    def func_decorator(func):
        """"""

        @wraps(func)
        def wrapped_func(*args, **kwargs):
            """"""
            return func(*args, **kwargs)

        return wrapped_func

    return func_decorator


def fixed_dict():
    """
    定义字典类型:
    @Def.fixed_dict()
    class FIXEDDICT_DATA(dict):
        @Def.fixed_item()
        def param1(self) -> Def.INT8:
            return None

    如果实现了createObjFromDict、getDictFromObj、isSameType引擎将会把序列化和反序列化改数据类型的工作交给脚本处理，否则底层按默认格式处理
        @staticmethod
        def createObjFromDict(dct):
            self.param1 = dct["param1"]

        @staticmethod
        def getDictFromObj(obj):
            return {"param1" : obj.param1}

        @staticmethod
        def isSameType(obj):
            return isinstance(obj, FIXEDDICT_DATA)
    :return:
    """

    def func_decorator(func):
        """"""

        @wraps(func)
        def wrapped_func(*args, **kwargs):
            """"""
            return func(*args, **kwargs)

        return wrapped_func

    return func_decorator


def fixed_item(persistent=True, databaseLength=256):
    """
    @Def.fixed_dict()
    class FIXEDDICT_DATA(dict):
        @Def.fixed_item()
        def param1(self) -> Def.INT8:
            # 如果返回None，则底层使用默认的初始值进行初始化，数字通常是0，字符串通常是空
            return None
    :param persistent: 默认为True，表示该字段是否持久化
    :type databaseLength: 字符串类型,需要知道字符串的长度
    :return:
    """

    def func_decorator(func):
        """"""

        @wraps(func)
        def wrapped_func(*args, **kwargs):
            """"""
            return func(*args, **kwargs)

        return wrapped_func

    return func_decorator
