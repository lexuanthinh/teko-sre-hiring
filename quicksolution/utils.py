import iso8601
import pytz

class Utils:
    def __init__(self):
        self.count = 0

    def convertTimestampToInt(self, timestamp):
        ##Convert timestamp to integer
        timestamp = timestamp.strip('\n')
        _date_obj = iso8601.parse_date(timestamp).astimezone(pytz.utc)
        ts = int(_date_obj.timestamp())

        return ts


    def analizeRequest(self, request_ts, bypass, max_rate):
        ## Implement argorithm
        present_rate = 0
        last_1hour = int(request_ts[-1] - 3600)
        # print(sorted(request_ts, reverse=True))

        if request_ts[0] >= last_1hour:
            bypass.append(0)

        else:
            for timestamp in sorted(request_ts, reverse=True):
                if timestamp > last_1hour:
                    pass
                elif timestamp <= last_1hour:
                    bypass_idx = len(request_ts) - sorted(request_ts, reverse=True).index(timestamp)

                    for e in range(bypass_idx, len(bypass)):
                        present_rate = present_rate + bypass[e]
                        
                    if present_rate < max_rate:
                        bypass.append(1)
                    elif present_rate >= max_rate:
                        bypass.append(0)
                    break

        return bypass