from utils import Utils

request_ts = []
bypass = []

def loadData(path):
    with open(path) as f:
        lines = f.readlines()
    return lines

def writeOutput(path):
    pass

if __name__ == '__main__':
    utils = Utils()
    cnt = 0
    file_path = 'input.txt'
    lines = loadData(file_path)

    for line in lines:
        if cnt == 0:
            max_rate = line.split()[1]
            cnt = 1
        elif cnt != 0:
            ts = utils.convertTimestampToInt(line)
            request_ts.append(ts)
            if len(request_ts) <= int(max_rate):
                bypass.append(1)
            else:
                bypass = utils.analizeRequest(request_ts, bypass, int(max_rate))
            
        print(bypass)    
        print('-'*50)

