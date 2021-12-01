import rsa
(pubkey,privkey)=rsa.newkeys(3072)
privatekey=privkey.save_pkcs1().decode("utf8")
publickey=pubkey.save_pkcs1().decode("utf8")
if(__name__=="__main__"):
	print(privatekey,publickey,sep="\n")
