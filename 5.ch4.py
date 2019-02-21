me = {"height": "165cm",
      "eye_color": "black",
      "favorite_author": "綾辻行人"
    }

feature = input("特徴を入力してください:")

if feature in me:
    n = me[feature]
    print(n)
else: print("該当データはありません。")
