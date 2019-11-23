seg = [0] * (800005)
lazy = [0] * (800005)
inf = 10000000

def build(ind,st,end):
    if(st > end):
        return

    if(st == end):
        seg[ind] = l[st]
        return

    mid = (st + end)//2

    build(2*ind,st,mid)
    build(2*ind + 1,mid + 1,end)

    seg[ind] = min(seg[2*ind],seg[2*ind + 1])



def rupdate(ind,st,end,lt,rt,val):

    if(st > end or st > rt or end < lt):
        return


    if(lazy[ind] != 0):
        seg[ind] += lazy[ind]
        if(st != end):
            lazy[2*ind] += lazy[ind]
            lazy[2*ind + 1] += lazy[ind]

        lazy[ind] = 0




    if(st >= lt and end <= rt):
        seg[ind] += val

        if(st != end):
            lazy[2*ind] += val
            lazy[2*ind + 1] += val


        return



    mid = (st + end)//2
    rupdate(2*ind,st,mid,lt,rt,val)
    rupdate(2*ind + 1,mid + 1,end,lt,rt,val)

    seg[ind] = min(seg[2*ind] + lazy[2*ind],seg[2*ind + 1] + lazy[2*ind + 1])




def query(ind,st,end,lt,rt):

    if(st > rt or end < lt):
        return inf


    if(lazy[ind] != 0):
        seg[ind] +=lazy[ind]

        if(st != end):
            lazy[2*ind] += lazy[ind]
            lazy[2*ind + 1] += lazy[ind]

        lazy[ind] = 0

    if(st >= lt and end <= rt):
        return seg[ind] + lazy[ind]


    mid = (st + end)//2

    x = query(2*ind,st,mid,lt,rt)
    y = query(2*ind + 1,mid+1,end,lt,rt)

    return min(x,y)





