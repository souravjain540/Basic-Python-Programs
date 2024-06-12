'''
    Program Title: A program to check the internet upload and download speed with python

    To run this program, to check the internet speed we use the speedtest module. 
    To install this package use pip install speedtest-cli syntax.

'''

import speedtest
speed = speedtest.Speedtest()
download_speed = speed.download()
upload_speed = speed.upload()
print(f'The download speed is {download_speed}')
print(f'The uplaod speed is {upload_speed}')                                          