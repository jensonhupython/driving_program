#流程:
#1. 建立 driving_program GitHub 專案
#2. 寫台灣部分
#3. 架構解釋
#4. 上傳 程式碼
#5. 寫美國部分
#6. 上傳 程式碼
#7. 最後 else 部分
#8. 上傳

country = input ('請問你是哪國人: ')
age = input('請你輸入你的年齡: ')
age = int(age)

if country == "台灣":
    if age >= 18:
        print("你可以在台灣考駕照")
    else:
        print("你還不能在台灣考駕照!!")
elif country == "美國":
    if age >= 16:
        print("你可以在美國考駕照")
    else:
        print("你還不能在美國考駕照")
else:
    print("哪國人只能輸入 台灣 跟 美國")
                    