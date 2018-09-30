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
        print("你可以考駕照")
    else:
        print("你還不能考駕照!!")