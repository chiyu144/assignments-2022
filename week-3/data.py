from urllib.request import urlopen
import json, csv

def get_spots_data (api_url):
  with urlopen(api_url) as res:
    # 取得 JSON 是哪個編碼 (這邊是 'utf-8')
    encoding = res.headers.get_content_charset()
    json_data = json.loads(res.read().decode(encoding))
    return json_data['result']['results']

def get_thumbnail (file_urls):
  file_url_list = list(map(lambda x: 'https://' + x, file_urls.split('https://')))[1:]
  return file_url_list[0]

def get_district (address):
  return address[5:8]

def generate_spots_csv (spots):
  with open('data.csv', 'w', newline='', encoding='utf-8') as csv_data:
    csv_file = csv.writer(csv_data)
    for spot in spots:
      # 景點名稱, 區域, 經度, 緯度, 第一張圖檔網址
      csv_file.writerow([spot['stitle'], get_district(spot['address']), spot['longitude'], spot['latitude'], get_thumbnail(spot['file'])])

api_url = 'https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json'
spots = get_spots_data(api_url)
generate_spots_csv(spots)