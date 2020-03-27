import jieba

if __name__=='__main__':
	jieba.set_dictionary('./dictionary/dict.txt.big.txt')
	jieba.load_userdict('./dictionary/NameDict.txt')

	f=open('./dragon8/第十二章　從此醉.txt','r',encoding='UTF-8')
	o=open('12.txt','w',encoding='utf-8')

	# with open('./dragon8/ch1.txt','r',encoding='UTF-8') as f:
	for i in f:
		sen=jieba.cut(i)
		sen=' '.join(sen)
		o.write(sen+'\n')
	
	f.close()
	o.close()
	# s=f.readline()
	# sen=jieba.cut(s)
	# sen=' '.join(sen)
	# print(sen)