import re

def fun(s):
    # return True if s is a valid email, else return False
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphanumeric = alphabet + "0123456789"
    usernames = alphanumeric + "_-"
    try:
        i = s.index('@')
    except ValueError:
        return False
    try:    
        j = s.index('.')
    except ValueError:
        return False
                
    username = s[:i]
    website_name = s[i+1:j]
    ext = s[j+1:]

    if len(ext) > 3 or len(ext) == 0 or len(username) == 0 or len(website_name) == 0:
        return False
        
    for c in username:
        if c not in usernames:
            return False
    
    for c in website_name:
        if c not in alphanumeric:
            return False
    
    for c in ext:
        if c not in alphabet:
            return False 
    
    return True 

def fun2(s):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphanumeric = alphabet + "0123456789"
    usernames = alphanumeric + "_-"
    # Using RegEx to parse an email
    m = re.match(r'(\w+)@(\w+)\.(\w+)', s)

    if m is None or len(m.group(3)) > 3:        
        return False
    
    for c in m.group(1):
        if c not in usernames:
            return False
    
    for c in m.group(2):
        if c not in alphanumeric:
            return False
    
    for c in m.group(3):
        if c not in alphabet:
            return False 
    
    return True 

def filter_mail(emails):
    return list(filter(fun2, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print(filtered_emails)