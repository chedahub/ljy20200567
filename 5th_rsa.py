p = 11
q = 13
n = p * q
phi_n = (p-1) * (q-1)

# e: 1 < e < phi_n && phi_n과 서로소
# 서로소: 공약수가 1밖에 없다
# 유클리드 호제법: gcd(a,b) = gcd(b,r), a = b*q + r
for e in range(1, phi_n):
    r1 = e  # 피제수 a
    r2 = phi_n  # 제수 b
    while (r2 > 0):  # 나머지가 0이 되면 종료
        qq = r1/r2  # 몫 (a/b)
        r = r1 - qq * r2  # 나머지 (a-q*b)
        r1 = r2  # 제수 b
        r2 = r  # 나머지 r

    if r1 == 1:
        break

print('e: ', e)

e = 7
d = 0
mod = 0
while True:
    d += 1
    mod = (e*d) % phi_n
    if mod == 1:
        break

print('d :', d)

# Encryption
# C = P^e mod n

plain = "CAU CPS DIST"
plain_list = [ord(x) for x in plain]

cipher = []
for i in plain_list:
    x = (i ** e) % n
    cipher.append(int(x))


# Decryption
# P = C^d mod n

decrypted = []
for i in cipher:
    x = (i ** d) % n
    decrypted.append(int(x))


print('plain text', plain_list)
print('cipher text', cipher)
print('decrypted text', decrypted)

# 숫자를 아스키코드로 바꿔준다.
# 문자가 하나씩 나오지 않도록(문자열로 출력되도록) join 함수를 사용해준다.
decrypted_text = ''.join([chr(x) for x in decrypted])
print(decrypted_text)
