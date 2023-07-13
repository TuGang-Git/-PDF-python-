# 将多个图片拼接为PDF
用Python写的一个图片转接PDF程序，界面用的是tkinter框架。

使用步骤：
1. 创建好文件夹存储图片，有顺序要求可以给定好排序的名字
2. 运行main.py，点击“选择文件夹”
3. 选择刚才你放图片的文件夹
4. 选择pdf存储位置并命名
5. 点击返回可以继续拼接，也可以关闭

打包成.exe可执行文件：在项目位置按shift+鼠标右键选择在此处打开PowerShell窗口，

再输入pyinstaller -F main.py --noconsole

最后去生成的dist文件夹中即可找到想要的.exe可执行文件！

## Put multiple images into a PDF file
This is a program written by python whose GUI is based on tkinter

Steps to use:
1. Create a folder to put images in. Name them in order if you need.
2. Run main.py and click "选择文件夹"
3. Choose the folder you just put your images in
4. Choose the destination of PDF file and name it
5. Click "返回" to do that again or close it
