from utils import Utils

request_ts = []
bypass = []

def loadData(path):
    with open(path) as f:
        lines = f.readlines()
    return lines

def writeOutput(path, res):
    with open(path, mode = 'wt', encoding = 'utf-8') as output:
        output.write('\n'.join(str(r) for r in res))

if __name__ == '__main__':
    utils = Utils()
    cnt = 0
    # file_path = 'input.txt'
    file_path = str(input("Enter the input txt file path (default input.txt): ") or "input.txt")
    lines = loadData(file_path)

    for line in lines:
        ## Get max rate from input file
        if cnt == 0:
            max_rate = line.split()[1]
            cnt = 1

        ## Handle the requests timestamp  
        elif cnt != 0:
            ts = utils.convertTimestampToInt(line)
            request_ts.append(ts)
            if len(request_ts) <= int(max_rate):
                bypass.append(1)
            else:
                bypass = utils.analizeRequest(request_ts, bypass, int(max_rate))
            
        print(bypass)    
        print('-'*50)
    
    ## Write result to output file
    bool_bypass = list(map(bool, bypass))

    writeOutput('output.txt', bool_bypass)
