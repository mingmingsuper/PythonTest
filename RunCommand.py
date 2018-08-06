import subprocess

# 不需要输入输出
# print('nslookup wwww.liuandy.cn')
#
# r = subprocess.call(['nslookup', 'wwww.liuandy.cn'])
# print('Exit code', r)

# 需要输入或输出
print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\nliuandy.cn\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)
