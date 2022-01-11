from urllib.request import urlopen
import json, csv

def getSpotsData (apiUrl):
  with urlopen(apiUrl) as res:
    # 取得 JSON 是哪個編碼 (這邊是 'utf-8')
    encoding = res.headers.get_content_charset()
    jsonData = json.loads(res.read().decode(encoding))
    return jsonData['result']['results']

def getThumbnail (fileUrls):
  fileUrlList = list(map(lambda x: 'https://' + x, fileUrls.split('https://')))[1:]
  return fileUrlList[0]

def getDistrict (address):
  return address[5:8]

def generateSpotsCsv (spots):
  with open('data.csv', 'w', newline='', encoding='utf8') as csvData:
    csvFile = csv.writer(csvData)
    for spot in spots:
      # 景點名稱, 區域, 經度, 緯度, 第一張圖檔網址
      csvFile.writerow([spot['stitle'], getDistrict(spot['address']), spot['longitude'], spot['latitude'], getThumbnail(spot['file'])])

apiUrl = 'https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json'
spots = getSpotsData(apiUrl)
generateSpotsCsv(spots)