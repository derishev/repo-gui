ip_dict = {}
with open('logs.txt', 'r') as f:
    for line in f:
        num = line.find(' ')
        ip_address = line[: num]
        if ip_address in ip_dict:
            value = ip_dict[ip_address]
            ip_dict[ip_address] = value + 1
        else:
            ip_dict[ip_address] = 1
max_spam = dict([max(ip_dict.items(), key=lambda k_v: k_v[1])])
print(max_spam)