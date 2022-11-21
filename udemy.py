def st(*args):
    d=[]
    for i in args:
        if type(i) == str:
            d.append(i)
    
    res = '#'.join(d)
    print(res)
    
st("fg","df")
