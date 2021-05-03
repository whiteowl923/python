from PIL import Image #pillow library import image
from bs4 import BeautifulSoup 
from urllib.request import urlopen
import urllib
import io
import os #make file
import requests



def asclopic():
    url=input("애즈클로 제품링크를 넣어주세요:")
    html = urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    rootElement = soup.find("div", attrs={"class": "listImg detailimg"})
    thumbsElements = rootElement.find_all("img", attrs={"class": "ThumbImage"})
    name = soup.find("h1", attrs={"class":"name"}).get_text().strip()

    os.mkdir("./{}".format(name))

    for index, value in enumerate(thumbsElements):
        imageUrl = "http:" + value.attrs["src"]
        print("index : {}  url : {}".format(index, imageUrl))

        with urlopen(imageUrl) as url:
            file = io.BytesIO(url.read())

        image = Image.open(file)
        filename = imageUrl.rsplit('/', 1)[-1]
        image.save("./{}/{}".format(name, filename))

        print(name , "Download Complete")



def vivaclosetpic():
    url = input("비바클로젯 제품링크를 넣어주세요:")
    html = urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    rootElement = soup.find("div", attrs={"class": "cont"})
    thumbsElements = rootElement.find_all("img")
    name_address = soup.find("tr", attrs={"class":"xans-record-"})
    name = name_address.find("td").get_text().strip()

    folder_path = "./{}".format(name)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)


    for index, value in enumerate(thumbsElements):
        imageUrl = "http://vivacloset.com" + urllib.parse.quote(value.attrs["ec-data-src"])
        print("index : {}  url : {}".format(index, imageUrl))

        with urlopen(imageUrl) as url:
            file = io.BytesIO(url.read())

        image = Image.open(file)
        filename = imageUrl.rsplit('/', 1)[-1]
        image.save("./{}/{}".format(name, filename))

    print(name , "Download Complete")



def wooalong():
    url = input("우알롱 상품링크를 넣어주세요:")
    html = urlopen(url).read() 
    soup = BeautifulSoup(html, "html.parser")

    #--------get location from html--------------

    rootElement = soup.find("div",{"id":"prdDetail"})
    thumbsElements = rootElement.find_all("img")
    print(thumbsElements)
    name_address = soup.find("div", attrs={"class":"infoArea"})
    name = name_address.find("td").get_text().strip().replace("/","")

    #----------------------------------------------


    folder_path = "./{}".format(name)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)


    for index, value in enumerate(thumbsElements):
        imageUrl = "https://www.wooalong.co.kr" + value.attrs["ec-data-src"] # making an imageurl
        print("index : {} url : {}".format(index, imageUrl))


        with urlopen(imageUrl) as url:
            file = io.BytesIO(url.read())

        image = Image.open(file)
        filename = imageUrl.rsplit('/', 1)[-1]
        image.save("./{}./{}".format(name, filename))

    print(name, "Download Complete")



def unetine():
    url=input("우네띠네 제품링크를 넣어주세요:")
    html = urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    rootElement = soup.find("div", attrs={"class": "cont"})
    thumbsElements = rootElement.find_all("img")
    name = soup.find("p", attrs={"style":"padding:0 5px 15px;"}).get_text().strip().replace("/","").replace("(해외배송 가능상품)","")


    os.mkdir("./{}".format(name))


    for index, value in enumerate(thumbsElements):
        imageUrl = "http://unetine.kr" + urllib.parse.quote(value.attrs["ec-data-src"])
        print("index : {}  url : {}".format(index, imageUrl))

        with urlopen(imageUrl) as url:
            file = io.BytesIO(url.read())

        image = Image.open(file)
        filename = imageUrl.rsplit('/', 1)[-1]
        image.save("./{}/{}".format(name, filename))

    print(name , "Download Complete")



def palejade():
    url=input("페일제이드 제품링크를 넣어주세요:")
    html = urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    rootElement = soup.find("div", attrs={"class": "cont"})
    thumbsElements = rootElement.find_all("img")
    address = soup.find("div", attrs={"class":"headingArea"})
    name = address.find("h2").get_text().strip().replace("/","")

    # print(thumbsElements)
    # # print(name)

    os.mkdir("./{}".format(name))


    for index, value in enumerate(thumbsElements):
        imageUrl = "http://palejade.shop" + urllib.parse.quote(value.attrs["ec-data-src"])
        print("index : {}  url : {}".format(index, imageUrl))

        with urlopen(imageUrl) as url:
            file = io.BytesIO(url.read())

        image = Image.open(file)
        filename = imageUrl.rsplit('/', 1)[-1]
        image.save("./{}/{}".format(name, filename))

    print(name , "Download Complete")



