import requests
def current_games():
    # 基本参数配置
    apiUrl1 = 'http://apis.juhe.cn/fapig/nba/query'
    apiKey = 'a5ca3efbd0da40ccd2cf38f65fc6f4f0'

    # 接口请求入参配置
    requestParams = {
        'key': apiKey,
    }

    # 发起接口网络请求
    response = requests.get(apiUrl1, params=requestParams)

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
def ranking():
    # 基本参数配置
    apiUrl2 = 'http://apis.juhe.cn/fapig/nba/rank'  # 接口请求URL
    apiKey = 'a5ca3efbd0da40ccd2cf38f65fc6f4f0'  # 在个人中心->我的数据,接口名称上方查看

    # 接口请求入参配置
    requestParams = {
        'key': apiKey,
    }

    # 发起接口网络请求
    response = requests.get(apiUrl2, params=requestParams)

    # 解析响应结果
    if response.status_code == 200:
        responseResult = response.json()
        # 网络请求成功。可依据业务逻辑和接口文档说明自行处理。
        title = responseResult['result']['title']
        duration = responseResult['result']['duration']
        rankings = responseResult['result']['ranking']
        print(f"联赛名称: {title}")
        print(f"赛季: {duration}")
        print("排名情况:")

        for area in rankings:
            name = area['name']
            type = area['type']
            print(f'地区：{name}/{type}')
            for list in area['list']:
                rank_id = list['rank_id']
                team = list['team']
                wins = list['wins']
                losses = list['losses']
                wins_rate = list['wins_rate']
                avg_score = list['avg_score']
                avg_lose_score = list['avg_lose_score']

                print(f'排名：{rank_id} 队伍名称：{team}')
                print(f'胜场数：{wins} 负场数：{losses}')
                print(f'胜率：{wins_rate}')
                # print(f'平均得分：{avg_score} 平均失分：{avg_lose_score}')
                print()
    else:
        # 网络异常等因素，解析结果异常。可依据业务逻辑自行处理。
        print('请求异常')


def main():
    print("查看近日赛程（输入1）/查看排名情况（输入2）")
    flag = int(input())
    if flag == 1:
        current_games()
    else:
        ranking()


if __name__ == "__main__":
    main()