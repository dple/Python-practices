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
    if len(ext) > 3:
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

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print(filtered_emails)