def dearmine():
    url=input("디얼마인 제품링크를 넣어주세요:")
    html = urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    rootElement = soup.find("div", attrs={"class": "edibot-product-detail"})
    thumbsElements = rootElement.find_all("img")
    name = soup.find("div", attrs={"class":"optCon"}).get_text().strip().replace("/","")

    # print(thumbsElements)

    os.mkdir("./{}".format(name))

    x = int

    for index, value in enumerate(thumbsElements):
        imageUrl = "https:" + urllib.parse.quote(value.attrs["ec-data-src"])
        x = imageUrl.find("img.cafe24.com") # find a link that makes an error
        if x > 0 :
            break
        print("index : {}  url : {}".format(index, imageUrl))

        with urlopen(imageUrl) as url:
            file = io.BytesIO(url.read())

        image = Image.open(file)
        filename = imageUrl.rsplit('/', 1)[-1]
        image.save("./{}/{}".format(name, filename))

    print(name , "Download Complete")



def acubi_club():
    url=input("아쿠비클럽 제품링크를 넣어주세요:")
    html = urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    rootElement = soup.find("div", attrs={"class": "cont"})
    thumbsElements = rootElement.find_all("img")
    name = soup.find("div", attrs={"class":"headingArea"}).get_text().strip().replace("/","")

    # print(thumbsElements)
    # # print(name)

    os.mkdir("./{}".format(name))


    for index, value in enumerate(thumbsElements):
        imageUrl = "http://acubi-club.kr" + urllib.parse.quote(value.attrs["ec-data-src"])
        print("index : {}  url : {}".format(index, imageUrl))

        with urlopen(imageUrl) as url:
            file = io.BytesIO(url.read())

        image = Image.open(file)
        filename = imageUrl.rsplit('/', 1)[-1]
        image.save("./{}/{}".format(name, filename))

    print(name , "Download Complete")



def looknone():
    url=input("룩넌 제품링크를 넣어주세요:")
    html = urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    rootElement = soup.find("div", attrs={"class": "cont"})
    thumbsElements = rootElement.find_all("img")
    address = soup.find("div", attrs={"class":"headingArea"})
    name = address.find("h2").get_text().strip().replace("/","")

    # print(thumbsElements)
    # # print(name)

    os.mkdir("./{}".format(name))

    x = int

    for index, value in enumerate(thumbsElements):
        imageUrl = "https://looknone.co.kr" + urllib.parse.quote(value.attrs["src"])
        x = imageUrl.find("cafe24") # find a link that makes an error
        if x > 0 :
            break
        print("index : {}  url : {}".format(index, imageUrl))

        with urlopen(imageUrl) as url:
            file = io.BytesIO(url.read())

        image = Image.open(file)
        filename = imageUrl.rsplit('/', 1)[-1]
        image.save("./{}/{}".format(name, filename))

    print(name , "Download Complete")



def raviroom():
    url=input("라비룸 제품링크를 넣어주세요:")
    html = urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    rootElement = soup.find("div", attrs={"class": "cont detail_con"})
    thumbsElements = rootElement.find_all("img")
    address = soup.find("div", attrs={"class":"headingArea"})
    name = address.find("h2").get_text().strip().replace("/","")

    # print(thumbsElements)
    # print(name)

    os.mkdir("./{}".format(name))


    for index, value in enumerate(thumbsElements):
        imageUrl = "http://raviroom.com" + urllib.parse.quote(value.attrs["src"])
        print("index : {}  url : {}".format(index, imageUrl))

        with urlopen(imageUrl) as url:
            file = io.BytesIO(url.read())

        image = Image.open(file)
        filename = imageUrl.rsplit('/', 1)[-1]
        image.save("./{}/{}".format(name, filename))

    print(name , "Download Complete")



def hoibo():
    url=input("호아이보 제품링크를 넣어주세요:")
    html = urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    rootElement = soup.find("div", attrs={"class": "cont"})
    thumbsElements = rootElement.find_all("img",attrs={"alt":""})
    del thumbsElements[-2:] # 뒤에 에러지우기

    name = soup.find("td").get_text().strip().replace("/","").replace("상품명","")

    # print(thumbsElements)
    os.mkdir("./{}".format(name))

    # for value in enumerate(thumbsElements):
    #     print(value)    
        
    for index, value in enumerate(thumbsElements):
        imageUrl = "http://hoibo.kr" + urllib.parse.quote(value.attrs["ec-data-src"])
        print("index : {}  url : {}".format(index, imageUrl))

    
        with urlopen(imageUrl) as url:
            file = io.BytesIO(url.read())

        image = Image.open(file)
        filename = imageUrl.rsplit('/', 1)[-1]
        image.save("./{}/{}".format(name, filename))

    print(name , "Download Complete")



