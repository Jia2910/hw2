import requests
import json

# 基本参数配置
apiUrl = 'http://apis.juhe.cn/fapig/nba/query'
apiKey = 'a5ca3efbd0da40ccd2cf38f65fc6f4f0'

# 接口请求入参配置
requestParams = {
    'key': apiKey,
}

# 发起接口网络请求
response = requests.get(apiUrl, params=requestParams)

# 解析响应结果
if response.status_code == 200:
    responseResult = response.json()
    # print(responseResult)
    title = responseResult['result']['title']
    duration = responseResult['result']['duration']
    matchs = responseResult['result']['matchs']

    print(f"联赛名称: {title}")
    print(f"赛季: {duration}")
    print("比赛信息:")

    for match in matchs:
        date = match['date']
        week = match['week']
        print(f"日期: {date}, 星期: {week}")

        for game in match['list']:
            time_start = game['time_start']
            status_text = game['status_text']
            team1 = game['team1']
            team2 = game['team2']
            team1_score = game['team1_score']
            team2_score = game['team2_score']

            print(f"  开始时间: {time_start}, 状态: {status_text}")
            print(f"  {team1} {team1_score} - {team2} {team2_score}")
            print()
else:
    # 网络异常等因素，解析结果异常。可依据业务逻辑自行处理。
    print('请求异常')
