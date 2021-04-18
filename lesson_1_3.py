print('This program calculates n+nn+nnn for any n >= 0')
n_string = input('Please, enter any non-negative integer number:  ')
'''n = int(input('Input any nuber from 0 to 9:  '))
a = 3*n + 2*10*n + 100*n
print(a)

n = int(n_string)
nn_string = 2*n_string
nn = int(nn_string)
nnn_string = 3*n_string
nnn = int(nnn_string)
print('n+nn+nnn = ', n+nn+nnn)
print('Another way')'''
i = 1
s = 0
string = '0'
while i < 4:
    string = string + n_string
    n = int(string)
    s = s + n
    i = i + 1
print('n+nn+nnn = ', s)


