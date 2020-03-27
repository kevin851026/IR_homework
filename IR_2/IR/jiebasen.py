import jieba

if __name__=='__main__':
	jieba.set_dictionary('./dictionary/dict.txt.big.txt')
	jieba.load_userdict('./dictionary/NameDict.txt')

	for i in range(50):
		s = './newdra8/'
		ns=''
		s = s + str(i+1) + '.txt'
		ns = ns + str(i+1) + '.txt'
		f=open(s,'r',encoding='UTF-8')
		o=open(ns,'w',encoding='utf-8')

		# with open('./dragon8/ch1.txt','r',encoding='UTF-8') as f:
		l = 0
		for j in f:
			sen=jieba.cut(j)
			sen=' '.join(sen)
			# print(sen.split()[1:])
			# print(len(sen.split()[1:]))
			o.write(sen)
		
		f.close()
		o.close()
	print(l)
	# s=f.readline()
	# sen=jieba.cut(s)
	# sen=' '.join(sen)
	# print(sen)