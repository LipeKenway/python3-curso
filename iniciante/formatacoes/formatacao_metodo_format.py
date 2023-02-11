a = 'A'
b = 'B'
c = 1.1

string = '| a = {0} | b = {tipo2} | c = {tipo3:.2f} |'
formato = string.format(a, tipo2=b, tipo3=c)

print(formato)