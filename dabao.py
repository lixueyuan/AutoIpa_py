#!/usr/bin/env python
#coding=utf-8
import os
import requests
import webbrowser
import subprocess
import shutil

#python3版本
#1、将工程的编译设备选成 Gemeric iOS Device
#2、command + B编译
#3、执行脚本文件
#以上步骤必须在使用之前编译一次，否则将出现代码不同步问题

#把projectPath改成自己本地的
projectPath = '/Users/a123/Library/Developer/Xcode/DerivedData/Bizpower-bgykvcwhryczmhfqdpmqjzeclpus/Build/Products/Debug-iphoneos/Bizpower.app'

#不用动
PayLoadPath = '/Users/a123/Desktop/Payload'
packBagPath = '/Users/a123/Desktop/ProgramBag'
openUrlPath = 'https://www.pgyer.com/manager/dashboard/app/40c633aa8dc0ba15191632860558825e'


#必要
userKey = "在蒲公英查看"
apiKey = "在蒲公英查看"

#上传蒲公英
def uploadIPA(IPAPath):
    if(IPAPath==''):
        print("\nipa包路径为空\n")
        return
    else:
        print("\n开始上传\n")
        url='http://www.pgyer.com/apiv1/app/upload'
        data={
            'uKey':userKey,
            '_api_key':apiKey,
            'installType':'2',
            'password':'',
            'updateDescription':""
        }
        files={'file':open(IPAPath,'rb')}
        r=requests.post(url,data=data,files=files)

def openDownloadUrl():
    print ("\n更新成功\n")
    webbrowser.open(openUrlPath,new=1,autoraise=True)


#编译打包流程（以下全是本地文件操作/手动也是这个步骤，将这个步骤留给机器）
def runPacage():
    subprocess.call(["rm","-rf",packBagPath])
    mkdir(PayLoadPath)
    subprocess.call(["cp","-r",projectPath,PayLoadPath])
    subprocess.call(["mkdir","-p",packBagPath])
    #将文件夹拷贝到packBagPath文件夹下
    subprocess.call(["cp","-r",PayLoadPath,packBagPath])
    subprocess.call(["rm","-rf",PayLoadPath])
    os.chdir(packBagPath)
    subprocess.call(["zip","-r","./Payload.zip","."])
    print ("\n完成\n")
    #将zip压缩文件改名为ipa格式（苹果包）
    subprocess.call(["mv","payload.zip","Payload.ipa"])
    subprocess.call(["rm","-rf","./Payload"])


#创建PayLoad文件夹（mkdir在本地终端是创建文件夹的意思，linux命令）
def mkdir(PayLoadPath):
    isExists = os.path.exists(PayLoadPath)
    if not isExists:
        os.makedirs(PayLoadPath)
        print(PayLoadPath + '创建成功')
        return True
    else:
        print (PayLoadPath + '目录已经存在')
        return False


if __name__ == '__main__':
    runPacage()
    uploadIPA('%s/Payload.ipa'%packBagPath)
    openDownloadUrl()
