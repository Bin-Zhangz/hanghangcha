import json
import execjs
import requests
page = 50

cookies = {
    'JSESSIONID': 'D24D81365B9DF23DD8AD16D145A02772',
    '_ACCOUNT_': 'NmFjOTU4ZDNlZjBmNGRlNjk4NjUyNjZlYmVlOGRhMTQlNDAlNDBtb2JpbGU6MTcyMjkwMzc5MTAyNDpmNGFkZmFjMmRiOTE5MmJmYzFiMjY0MzZmNjNkZDgzMg',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Auth-Plus': '',
    'Client-Encrypt': 'v1.1',
    'Connection': 'keep-alive',
    # 'Cookie': 'JSESSIONID=D24D81365B9DF23DD8AD16D145A02772; _ACCOUNT_=NmFjOTU4ZDNlZjBmNGRlNjk4NjUyNjZlYmVlOGRhMTQlNDAlNDBtb2JpbGU6MTcyMjkwMzc5MTAyNDpmNGFkZmFjMmRiOTE5MmJmYzFiMjY0MzZmNjNkZDgzMg',
    'Origin': 'https://www.hanghangcha.com',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
    'X-Requested-With': 'XMLHttpRequest',
    'clientInfo': 'web',
    'clientVersion': '1.0.6',
    'currentHref': 'https://www.hanghangcha.com/securities-search',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Microsoft Edge";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

for page in range(0,3500,50):

    params = {
        'filter': '{"limit":50,"skip":'+ str(page) +',"order":"total_market_value DESC","keyword":"","plate":"","regionCode":null,"year":null,"tagName":""}',
    }

    response = requests.get(
        'https://api.hanghangcha.com/hhc/member/stock/stockXueqiu',
        params=params,
        cookies=cookies,
        headers=headers,
    ).json()
    # print(response)
    with open("codejsdemo0.js","r",encoding="utf-8")as f:
        cip_hre = f.read()

    context = execjs.compile(cip_hre)
    decode = context.call("main123",response['data'])

    for i in json.loads(decode)['data']['data']:
        print(i)
    #
