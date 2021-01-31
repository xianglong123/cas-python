import zipfile


def zip_files(files, zip_name):
    zip = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)
    for file in files:
        print('compressing', file)
        zip.write(file)
    zip.close()
    print('compressing finished')


files = ['.\\123.txt', '.\\3.txt']  # 文件的位置，多个文件用“，”隔开
zip_file = '.\\m66y.zip'  # 压缩包名字
zip_files(files, zip_file)
