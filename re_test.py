import re
p = re.compile('\d{4}-\d{2}-\d{2}')
n = p.match("2021-02-15")
m = p.search("[2021-02-15 11:42:03:401] - [2021-02-15 11:42:03:401][2021-02-15 11:42:03:401][2021-02-15 11:42:03:401][2021-02-15 11:42:03:401]")
print(p.findall("[2021-02-15 11:42:03:401] - [2021-02-35 11:42:03:401][2021-12-15 11:42:03:401][2221-02-15 11:42:03:401][3021-02-15 11:42:03:401]"))
