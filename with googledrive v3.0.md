from google.colab import auth
auth.authenticate_user()
import gspread
from oauth2client.client import GoogleCredentials
import pandas as pd

gc = gspread.authorize(GoogleCredentials.get_application_default())

wb = gc.open_by_url('https://docs.google.com/spreadsheets/d/1ZEEbu0_kI9UxGbofKOb9YhBTkgYdqspxkAcQoZl_bnE/edit#gid=1591956893') # 해당 엑셀 파일에서 바로 가져온 url

#------랜덤으로 메뉴 하나씩 뽑아오자 ------
total_menu = pd.DataFrame()
#----한식 뽑기-----
sheet_k = wb.worksheet('korean')
data_k = pd.DataFrame(sheet_k.get_all_values(),)
data_k = data_k[1:(len(data_k)+1)]
ran_k = data_k.sample() # 외 수를 불러오는지 모르겠네.
total_menu = pd.concat([total_menu,ran_k]) # DataFrame 은 append가 아니라 concat으로 데이터를 합쳐야 한다.


#----중식 뽑기-----
sheet_c = wb.worksheet('chinese')
data_c = pd.DataFrame(sheet_c.get_all_values(),)
data_c = data_c[1:(len(data_c)+1)]
ran_c = data_c.sample()

total_menu = pd.concat([total_menu,ran_c])
#----일식 뽑기-----
sheet_j = wb.worksheet('japanese')
data_j = pd.DataFrame(sheet_j.get_all_values(),)
data_j = data_j[1:(len(data_j)+1)]
ran_j = data_j.sample()
total_menu = pd.concat([total_menu,ran_j])
#----분식 뽑기-----
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

#---- index, columns 수정하기 -----
total_menu.columns = [ '식당','대표메뉴','별점','리뷰','주소']
total_menu.index = ['1.한식 추천','2.중식 추천','3.일식 추천','4.분식 추천','5.학원생 추천']

print(total_menu)
#------ 메뉴 선택하기 ------
choice_menu_num = input('1~5번중에 어떤 메뉴가 마음에 드시나요? 번호를 입력해주세요.') # 5개의 식당중 하나 선택하기
choosen_res_all = total_menu.iloc[int(choice_menu_num)] # 가고자 하는 식당의 5가지 정보
choosen_res_name = total_menu.iloc[int(choice_menu_num)][0] # 가고자하는 식당 이름 출력

#---- 사용자가 보게 될 text -----
print(choosen_res_name,'을 선택하셨군요?\n학원에서 {0}까지 가는 길을 알려드릴게요. 잠시만요'.format(choosen_res_name))


