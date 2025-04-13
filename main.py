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
    print(responseResult)

else:
    # 网络异常等因素，解析结果异常。可依据业务逻辑自行处理。
    print('请求异常')