def hittaek():
    url=input("히트택 제품링크를 넣어주세요:")
    html = urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    rootElement = soup.find("div", attrs={"class": "edibot-product-detail"})
    thumbsElements = rootElement.find_all("img")
    del thumbsElements[:5]
    address = soup.find("div", attrs={"class":"headingArea"})
    name = address.find("h2").get_text().strip().replace("/","").replace("1+1","")

    # print(thumbsElements)
    # for value in enumerate(thumbsElements):
    #     print(value)
    # # print(name)

    os.mkdir("./{}".format(name))


    for index, value in enumerate(thumbsElements):
        imageUrl = "http:" + urllib.parse.quote(value.attrs["ec-data-src"])
        print("index : {}  url : {}".format(index, imageUrl))

        with urlopen(imageUrl) as url:
            file = io.BytesIO(url.read())

        image = Image.open(file)
        filename = imageUrl.rsplit('/', 1)[-1]
        image.save("./{}/{}".format(name, filename))

    print(name , "Download Complete")



def bowlow():
    url=input("바우로 제품링크를 넣어주세요:")
    html = urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    rootElement = soup.find("div", attrs={"class":"edibot-product-detail"})
    thumbsElements = rootElement.find_all("img", attrs={"style":"display: block; max-width:100%"})
    address = soup.find("div", attrs={"class":"mun-detail-desc"})
    name = address.find("span").get_text().strip().replace("/","")
    # print(name)

    # print(thumbsElements)



    os.mkdir("./{}".format(name))



    for index, value in enumerate(thumbsElements):
        imageUrl = "http:" + urllib.parse.quote(value.attrs["ec-data-src"])
        print("index : {}  url : {}".format(index, imageUrl))

        with urlopen(imageUrl) as url:
            file = io.BytesIO(url.read())

        image = Image.open(file)
        filename = imageUrl.rsplit('/', 1)[-1]
        image.save("./{}/{}".format(name, filename))

    print(name , "Download Complete")


def our_uniform():
    url=input("아워유니폼 제품링크를 넣어주세요:")
    html = urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    rootElement = soup.find("div", attrs={"class": "cont productdetail"})
    thumbsElements = rootElement.find_all("img")
    name = soup.find("div", attrs={"class":"productname -f_ns"}).get_text().strip().replace("/","")

    os.mkdir("./{}".format(name))

    for index, value in enumerate(thumbsElements):
        imageUrl = "http://www.our-uniform.com" + urllib.parse.quote(value.attrs["ec-data-src"]) #urllib.parse.quote 한국말 링크 바꿔주는것
        print("index : {}  url : {}".format(index, imageUrl))

        with urlopen(imageUrl) as url:
            file = io.BytesIO(url.read())

        image = Image.open(file)
        filename = imageUrl.rsplit('/', 1)[-1]
        image.save("./{}/{}".format(name, filename))

    print(name , "Download Complete")




def roain():
    url=input("로아인 제품링크를 넣어주세요:")
    html = urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    rootElement = soup.find("div", attrs={"style":"margin: 0px; padding: 0px; text-align: center; text-size-adjust: auto;"})
    thumbsElements = rootElement.find_all("img")
    del thumbsElements[:2]
    address = soup.find("div", attrs={"class":"prd_name"})
    name = address.find("li", attrs={"class":"name"}).get_text().strip().replace("/","")
    # print(name)

    # print(thumbsElements)



    os.mkdir("./{}".format(name))



    for index, value in enumerate(thumbsElements):
        imageUrl = "http://roain.kr" + urllib.parse.quote(value.attrs["ec-data-src"])
        print("index : {}  url : {}".format(index, imageUrl))

        with urlopen(imageUrl) as url:
            file = io.BytesIO(url.read())

        image = Image.open(file)
        filename = imageUrl.rsplit('/', 1)[-1]
        image.save("./{}/{}".format(name, filename))

    print(name , "Download Complete")




def picture():
    if pic_brand == "애즈클로":
        asclopic()

    elif pic_brand == "우알롱":
        wooalong()

    elif pic_brand == "비바클로젯":
        vivaclosetpic()

    elif pic_brand == "라비룸":
        raviroom()

    elif pic_brand == "우네띠네":
        unetine()

    elif pic_brand == "디얼마인":
        dearmine()

    elif pic_brand == "아쿠비클럽":
        acubi_club()

    elif pic_brand == "페일제이드":
        palejade()

    elif pic_brand == "룩넌":
        looknone()

    elif pic_brand == "호아이보":
        hoibo()

    elif pic_brand == "히트택":
        hittaek()

    elif pic_brand == "아워유니폼":
        our_uniform()

    elif pic_brand == "바우로":
        bowlow()

    elif pic_brand == "로아인":
        roain()




print("\nFECLODIN PICTURE DOWNLOAD PROGRAM")
print("브랜드명을 정확하게 입력해주세요!")
print("가능한 브랜드: 애즈클로, 바우로, 호아이보, 히트택, 디얼마인, 비바클로젯, 라비룸, 룩넌, 아워유니폼, 아쿠비클럽, 우네띠네, 페일제이드, 우알롱\n")
pic_brand = input("사진을 가져올 브랜드명을 입력하세요:")



while pic_brand != "멈춰":
    picture()
