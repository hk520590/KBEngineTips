##KBEngine在IDE里面的自动完成和提示功能

### 介绍

KBEngine的Python脚本API在IDE里面无法自动完成

这个项目实现KBEngineAPI的python版本,实现在IDE里面能够正确的自动完成

该项目Fork自[KBEngine-Python-Tips](https://github.com/likecg2010/KBEngine-Python-Tips)项目

最新内容按照KBEngine1.1.8的API提供

### 使用方法

使用时,把KBEngineTips文件夹拷贝到python安装目录的Lib文件夹里面

在需要使用的地方按照下面的方式导入模块

在base上

		try:
		    import KBEngine
		except ImportError as e:
    		# 这里这样做就是为了编码方便
    		# 实际代码运行的时候是不会走到这里的
    		from KBEngineTips.BaseApp import KBEngine

在cell上

		try:
		    import KBEngine
		except ImportError as e:
    		# 这里这样做就是为了编码方便
    		# 实际代码运行的时候是不会走到这里的
    		from KBEngineTips.CellApp import KBEngine

其他模块上按照上述方法使用

这样做的原理是:

1. 在编辑文件夹的时候,因为没有KBEngine模块,所以import KBEngine会出错,就是使用下面的from导入KBEngine

2. 在程序执行时,import KBEngine会执行成功,所以不会执行下面的from语句\


####该方法在Pycharm上测试成功,其他IDE没有测试 

