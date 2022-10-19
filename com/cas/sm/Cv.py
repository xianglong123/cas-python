import subprocess

# 实现拷贝
def copy(text):
    p = subprocess.Popen(["pbcopy", "w"], stdin=subprocess.PIPE, close_fds=True)
    # 将内容(text)拷贝起来
    p.communicate(input=text.encode("utf-8"))

# 实现粘贴
def paste():
    p = subprocess.Popen(["pbpaste", "r"], stdout=subprocess.PIPE, close_fds=True)
    stdout, stderr = p.communicate()
    #返回粘贴内容
    return stdout.decode("utf-8")


