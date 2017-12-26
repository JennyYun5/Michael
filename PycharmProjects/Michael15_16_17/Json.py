import json
# 将数组编码为 JSON 格式数据
data = [{'a':1, 'b':2, 'c':3, 'd':4, 'e':5}]
json = json.dumps(data, sort_keys=True, indent=4, separators=(',', ';'))
print(json)

# json.loads 用于解码 JSON 数据。该函数返回 Python 字段的数据类型。
jsonData = {"a":1,"b":2,"c":3,"d":4,"e":5}
text = json.loads(jsonData)
print(text)
