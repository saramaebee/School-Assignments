# Type your code here. 
def __main__():
    inpass = input()
    inshdw = input()
    user = input()
    pw = input()
    
    ip_lines = []
    is_lines = []
    
    with open(inpass, 'r') as _inpass:
        for un_line in _inpass:
            # print(line)
            ip_lines.append(un_line.split(':', 2)[0])
    
    with open(inshdw, 'r') as _inshdw:
        for pw_line in _inshdw:
            is_lines.append(pw_line.split(':', 2)[1])
            
    # print('ip_lines:', ip_lines)
    # print('is_lines:', is_lines)
        
    for i in range(min(len(ip_lines), len(is_lines))):
        print('Brute Force Attempt:')
        print('Login:', ip_lines[i])
        print('Password:', is_lines[i])
        print('Successful' if (ip_lines[i] == user and is_lines[i] == pw) else 'Unsuccessful', 'brute force attempt')
        print()
    
if __name__ == '__main__':
    __main__()
