import os, re
list = []
with open(os.path.join(os.path.dirname(__file__),'filter_words.txt'), encoding='utf-8') as f:
    for content in f.readlines():
        content = content.strip('\n').encode('utf-8').decode('utf-8-sig')
        list.append(content)
print([x for x in list])

user_input = input("Please input sentense: ")
for word in list:
    if word in user_input:
        new = re.subn(word,'*'*len(word),user_input)
        user_input = new[0]
print(user_input)



