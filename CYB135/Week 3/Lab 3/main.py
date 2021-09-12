import csv

def __main__():
    filename = input()
    anomalies = {}
    with open(filename) as _file:
        file_reader = csv.reader(_file, delimiter=',')
        for row in file_reader:
            # kinda frustrated with the csv file being a single line but what can ya do
            for i in range(len(row)):
                if i % 2 == 0:
                    _login_attempt = (row[i], int(row[i+1]))
                    if _login_attempt[1] < 9 or _login_attempt[1] > 17:
                        anomalies[_login_attempt[0]] = _login_attempt[1]
    
    if len(anomalies) > 0:
        print('Anomaly Login Attempts:')
        for login in anomalies:
            print(f'{login} {anomalies[login]}')
    else:
        print('No anomaly login attempts')
        
if __name__ == '__main__':
    __main__()
