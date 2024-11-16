from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
from bs4 import BeautifulSoup
import requests
import time
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 获取系统变量serverKey
serverKey = os.environ.get('serverKey')

cookie_json = os.environ.get('COOKIE')
# 获取 COOKIE 环境变量
# with open('cookies.json', 'r') as f:
#     cookie_json = f.read()

# 获取 COOKIE 环境变量并解析为 JSON 列表


if cookie_json:
    try:
        # 解析 JSON 字符串
        cookie_data = json.loads(cookie_json)
    except json.JSONDecodeError:
        print("错误：无法解析 COOKIE 环境变量为 JSON。")
else:
    print("错误：COOKIE 环境变量未设置。")

chrome_options = Options()
chrome_options.add_argument("--headless=new")  # 使用新版无头模式
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
# 添加以下选项来模拟真实浏览器
chrome_options.add_argument("--window-size=1920,1080")  # 设置窗口大小
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # 禁用自动化标志
chrome_options.add_argument("--disable-gpu")
# 添加 User-Agent
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")

# 添加其他选项
prefs = {
    "profile.default_content_setting_values.notifications": 2,  # 禁用通知
    "credentials_enable_service": False,  # 禁用保存密码提示
    "profile.password_manager_enabled": False
}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])  # 禁用自动化提示
chrome_options.add_experimental_option('useAutomationExtension', False)

web = webdriver.Chrome(options=chrome_options)

def Lingqu():
    try:
        # 切换到进行中的任务
        web.find_element(By.XPATH, '//*[@id="main"]/table/tbody/tr/td[1]/div[2]/table/tbody/tr[3]/td').click()
        # 点击进行中的任务
        # 完成日常
        time.sleep(2)
        try:
            web.find_element(By.XPATH, '//*[@id="both_15"]/a/img').click()
            print('日常领取成功')
            # 用urlencode编码中文内容
            messagecontent = '日常领取成功'
            messagecontent = requests.utils.quote(messagecontent)
            # 通过server酱发送通知
            url = f"https://sctapi.ftqq.com/{serverKey}.send?title={messagecontent}&desp=messagecontent"

            payload={}
            headers = {
            'User-Agent': 'Apifox/1.0.0 (https://apifox.com)'
            }

            response = requests.request("GET", url, headers=headers, data=payload)
        except:
            print('日常领取失败')
            
            
        try:
            # 尝试点击周常,没有就跳了
            web.find_element(By.XPATH, '//*[@id="both_14"]/a/img').click()
            print('周常领取成功')
            # 用urlencode编码中文内容
            messagecontent = '周常领取成功'
            messagecontent = requests.utils.quote(messagecontent)
            # 通过server酱发送通知
            url = f"https://sctapi.ftqq.com/{serverKey}.send?title={messagecontent}&desp=messagecontent"

            payload={}
            headers = {
            'User-Agent': 'Apifox/1.0.0 (https://apifox.com)'
            }

            response = requests.request("GET", url, headers=headers, data=payload)

        except:
            pass


    except:
        # 用urlencode编码中文内容
        messagecontent = '日常领取失败'
        messagecontent = requests.utils.quote(messagecontent)

        # 通过server酱发送通知
        url = f"https://sctapi.ftqq.com/{serverKey}.send?title={messagecontent}&desp=messagecontent"

        payload={}
        headers = {
        'User-Agent': 'Apifox/1.0.0 (https://apifox.com)'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        print('日常暂未刷新或领取失败')








url = 'https://www.south-plus.net/plugin.php?H_name-tasks.html.html'
web.get(url)
time.sleep(1)
# 保存cookies为json格式
# cookies = web.get_cookies()
# print(cookies)
# with open('cookies.json', 'w') as f:
#     json.dump(cookies, f)


# 将cookies添加到webdriver中   
for cookie in cookie_data:
    web.add_cookie(cookie)

# 重新加载页面
web.refresh()
# 截图当前页面
WebDriverWait(web, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="p_15"]')))
# 领取周常
try:  
    # 添加显式等待，确保元素可点击
    WebDriverWait(web, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="p_15"]/a/img'))
    )
    try:
        web.find_element(By.XPATH, '//*[@id="p_15"]/a/img').click()
        print('周常领取成功')
        web.find_element(By.XPATH, '//*[@id="p_14"]/a/img').click()
        print('日常领取成功')
        Lingqu()
    except:
        web.find_element(By.XPATH, '//*[@id="p_14"]/a/img').click()
        print('日常领取成功')
        Lingqu()


    
except Exception as e:
    print(f"发生错误: {str(e)}")






web.quit()
