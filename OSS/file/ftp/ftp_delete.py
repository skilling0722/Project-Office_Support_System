#-*- encoding: UTF-8 -*-

import ftplib
import os, time


def file_delete(filename, filepath2):
    ftp = ftplib.FTP()
    ftp.encoding='utf-8'
    
    ip = '52.78.146.225'
    port = 21

    login_id = "yeonwoo"
    login_pwd = '1234'

    filepath = "/home/yeonwoo"



    ftp.set_pasv(False)
    ftp.connect(ip, port)
    ftp.login(login_id, login_pwd)

    ftp.cwd(filepath)

    ftp.delete(filename)

    ftp.close()