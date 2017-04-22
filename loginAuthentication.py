#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Jon Zhang
@contact: zj.fly100@gmail.com
@site:
@version: 2.0
@license:
@file: loginAuthentication.py
@time: 2017-3-7 12:28

function requirement:
    编写登陆接口
        输入用户名密码
        认证成功后显示欢迎信息
        输错三次后锁定
"""
import sys

def rewriteAccountFile(aFile,accountList):
    """
     update the error times of account
    :param aFile,accountList:
    :return:
    """
    writeAccountFile = open(aFile,'w')
    for i in range(len(accountList)):
        a,b,c = accountList[i]
        l = a + "\t" + b + "\t" + str(c) + "\n"
        writeAccountFile.write(l)
    writeAccountFile.close()
#If the account's password has been wrong for three time,the account is locking
def loginAuthentication(aFile,accountList):
    while True:
        inputName = input("Please input your username:").strip()
        if len(inputName) == 0 :
            continue
        aSignForPassword = 1
        while aSignForPassword:
            inputPassword = input("Please input your password:").strip()
            if len(inputPassword) != 0:
                aSignForPassword = 0
        for i in range(len(accountList)):
            if inputName == accountList[i][0]:
                if accountList[i][2] == "3":
                    #sys.exit("To many retry,The account [%s] is locked!"% inputName)
                    print("To many retries ,The account [%s] is locked!"% inputName)
                    return 0
                if inputPassword == accountList[i][1]:
                    accountList[i][2] = 0
                    rewriteAccountFile(aFile, accountList)
                    #sys.exit("Welcome to ***** system!")
                    print("Welcome to ***** system!")
                    return 1
                else:
                    accountList[i][2] = str(int(accountList[i][2]) + 1)
                    print("Your account or password is wrong! Please try again!")
                    rewriteAccountFile(aFile,accountList)
                    break
        else:
            print("There is no username [%s],please register!" % inputName)
            #Can write a  module of register
if __name__ == '__main__':
    accountFile = "account.txt"
    readAccountFile = open(accountFile)
    f = readAccountFile.readlines()
    makeAccountAsList = [[i.split()[0], i.split()[1], i.split()[2]] for i in f]
    readAccountFile.close()
    loginAuthentication(accountFile,makeAccountAsList)