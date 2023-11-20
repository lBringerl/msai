def check_pwd(pwd: str):
    if len(pwd) < 8:
        return False
    if pwd.lower() == pwd:
        return False
    if pwd.upper() == pwd:
        return False
    if pwd.lower().find('anna') != -1:
        return False
    if not any(c.isdigit() for c in pwd):
        return False
    if len({c for c in pwd}) < 4:
        return False
    return True
    

if __name__ == '__main__':
    pwd = input()
    if check_pwd(pwd):
        print('strong')
    else:
        print('weak')
