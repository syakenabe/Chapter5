print("Hello".upper())

print("Hello".replace("l","L"))

fruit =[]

print(fruit)

fruit = ["apple", "orange", "greap"]

print(fruit)

fruit.append("banana")
fruit.append("peach")

print(fruit)

random = []

random.append(True)
random.append(151)
random.append(1.2)
random.append("Hello")

print(random)

print(fruit[0])
print(random[3])

colors = ["bule", "green", "yellow" ]

print(colors)

colors[2] = "red"

print(colors)

colors = ["bule", "green", "yellow"]
print(colors)
item = colors.pop()
print(item)
print(colors)

colors1 = ["bule", "green", "yellow"]
colors2 = ["orenge", "pink", "black"]
print(colors1 + colors2)

colors = ["bule", "green", "yellow"]
print("white" in colors)

colors = ["bule", "green", "yellow"]
print("black" not in colors)

print(len(colors))

#colors = ["purple", "orenge", "green"]
#guess = input("何色でしょう？（入力してください）：")
#if guess in colors:
#    print("あたり")
#else:
#    print("はずれ")

my_tuple = ()
print(my_tuple)

randam = ("M.Jackson", 1958, True)
print(randam)

#これはタプル
print(("self_taught",))
#これは数値演算のかっこ
print((9+4)*2)

dys = ("1984", "Brave New World", "Fahrenheit 451")
#タプルは変更できない！
#dys[1] = "Handmaid's Tale"
print(dys[2])

print("1984" in dys)
print("Handmaid's Tale" not in dys)

fruits = {"Apple": "Red",
          "Banana": "Yellow"}
print(fruits)

facts ={}
#バリューを追加
facts["code"] = "fun"
#キーで参照
print(facts["code"])

#バリューを追加
facts["Bill"] = "Gates"
#キーで参照
print(facts["Bill"])

#バリューを追加
facts["founded"] = 1776
#キーで参照
print(facts["founded"])

bill = {"Bill Gates": "charitable"}
print("Bill Gates" in bill)
print("Bill Doors" not in bill)

books = {"Dracula": "Stoker",
         "1984": "Orwell",
         "The Trial": "Kafka"}
del books ["The Trial"]
print(books)

songs = {"1": "fun",
         "2": "blue",
         "3": "me",
         "4": "floor",
         "5": "live"
         }
#n = input("数字を入力してください:")

#if n in songs:
#    song = songs[n]
#    print(song)
#else:
#   print("見つかりません")
lists = []
rap = ["カニエ・ウェスト", "ジェイ・Ｚ", "エミネム", "ナズ"]
rock = ["ボブ・ディラン", "ザ・ビートルズ", "レッド・ツェッペリン"]
djs = ["ゼッズ・デッド", "ティエスト"]

lists.append(rap)
lists.append(rock)
lists.append(djs)

print(lists)

rap = lists[0]
rap.append("ケンドリック・ラマー")
print(rap)
print(lists)

locations = []
la = (34.0522, 188.2437)
chicago = (41.8781, 87.6298)

locations.append(la)
locations.append(chicago)

print(locations)

eights = ["Edger Allan Poe", "Charles Dickens"]
nines = ["Hemingway", "Fitzgerald", "Orwell"]
authors = (eights, nines)
print(authors)

bday = {"Hemingway": "7.21.1899",
        "Fitzgerald": "9.24.1896"}

my_list = [bday]
print(my_list)
my_tuple = (bday,)
print(my_tuple)

ny = {
    "座標": (40.7128, 74.0059),

    "セレブ": [
        "ウッディ・アレン",
        "ジェイ・ｚ",
        "ケヴィン・ベーコン",
        ],
    "事実":{
        "州": "ニューヨーク",
        "国": "アメリカ",
        }
    }

print(ny)
