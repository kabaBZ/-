# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import json

def response(follow):
    if '/aweme/v1/user/follower/list/' in follow.request.url:
        for user in json.loads(follow.response.text)['followers']:
            user_info = {}
            user_info['share_id'] = user['uid']
            user_info['DY_id'] = user['short_id']
            user_info['nickname'] = user['nickname']
            with open('douyin.csv','a',encoding='utf-8') as f:
                f.write(json.dumps(user_info,ensure_ascii=False))
                f.write('\n')
