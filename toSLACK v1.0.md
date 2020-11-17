#!pip install slacker
#!pip install Selenium             # 동적 웹페이지를 크롤링하기 위한 라이브러리
#!pip install beautifulsoup4        # 정적 웹페이지를 크롤링을 할 수 있는 라이브러리
#!apt-get update
#!apt install chromium-chromedriver
#!cp /usr/lib/chromium-browser/chromedriver /usr/bin # 유저 bin 에 저장하기 위해 path 정해주기

from google.colab import auth
auth.authenticate_user()
import gspread
from oauth2client.client import GoogleCredentials
import pandas as pd

gc = gspread.authorize(GoogleCredentials.get_application_default())
wb = gc.open_by_url('https://docs.google.com/spreadsheets/d/1ZEEbu0_kI9UxGbofKOb9YhBTkgYdqspxkAcQoZl_bnE/edit#gid=1591956893') # 엑셀 파일 링크(구글드라이브)

#------text 정렬 ------
pd.set_option('display.max_rows', 500)# 최대 줄 수 설정
pd.set_option('display.max_columns', 500)# 최대 열 수 설정
pd.set_option('display.width', 1000)# 표시할 가로의 길이
total_menu.style.set_properties(**{'text-align': 'vcenter'}) # text 가운데 정렬
total_menu = pd.DataFrame()
#----한식 추천 뽑기-----
sheet_k = wb.worksheet('korean')
data_k = pd.DataFrame(sheet_k.get_all_values(),)
data_k = data_k[1:(len(data_k)+1)]
ran_k = data_k.sample() 
total_menu = pd.concat([total_menu,ran_k]) # DataFrame 은 append가 아니라 concat으로 데이터를 합쳐야 한다.

#----중식 추천 뽑기-----
sheet_c = wb.worksheet('chinese')
data_c = pd.DataFrame(sheet_c.get_all_values(),)
data_c = data_c[1:(len(data_c)+1)]
ran_c = data_c.sample()
total_menu = pd.concat([total_menu,ran_c])
#----일식 추천 뽑기-----
sheet_j = wb.worksheet('japanese')
data_j = pd.DataFrame(sheet_j.get_all_values(),)
data_j = data_j[1:(len(data_j)+1)]
ran_j = data_j.sample()
total_menu = pd.concat([total_menu,ran_j])
#----분식 추천 뽑기-----
sheet_s = wb.worksheet('simple_meal')
data_s = pd.DataFrame(sheet_s.get_all_values(),)
data_s = data_s[1:(len(data_s)+1)]
ran_s = data_s.sample()
total_menu = pd.concat([total_menu,ran_s])
#----학원생 추천 뽑기-----
sheet_m = wb.worksheet('member')
data_m = pd.DataFrame(sheet_m.get_all_values(),)
data_m = data_m[1:(len(data_m)+1)]
ran_m = data_m.sample()
total_menu = pd.concat([total_menu,ran_m])

#-----index, columns 수정하기 -----
pd.set_option('display.max.colwidth', 70)
total_menu.columns = [ '식당','대표메뉴','별점','리뷰','주소','URL']
total_menu.index = ['1.한식 추천','2.중식 추천','3.일식 추천','4.분식 추천','5.학원생 추천']
show_total = total_menu[[ '식당','대표메뉴','별점','리뷰','주소','URL']]
show_tatal_str= str(show_total)

#-----슬랙 등록
import sys
sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver') # '시스템 path 등록을 해줬습니다' 이게 뭔말이야? 어떤 시스템에다가 경로를 등록해줬단 말인거지? : 크롬드라이버를 동적으로 이용하기 위한 조치
from slacker import Slacker

#----- 슬랙 인증 후 메시지 전송
print(show_tatal_str)
token = 'xoxb-1502504146866-1515151579825-mu1ZwhiDTC3q3vqwWpVud22m'
slack = Slacker(token)
msg = show_tatal_str
slack.chat.post_message('#lunch', msg, as_user=True)
