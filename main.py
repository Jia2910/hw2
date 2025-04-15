import requests

class nbamessage:
    def __init__(self, flag):
        self.flag = flag
        if self.flag == 1:
            self.apiUrl = 'http://apis.juhe.cn/fapig/nba/query'
        elif self.flag == 2:
            self.apiUrl = 'http://apis.juhe.cn/fapig/nba/rank'
        else:
            print("error")
            exit()
        self.apiKey = 'a5ca3efbd0da40ccd2cf38f65fc6f4f0'
        # 接口请求入参配置
        self.requestParams = {
            'key': self.apiKey,
        }
        self.response = requests.get(self.apiUrl, params=self.requestParams)

    def get_message(self):
        if self.flag == 1:
            if self.response.status_code == 200:
                responseResult = self.response.json()
                self.title = responseResult['result']['title']
                self.duration = responseResult['result']['duration']
                self.matchs = responseResult['result']['matchs']

            else:
                # 网络异常等因素，解析结果异常。可依据业务逻辑自行处理。
                print('请求异常')
        elif self.flag == 2:
            if self.response.status_code == 200:
                responseResult = self.response.json()
                self.title = responseResult['result']['title']
                self.duration = responseResult['result']['duration']
                self.rankings = responseResult['result']['ranking']
            else:
                # 网络异常等因素，解析结果异常。可依据业务逻辑自行处理。
                print('请求异常')
        else:
            print('请求异常')

    def display_all(self):
        if self.flag == 1:

            print(f"联赛名称: {self.title}")
            print(f"赛季: {self.duration}")
            print("比赛信息:")

            for match in self.matchs:
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

            print(f"联赛名称: {self.title}")
            print(f"赛季: {self.duration}")
            print("排名情况:")

            for area in self.rankings:
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



def main():
    print("查看近日赛程（输入1）/查看排名情况（输入2）")
    flag = int(input())
    nba = nbamessage(flag)
    nba.get_message()
    nba.display_all()


if __name__ == "__main__":
    main()


