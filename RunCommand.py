import subprocess

# print('nslookup wwww.liuandy.cn')
#
# r = subprocess.call(['nslookup', 'wwww.liuandy.cn'])
# print('Exit code', r)

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\nliuandy.cn\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)
