import os
import re
from pprint import pprint

path = r"/Volumes/Media/【画质狂魔&猪猪】火影忍者001-720 DVD&HD GB MKV 收藏版 中文字幕 (高速做种正式版)/火影忍者.疾风传"
pattern = r"\[\d*\]"


def subn(matched):
    value = int(matched.group('value'))
    print(value - 220)
    return f"[{value - 220}]"


for p, _, filenames in os.walk(path):
    for filename in filenames:
        if re.search(pattern, filename):
            new_name = re.sub('\[(?P<value>\d+)\]', subn, filename)
            # print(new_name)
            os.rename(os.path.join(p, filename), os.path.join(p, new_name))
