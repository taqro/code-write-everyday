K = int(input())
b = format(K, 'b')  # bの型はstrです
ans = b.replace('1', '2') # str型であるbの'1'を'2'に置き換えます
print(ans)
