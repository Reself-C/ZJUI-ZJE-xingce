from selenium import webdriver
from configs import parse_args
import time
from datetime import datetime

def run(args):
    driver = webdriver.Chrome()
    driver.get(args.url)
    time.sleep(1)
    
    # 姓名
    driver.find_element_by_id('q1').clear()
    driver.find_element_by_id('q1').send_keys(args.name)
    
    # 学号
    driver.find_element_by_id('q2').clear()
    driver.find_element_by_id('q2').send_keys(args.id)
    
    # 手机号
    driver.find_element_by_id('q3').clear()
    driver.find_element_by_id('q3').send_keys(args.phone)
    
    # 单位
    if args.loc == 'ZJUI':
        driver.find_element_by_id('q4_1').click()
    elif args.loc == 'ZJE':
        driver.find_element_by_id('q4_0').click()
        
    # 年级
    if args.grade == '2018':
        driver.find_element_by_id('q5_0').click()
    elif args.grade == '2019':
        driver.find_element_by_id('q5_1').click()
    elif args.grade == '2020':
        driver.find_element_by_id('q5_2').click()
    elif args.grade == '2021':
        driver.find_element_by_id('q5_3').click()

    driver.find_element_by_id('submitbutton').click()
    driver.close()
    driver.quit()

if __name__ == '__main__':
    args = parse_args()
    print(args)
    while True:
        now = datetime.now()
        if args.hr == now.hour and args.min == now.minute:
            run(args)
        time.sleep(15)