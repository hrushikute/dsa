def sum_rec(tart,end):
    if tart == end:
        return tart
    # if end -tart ==1:
    #     return tart+end
    mid = (tart+end)//2
    return sum_rec(tart,mid) + sum_rec(mid+1, end)

print(sum_rec(0,10091))
