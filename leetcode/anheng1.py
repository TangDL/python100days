import sys

if __name__=="__main__":
    [n, m] = list(map(int, sys.stdin.readline().strip().split()))
    nums = []
    for i in range(m):
        nums.append(list(map(int, sys.stdin.readline().strip().split())))

    [start, end, begin_time] = list(map(str, sys.stdin.readline().strip().split()))
    month = int(begin_time.split('.')[0])
    [day, hour] = list(map(int, begin_time.split('.')[1].split('/')))
    start, end = int(start), int(end)
    cost_times = []

    def helper(start, cost_time):
        for s, e, time in nums:
            if s == start and e == end:
                cost_times.append(cost_time+time)
                return
            if s == start:
                cost_time += time
                helper(e, cost_time)
                cost_time -= time

    helper(start, 0)
    min_time = min(cost_times)

    need_day = min_time // 24
    need_hour = min_time % 24
    need_month = need_day // 30

    end_day = day + need_day + 1 if (hour + need_hour) // 24 > 0 else 0
    end_month = month + need_month + 1 if (end_day) // 30 > 0 else 0
    end_day = end_day % 30
    end_hour = (hour + need_hour)%24

    sys.stdout.write("%d.%d/%d"%(end_month, end_day, end_hour))
