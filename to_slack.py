#------ 처음 한 번 실행할 때는 설치해 줘야 하는 부분입니다.----- 반복 실행할 경우 건너뛰어도 됩니다. 
!pip install slacker
!pip install Selenium             # 동적 웹페이지를 크롤링하기 위한 라이브러리
!pip install beautifulsoup4        # 정적 웹페이지를 크롤링을 할 수 있는 라이브러리
!apt-get update
!apt install chromium-chromedriver
!cp /usr/lib/chromium-browser/chromedriver /usr/bin # 유저 bin 에 저장하기 위해 path 정해주기
#------------------------------------------------------------------------------------------------------

from google.colab import auth
auth.authenticate_user()
import gspread
from oauth2client.client import GoogleCredentials
import pandas as pd

gc = gspread.authorize(GoogleCredentials.get_application_default())
wb = gc.open_by_url('https://docs.google.com/spreadsheets/d/1ZEEbu0_kI9UxGbofKOb9YhBTkgYdqspxkAcQoZl_bnE/edit#gid=1591956893') # 엑셀 파일 링크(구글드라이브)

#------text 정렬 ------
total_menu = pd.DataFrame()
pd.set_option('display.max_rows', 500)# 최대 줄 수 설정
pd.set_option('display.max_columns', 500)# 최대 열 수 설정
pd.set_option('display.width', 1000)# 표시할 가로의 길이
total_menu.style.set_properties(**{'text-align': 'vcenter'}) # text 가운데 정렬

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
total_menu.columns = [ '식당','대표메뉴','별점','리뷰','주소','URL']
total_menu.index = ['1.한식 추천','2.중식 추천','3.일식 추천','4.분식 추천','5.학원생 추천']
show_total = total_menu[[ '식당','대표메뉴','별점','리뷰','주소','URL']]
print(show_total)

#-------식당명~ url 변수로 지정하기-----

bistro_name1 =show_total["식당"][0]
bistro_name2 =show_total["식당"][1]
bistro_name3 =show_total["식당"][2]
bistro_name4 =show_total["식당"][3]
bistro_name5 =show_total["식당"][4]

bistro_menu1 = show_total["대표메뉴"][0]
bistro_menu2 = show_total["대표메뉴"][1]
bistro_menu3 = show_total["대표메뉴"][2]
bistro_menu4 = show_total["대표메뉴"][3]
bistro_menu5 = show_total["대표메뉴"][4]

bistro_review1 = show_total["리뷰"][0]
bistro_review2 = show_total["리뷰"][1]
bistro_review3 = show_total["리뷰"][2]
bistro_review4 = show_total["리뷰"][3]
bistro_review5 = show_total["리뷰"][4]

bistro_star1 = show_total["별점"][0]
bistro_star2 = show_total["별점"][1]
bistro_star3 = show_total["별점"][2]
bistro_star4 = show_total["별점"][3]
bistro_star5 = show_total["별점"][4]

bistro_Anschrift1 = show_total["주소"][0]
bistro_Anschrift2 = show_total["주소"][1]
bistro_Anschrift3 = show_total["주소"][2]
bistro_Anschrift4 = show_total["주소"][3]
bistro_Anschrift5 = show_total["주소"][4]

bistro_url1 = show_total["URL"][0]
bistro_url2 = show_total["URL"][1]
bistro_url3 = show_total["URL"][2]
bistro_url4 = show_total["URL"][3]
bistro_url5 = show_total["URL"][4]

#-----슬랙 등록
import requests
import json

slack_webhook_url = "https://hooks.slack.com/services/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" # slack 에서 webhook을 체널에 등록해야하며, 등록하면서 해당 체널에서 사용할 webhook url을 얻어와야한다.

headers = {
    "Content-type": "application/json"
}

data = { #아래는 json 형식. 슬랙 api 페이지에 가면 다양하게 정형화된 json 형식의 파일들을 볼 수 있다. 참고하자.
	"blocks": [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*No Pain No Coding!*\n오늘 오전도 :star2:꿈:star2:을 위해 열심히 달려오신 여러분, 식사하러 가시죠!\n추천 링크는 아래에 걸어둘게요!:small_red_triangle_down:"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": ":kr:*1.한식 추천:{0}*\n{1} \n:star: {3}\n{2}\n주소:{4}".format(bistro_name1,bistro_menu1,bistro_review1,bistro_star1,bistro_Anschrift1)
			},
			"accessory": {
				"type": "image",
				"image_url": "https://s3-media3.fl.yelpcdn.com/bphoto/c7ed05m9lC2EmA3Aruue7A/o.jpg",
				"alt_text": "alt text for image"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*:cn:2.중식 추천:{0}*\n{1} \n:star: {3}\n{2}\n주소:{4}".format(bistro_name2,bistro_menu2,bistro_review2,bistro_star2,bistro_Anschrift2)
			},
			"accessory": {
				"type": "image",
				"image_url": "https://s3-media2.fl.yelpcdn.com/bphoto/korel-1YjNtFtJlMTaC26A/o.jpg",
				"alt_text": "alt text for image"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*:flag-jp:3.일식 추천:{0}*\n{1} \n:star: {3}\n{2}\n주소:{4}".format(bistro_name3,bistro_menu3,bistro_review3,bistro_star3,bistro_Anschrift3)
			},
			"accessory": {
				"type": "image",
				"image_url": "https://s3-media2.fl.yelpcdn.com/bphoto/DawwNigKJ2ckPeDeDM7jAg/o.jpg",
				"alt_text": "alt text for image"
			}
		},
    {
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*:ramen:4.분식 추천:{0}*\n{1} \n:star: {3}\n{2}\n주소:{4}".format(bistro_name4,bistro_menu4,bistro_review4,bistro_star4,bistro_Anschrift4)
			},
			"accessory": {
				"type": "image",
				"image_url": "https://s3-media2.fl.yelpcdn.com/bphoto/DawwNigKJ2ckPeDeDM7jAg/o.jpg",
				"alt_text": "alt text for image"
			}
		},
    {
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*:school:5.학원생 추천:{0}*\n{1} \n:star: {3}\n{2}\n주소:{4}".format(bistro_name5,bistro_menu5,bistro_review5,bistro_star5,bistro_Anschrift5)
			},
			"accessory": {
				"type": "image",
				"image_url": "https://s3-media2.fl.yelpcdn.com/bphoto/DawwNigKJ2ckPeDeDM7jAg/o.jpg",
				"alt_text": "alt text for image"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "{0}".format(bistro_name1),
					},
					"value": "click_me_123",
          "url": "{0}".format(bistro_url1)
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "{0}".format(bistro_name2),
					},
					"value": "click_me_123",
     			"url": "{0}".format(bistro_url2)

				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "{0}".format(bistro_name3),

					},
					"value": "click_me_123",
          "url": "https://google.com",
          "url": "{0}".format(bistro_url3)
				},
        {
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "{0}".format(bistro_name4),
					},
					"value": "click_me_123",
          "url": "{0}".format(bistro_url4)
				},
        {
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "{0}".format(bistro_name5),
					},
					"value": "click_me_123",
          "url": "{0}".format(bistro_url5)
				}
        
			]
		}
	]
}

res = requests.post(slack_webhook_url, headers=headers, data=json.dumps(data)) # json 형식으로 보내기 위해서 이와 같은 형식의 함수를 사용 
print(res.status_code)