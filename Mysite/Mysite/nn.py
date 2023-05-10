# non
from django.http import HttpResponse as hr
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
def passing_(request):
    # global password
    import random
    import string
    s1= string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    vaue  = random.shuffle(s)
    password = "".join(s[0:16])

    password = "".join(s[0:16])
    params={"keys":password}
    return password


def about(request):
    name=request.GET.get('text','default')
    print(name)
    cheak=request.GET.get('data cheak','off')
    print(cheak)
    analize=name.lower()
    passi = passing_(request)
    params={'goodword':analize,'keys':passi}
    if cheak=='on':
        li=[]
        code=3
        with open("ans.txt",'r')as t:
            file_in=t.readlines()
            print("line readed")
            for names in file_in:
                li.append(names.strip())
                print(f"list appended {li}")
            for data in li:
                # print(data,analize)
                if data==analize:
                    # print(name)
                    print("it is already in list")
                    code=0
                    break
                else:
                    code=1
        if code==1:
            with open('ans.txt','a') as t:
                t.write(name.lower())
                t.write('\n')
                print("data saved!!")
        else:
            pass
    elif cheak=='off':
        print('data is not saved')
    else:
        pass
    return render(request,'pag.html',params)
def cap(request):
    return hr("1")
