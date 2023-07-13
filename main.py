import tkinter as tk
from tkinter import filedialog
from PIL import Image
import os

def img_to_pdf(infolder, outpath):
    # 提取出文件夹中的所有图片
    img_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff')
    img_files = [file for file in os.listdir(infolder) if file.lower().endswith(img_extensions)]

    # 存放图片对象
    images = []
    cnt = 0
    first_image = None
    for img_file in img_files:
        img_path = os.path.join(infolder, img_file)
        image = Image.open(img_path).convert("RGB")
        if cnt == 0:
            first_image = image
            cnt = 1
        else:
            image = image.resize(first_image.size) # 所有图片大小和第一张保持一致
        images.append(image)

    # 拼接成pdf文件
    if images:
        images[0].save(outpath, save_all=True, append_images=images[1:], quality=95)
        # select_button.config(text="")
        # hint_label.config(text="")
        select_button.pack_forget()
        hint_label.pack_forget()

        completion_label.config(text="拼接完成！", font=32)
        completion_label.pack(pady=40)
        path = os.path.join(outpath)
        for i in range(len(path)):
            if i % 30 == 0 and i != 0:
                path = path[:i+1] + '\n' + path[i+1:]
        path_label.config(text="PDF路径：" + path, font=32)
        path_label.pack()
        return_button.pack(pady=10)
    else:
        completion_label.config(text="未找到图片！", font=32)
        path_label.config(text="", font=32)
        return_button.pack_forget()

def select_folder():
    folder_path = filedialog.askdirectory()

    if folder_path:
        pdf_file = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])

        if pdf_file:
            img_to_pdf(folder_path, pdf_file)

def return_to_main():
    completion_label.pack_forget()
    path_label.pack_forget()
    return_button.pack_forget()
    # select_button.config(text="选择文件夹", font=32)
    # hint_label.config(text="选择图片所在的文件夹，将其中的图片拼接成pdf文件", font=32)
    select_button.pack(pady=20)
    hint_label.pack()

root = tk.Tk()
root.title("图片拼接PDF文件")

# 获取窗口大小
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
Width = 640  # 窗口大小值
Hight = 320
# 计算中心坐标
cen_x = (sw - Width) / 2
cen_y = (sh - Hight) / 2
# 设置窗口大小并居中
root.geometry('%dx%d+%d+%d' % (Width, Hight, cen_x, cen_y))


select_button = tk.Button(root, text="选择文件夹", command=select_folder, font=32)
select_button.pack(pady=20)
hint_label = tk.Label(root,text="选择图片所在的文件夹，将其中的图片拼接成pdf文件。"
                                "\n当选择完图片所在文件夹后，"
                                "\n可以选择PDF文件存放位置并命名"
                                "\n\n请注意原图片的方向，如果有误请手动调整回来", font=32)
hint_label.pack()

completion_label = tk.Label(root, text="", font=32)
completion_label.pack(pady=40)

path_label = tk.Label(root, text="")
path_label.pack()

return_button = tk.Button(root, text="返回", command=return_to_main, font=32)

root.mainloop()
