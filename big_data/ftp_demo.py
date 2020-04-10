"""
 从 FTP 服务器获取文件
"""
import ftplib

ftp = ftplib.FTP('tgftp.nws.noaa.gov')
ftp.login()

# 连接上，可以用 ftp 队列列出并更改目录
ftp.cwd('data')
ftp.nlst()


if __name__ == '__main__':
    print('------------')