# создание файла с логами
import requests
url = 'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
content_url = requests.get(url)
content = content_url.text
with open('logs.txt', 'w') as f:
    f.write(content)
line_list = []
with open('logs.txt', 'r') as f:
    for line in f:
        num = line.find(' ')
        line_1 = line[: num]
        num2 = line.find('"', num)
        num2_end = line.find(' ', num2)
        line_2 = line[num2: num2_end]
        num3_end = line.find(' ', num2_end + 1)
        line_3 = line[num2_end + 1: num3_end]
        line_list.append((line_1, line_2, line_3))

print(line_list)