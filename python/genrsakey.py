import rsa
(pubkey,privkey)=rsa.newkeys(3072)
print(privkey.save_pkcs1().decode("utf8"))
print(pubkey.save_pkcs1().decode("utf8"))
