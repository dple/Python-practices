import re

if __name__ == '__main__':
    T = int(input()) 
    pattern = r'^[+-]?\d*.\d+$'

    for _ in range(T): 
        
        f = input()         
    
        try:        
            num = float(f)     
            match = re.search(pattern, f) 
            print(bool(match)) 
        except: 
            print(False)