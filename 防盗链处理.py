# 爬取梨视频中的video
# 真实连接：     https://video.pearvideo.com/mp4/adshort/20190215/cont-1517776-13583811_adpkg-ad_hd.mp4
# 可以获取的链接：https://video.pearvideo.com/mp4/adshort/20190215/1667881163822-13583811_adpkg-ad_hd.mp4
import requests

url = 'https://www.pearvideo.com/video_1516005'

# 1.获取contId
contId = url.split('_')[1]

# 2.将获取的contId拼接到获取srcUrl链接中获取srcURL
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "Referer": url
}
videoStatus_link = f'https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.7469090931327491'
resp = requests.get(videoStatus_link, headers=headers)
dic = resp.json()

# 3.获取systemTime，将连接中的值替换为contId
srcUrl = dic['videoInfo']['videos']['srcUrl']
systemTime = dic['systemTime']
srcUrl = srcUrl.replace(systemTime, f'cont-{contId}')
print(srcUrl)

# 4.下载视频
with open(f"{contId}.mp4", mode="wb") as f:
    f.write(requests.get(srcUrl).content)


