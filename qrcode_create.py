import qrcode

        #二维码的生成

data = input("请输入一个任意的数据")
img = qrcode.make(data)
img.save("qrcode.jpg")
img.show()

input("按回车键退出")