# ----------- 가는 길, 도보 걸리는 시간 알려주기 -----------
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome('c:/chromedriver.exe')
url = 'https://map.naver.com/v5/directions/14139877.295363877,4507130.702141138,%ED%94%8C%EB%A0%88%EC%9D%B4%EB%8D%B0%EC%9D%B4%ED%84%B0,1445764215,PLACE_POI/-/-/walk?c=14139868.3907171,4507084.3705823,18,0,0,0,dh'

driver.implicitly_wait(3)
search_ad = '서울 서초구 효령로 314 1층'
#search_ad = '서울 서초구 남부순환로339길 60'
driver.get(url)
search_ad_in_map = driver.find_element_by_xpath('//*[@id="directionGoal1"]').send_keys(search_ad,(Keys.ENTER))
button = driver.find_element_by_xpath('//*[@id="container"]/shrinkable-layout/div/directions-layout/directions-result/div[1]/directions-search-list/search-list/search-list-contents/perfect-scrollbar/div/div[1]/div/div/div/search-item-address/div/div[1]/button/span')
button.click()
driver.find_element_by_xpath('//*[@id="container"]/shrinkable-layout/div/directions-layout/directions-result/div[1]/directions-summary-list/directions-hover-scroll/div/div/directions-summary-item-walking/div[3]/button').click()

#driver.find_element_by_button('div > btn.btn_direction.active').click() # 가는 길 상세하게 보여주기