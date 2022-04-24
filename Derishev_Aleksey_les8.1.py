import re

email_dict = {}
re_name = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')


def email_parse(email_address):
    if re_name.match(email_address):
        user_neme = email_address[: email_address.find('@')]
        domain_name = email_address[email_address.find('@') + 1:]
        email_dict[user_neme] = domain_name
    else:
        raise ValueError
    return email_dict


if __name__ == '__main__':
    print(email_parse('name.surname@gmail.com'))
