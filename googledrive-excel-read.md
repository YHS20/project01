#-----교수님이 도와주신거다. 정확한 코드는 따로 공부해서 익혀두자.
from google.colab import auth
auth.authenticate_user()
import gspread
from oauth2client.client import GoogleCredentials
import pandas as pd

gc = gspread.authorize(GoogleCredentials.get_application_default())

wb = gc.open_by_url('https://docs.google.com/spreadsheets/d/1htC_zBLWXdmDIhhkZ64kpP8DIJXV2a0jFz0tJgnFA9E/edit#gid=0') # 해당 엑셀 파일에서 바로 가져온 url

sheet = wb.worksheet('Sheet1')
data = sheet.get_all_values()
df = pd.DataFrame(data)
df.columns = df.iloc[0]
df = df.iloc[1:]
df