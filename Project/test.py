data = ['phill', 'henry', 'john']
def ana(dat):
    return len(dat)

while True:
    print(ana(data))
    res = str(input())
    data.append(res)
    