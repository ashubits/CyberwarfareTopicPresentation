import pefile, malduck
pe = pefile.PE(r'C:\Users\me\Desktop\650f0d694c0928d88aeeed649cf629fc8a7bec604563bca716b1688227e0cc7e.exe')
encrypted_shellcode = pe.sections[0].get_data()[5:0x4615+5]
decrypted_shellcode = bytearray(encrypted_shellcode)
key = 0x15C13
for j in range(0x3FDF,-1,-1):
    decrypted_shellcode[j] ^= malduck.BYTE(key)
    key = malduck.rol(key + 0x92819200, 1, 32)
print(decrypted_shellcode)