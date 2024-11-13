
def merge_intervals(intervals):
    #check if empty
    if not intervals:
        return 0
    #sort by numerical order
    intervals.sort()
    #list to store what is merged and start from index 0 => interval 0
    merged,current_interval = [], intervals[0]


    for interval in intervals[1:]:
        #merge if current interval overlap with next interval
        if current_interval[1] >= interval[0]:
        #move current interval end to max of both interval ends
            current_interval[1] = max(current_interval[1], interval[1])
        else:
        #no overlap then continue adding to current intervals 
            merged.append(current_interval)
            current_interval = interval

    #add last interval to the new merged list
    merged.append(current_interval)

    return merged


intervals = [[1, 3], [2, 4], [6, 8]]
print(merge_intervals(intervals))
