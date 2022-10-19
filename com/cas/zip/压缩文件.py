import zipfile


def zip_files(files, zip_name):
    zip = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)
    for file in files:
        print('compressing', file)
        zip.write(file)
    zip.close()
    print('compressing finished')


files = ['.\\123.txt', '.\\3.txt']
zip_file = '.\\m66y.zip'
zip_files(files, zip_file)
