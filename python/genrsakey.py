import rsa
def pemkeys(size=3072):
	(pubkey,privkey)=rsa.newkeys(size)
	return(privkey.save_pkcs1().decode("utf8"),pubkey.save_pkcs1().decode("utf8"))
if(__name__=="__main__"):
	keys=pemkeys()
	print(keys[0],keys[1],sep="\n")
