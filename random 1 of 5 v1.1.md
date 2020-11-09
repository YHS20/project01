import pandas as pd
#crawled data 불러오기
#def korean_menu_randem ( ) :
lunch_filename= 'C:/myPyCode/first_project/lunch.xlsx'
import pandas as pd
random_menu_df = pd.DataFrame()
df_index = pd.DataFrame({'추천식당':['한식 추천','중식 추천','일식 추천','분식 추천','학원생 추천']})
dp_korean_menu_excel_read = pd.read_excel(lunch_filename,sheet_name=0,encoding = "cp949")
random_korean_menu = dp_korean_menu_excel_read.sample()
random_menu_df = random_menu_df.append(random_korean_menu, ignore_index = True)
#print(random_menu_df)
#random_menu_df.append(random_korean_menu) 랜덤으로 뽑은거 빈 dataframe 에 넣기

dp_chinese_menu_excel_read = pd.read_excel(lunch_filename,sheet_name=1,encoding = "cp949")
random_chinese_menu = dp_chinese_menu_excel_read.sample()
random_menu_df = random_menu_df.append(random_chinese_menu, ignore_index = True)

dp_japanese_menu_excel_read = pd.read_excel(lunch_filename,sheet_name=2,encoding = "cp949")
random_japanese_menu = dp_korean_menu_excel_read.sample()
random_menu_df = random_menu_df.append(random_japanese_menu, ignore_index = True)

dp_simple_meal_menu_excel_read = pd.read_excel(lunch_filename,sheet_name=3,encoding = "cp949")
random_simple_meal_menu = dp_simple_meal_menu_excel_read.sample()
random_menu_df = random_menu_df.append(random_simple_meal_menu, ignore_index = True)

dp_member_menu_excel_read = pd.read_excel(lunch_filename,sheet_name=4,encoding = "cp949")
random_member_menu = dp_member_menu_excel_read.sample()
random_menu_df = random_menu_df.append(random_member_menu, ignore_index = True)

#-----------인덱스를 수정해보자 ----------
#recomend_res = {'추천식당':['한식 추천','중식 추천','일식 추천','분식 추천','학원생 추천']}
#random_menu_df.set_index('추천식당')
#print(random_menu_df)
total_menu_df = df_index.join(random_menu_df)
total_menu_df.set_index('추천식당', inplace=True) # index 를 추천 식당 순서로 수정
print('오늘 점심메뉴 많이 고민 되시죠?\n',total_menu_df)

#-----------------인덱스를 수정해보자 --------------

choice_menu = input('1~5번중에 어떤 메뉴가 마음에 드시나요? 번호를 입력해주세요.')
choosen_res = random_menu_df.loc[int(choice_menu)][0:]
print(choosen_res[0],'을 선택하셨군요?\n학원에서 식당까지 가는 길을 알려드릴게요. 잠시만요')
search_res = choosen_res[0] # 추후 검색에 이용할 식당 상호명
search_ad = choosen_res['주소'] # 추후 검색에 이용할 주소

#------ 지도 보여주기-----
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome('c:/chromedriver.exe')
url = 'https://map.naver.com/v5/directions/14139877.295363877,4507130.702141138,%ED%94%8C%EB%A0%88%EC%9D%B4%EB%8D%B0%EC%9D%B4%ED%84%B0,1445764215,PLACE_POI/-/-/walk?c=14139868.3907171,4507084.3705823,18,0,0,0,dh'

driver.implicitly_wait(3)

driver.get(url)
search_ad_in_map = driver.find_element_by_xpath('//*[@id="directionGoal1"]').send_keys(search_ad,(Keys.ENTER))
button = driver.find_element_by_xpath('//*[@id="container"]/shrinkable-layout/div/directions-layout/directions-result/div[1]/directions-search-list/search-list/search-list-contents/perfect-scrollbar/div/div[1]/div/div/div/search-item-address/div/div[1]/button/span')
button.click()
#driver.find_element_by_button('div > btn.btn_direction.active').click()