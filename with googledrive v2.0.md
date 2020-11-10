from google.colab import auth
auth.authenticate_user()
import gspread
from oauth2client.client import GoogleCredentials
import pandas as pd

gc = gspread.authorize(GoogleCredentials.get_application_default())

wb = gc.open_by_url('https://docs.google.com/spreadsheets/d/1ZEEbu0_kI9UxGbofKOb9YhBTkgYdqspxkAcQoZl_bnE/edit#gid=1591956893') # 해당 엑셀 파일에서 바로 가져온 url

#------랜덤으로 메뉴 하나씩 뽑아오자 ------
total_menu = []
#----한식 뽑기-----
sheet_k = wb.worksheet('korean')
data_k = pd.DataFrame(sheet_k.get_all_values(),)
ran_k = data_k.sample()
total_menu.append(ran_k)

#----중식 뽑기-----
sheet_c = wb.worksheet('chinese')
data_c = pd.DataFrame(sheet_c.get_all_values(),)
ran_c = data_c.sample()
total_menu.append(ran_c)
#----일식 뽑기-----
sheet_j = wb.worksheet('japanese')
data_j = pd.DataFrame(sheet_j.get_all_values(),)
ran_j = data_j.sample()
total_menu.append(ran_j)
#----분식 뽑기-----
sheet_s = wb.worksheet('simple_meal')
data_s = pd.DataFrame(sheet_s.get_all_values(),)
ran_s = data_s.sample()
total_menu.append(ran_s)
#----학원생 추천 뽑기-----
sheet_m = wb.worksheet('member')
data_m = pd.DataFrame(sheet_m.get_all_values(),)
ran_m = data_m.sample()
total_menu.append(ran_m)
print(total_menu)
#---- 랜덤으로 뽑은 메뉴 하나로 합치기

lunch_columns = ['식당이름','대표 메뉴','평점','리뷰','주소']
#lunch_index = []
