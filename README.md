# [python自动打包工具]()

## 该脚本基于python3版本
1、将工程的编译设备选成 Gemeric iOS Device
2、command + B编译
3、执行脚本文件

### 使用准备
1.进入蒲公英官网注册账号（需实名认证）
2.获取user_key/api_key(由蒲公英提供)
3.编译工具[pycharm下载地址](https://www.jetbrains.com/pycharm/)，[使用说明见](https://blog.csdn.net/abstract_js/article/details/71789782)

### 将脚本在pycharm中打开
1.需要安装对应的支持库（头文件中根据报错提示在设置中添加）[详情见](https://jingyan.baidu.com/article/93f9803f5dababe0e46f55fc.html)

### 使用前将project地址改成自己本地的
```
projectPath = '/Users/a123/Library/Developer/Xcode/DerivedData/Bizpower-bgykvcwhryczmhfqdpmqjzeclpus/Build/Products/Debug-iphoneos/Bizpower.app'

userKey = "在蒲公英查看"
apiKey = "在蒲公英查看"
```
### 执行main函数（等待网页自动跳出时完成）



