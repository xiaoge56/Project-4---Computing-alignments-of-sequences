#coding:utf-8
import fiel1
import sys
import random
alg_HumanEyelessProtein='MQNSHSGVNQLGGVFVNGRPLPDSTRQKIVELAHSGARPCDISRILQVSNGCVSKILGRYYETGSIRPRAIGGSKPRVATPEVVSKIAQYKRECPSIFAWEIRDRLLSEGVCTNDNIPSVSSINRVLRNLASEKQQMGADGMYDKLRMLNGQTGSWGTRPGWYPGTSVPGQPTQDGCQQQEGGGENTNSISSNGEDSDEAQMRLQLKRKLQRNRTSFTQEQIEALEKEFERTHYPDVFARERLAAKIDLPEARIQVWFSNRRAKWRREEKLRNQRRQASNTPSHIPISSSFSTSVYQPIPQPTTPVSSFTSGSMLGRTDTALTNTYSALPPMPSFTMANNLPMQPPVPSQTSSYSCMLPTSPSVNGRSYDTYTPPHMQTHMNSQPMGTSGTTSTGLISPGVSVPVQVPGSEPDMSQYWPRLQ'
alg_FruitflyEyelessProtein='MRNLPCLGTAGGSGLGGIAGKPSPTMEAVEASTASHPHSTSSYFATTYYHLTDDECHSGVNQLGGVFVGGRPLPDSTRQKIVELAHSGARPCDISRILQVSNGCVSKILGRYYETGSIRPRAIGGSKPRVATAEVVSKISQYKRECPSIFAWEIRDRLLQENVCTNDNIPSVSSINRVLRNLAAQKEQQSTGSGSSSTSAGNSISAKVSVSIGGNVSNVASGSRGTLSSSTDLMQTATPLNSSESGGASNSGEGSEQEAIYEKLRLLNTQHAAGPGPLEPARAAPLVGQSPNHLGTRSSHPQLVHGNHQALQQHQQQSWPPRHYSGSWYPTSLSEIPISSAPNIASVTAYASGPSLAHSLSPPNDIESLASIGHQRNCPVATEDIHLKKELDGHQSDETGSGEGENSNGGASNIGNTEDDQARLILKRKLQRNRTSFTNDQIDSLEKEFERTHYPDVFARERLAGKIGLPEARIQVWFSNRRAKWRREEKLRNQRRTPNSTGASATSSSTSATASLTDSPNSLSACSSLLSGSAGGPSVSTINGLSSPSTLSTNVNAPTLGAGIDSSESPTPIPHIRPSCTSDNDNGRQSEDCRRVCSPCPLGVGGHQNTHHIQSNGHAQGHALVPAISPRLNFNSGSFGAMYSNMHHTALSMSDSYGAVTPIPSFNHSAVGPLAPPSPIPQQGDLTPSSLYPCHMTLRPPPMAPAHHHIVPGDGGRPAGVGLGSGQSANLGASCSGSGYEVLSAYALPPPPMASSSAADSSFSAASSASANVTPHHTIAQESCPSPCSSASHFGVAHSSGFSSDPISPAVSSYAHMSYNYASSANTMTPSSASGTSAHVAPGKQQFFASCFYSPWV'
ConsensusPAXDomain='GHGGVNQLGGVFVNGRPLPDVVRQRIVELAHQGVRPCDISRQLRVSHGCVSKILGRYYETGSIKPGVIGGSKPKVATPKVVEKIAEYKRQNPTMFAWEIRDRLLAERVCDNDTVPSVSSINRIIR'
def get_sc():
	f=open(r'C:\Users\xiaoge\Documents\GitHub\Project-4---Computing-alignments-of-sequences\alg_PAM50.txt','r')
	dat=[]
	for x in f:
		
		dat.append(x.split()[1:])
	f.close()
	dat=dat[1:]
	sc='A   R   N   D   C   Q   E   G   H   I   L   K   M   F   P   S   T   W   Y   V   B   Z   X  -'
	sc_matrix={}
	for x in sc.split():
		sc_matrix[x]={}
	for x in sc.split():
		for j in sc.split():
			
			sc_matrix[x][j]=int(dat[sc.split().index(x)][sc.split().index(j)])
	return  sc_matrix
	
# m=fiel1.compute_alignment_matrix(alg_HumanEyelessProtein,alg_FruitflyEyelessProtein,get_sc(),False)
# s=fiel1.compute_local_alignment(alg_HumanEyelessProtein,alg_FruitflyEyelessProtein,get_sc(),m)
# print s
# def ss(a):
# 	m=0
# 	lenm=len(a[1])
# 	for x,y in zip(a[1],a[2]):
# 		if x==y:
# 			m+=1
# 	print float(m)/lenm
# new_x=''
# for x in s[1]:
# 	if '-'!=x:
# 		new_x+=x
# new_y=s[2]
# print len(s[1]),len(s[2])
# m=fiel1.compute_alignment_matrix(new_x,ConsensusPAXDomain,get_sc(),True)
# s=fiel1.compute_global_alignment(new_x,ConsensusPAXDomain,get_sc(),m)
# print s,ss(s),'\n'

# m=fiel1.compute_alignment_matrix(new_y,ConsensusPAXDomain,get_sc(),True)
# s=fiel1.compute_global_alignment(new_y,ConsensusPAXDomain,get_sc(),m)
# print s,ss(s),'\n'



# import random
# randddddd1=''
# randddddd2=''
# s='ACBEDGFIHKMLNQPSRTWVYXZ'
# for x in range(len(new_y)):
# 	randddddd1+=random.choice(s)
# 	randddddd2+=random.choice(s)
# m=fiel1.compute_alignment_matrix(randddddd1,randddddd2,get_sc(),True)
# s=fiel1.compute_global_alignment(randddddd1,randddddd2,get_sc(),m)
# print s,ss(s),'\n'


def generate_null_distribution(seq_x, seq_y, scoring_matrix, num_trials):
	scoring_distribution={}
	ret=map(dosomething,[(seq_x, seq_y, scoring_matrix) for x in range(num_trials)])
	
	
	return ret
def dosomething(t):
	seq_x, seq_y, scoring_matrix=t[0],t[1],t[2]
		# seq_x_1=list(seq_x)
		# random.shuffle(seq_x_1)
		# seq_x=''.join(seq_x_1)
	seq_y_1=list(seq_y)
	random.shuffle(seq_y_1)
	seq_y=''.join(seq_y_1)
	ss=fiel1.compute_alignment_matrix(seq_x,seq_y,scoring_matrix,False)
	s=fiel1.compute_local_alignment(seq_x, seq_y, scoring_matrix, ss)
	return s[0]		
	
result=[49, 53, 44, 48, 48, 47, 47, 40, 57, 48, 50, 43, 47, 51, 39, 47, 60, 46, 54, 62, 71, 73, 44, 68, 48, 47, 45, 57, 46, 47, 59, 50, 45, 63, 51, 59, 52, 44, 52, 47, 42, 51, 45, 42, 55, 60, 48, 62, 66, 74, 50, 60, 49, 61, 49, 55, 51, 55, 46, 49, 52, 50, 62, 55, 51, 52, 50, 55, 54, 74, 52, 58, 47, 53, 58, 45, 62, 49, 44, 65, 45, 48, 45, 49, 53, 48, 58, 46, 54, 61, 52, 55, 53, 50, 56, 50, 44, 48, 49, 54, 68, 48, 41, 47, 53, 44, 53, 53, 51, 53, 46, 47, 63, 51, 46, 44, 43, 54, 51, 50, 56, 43, 51, 50, 57, 40, 50, 45, 43, 43, 52, 43, 47, 53, 51, 47, 53, 43, 45, 58, 52, 44, 65, 48, 65, 50, 52, 61, 46, 48, 51, 64, 67, 65, 50, 57, 67, 47, 56, 43, 41, 56, 44, 44, 49, 54, 47, 52, 51, 47, 50, 44, 51, 43, 42, 70, 61, 58, 53, 67, 64, 46, 52, 54, 65, 62, 64, 53, 56, 50, 48, 54, 48, 55, 58, 40, 59, 49, 54, 63, 53, 53, 53, 54, 47, 69, 43, 46, 51, 45, 48, 76, 63, 50, 46, 53, 48, 47, 51, 47, 56, 56, 52, 57, 56, 54, 51, 47, 57, 46, 49, 47, 45, 85, 49, 48, 56, 61, 53, 59, 49, 54, 52, 56, 45, 57, 50, 66, 45, 55, 52, 47, 49, 42, 46, 57, 48, 55, 53, 53, 48, 53, 57, 49, 50, 65, 49, 46, 45, 51, 57, 42, 51, 62, 47, 54, 46, 44, 51, 47, 61, 53, 53, 52, 70, 59, 54, 48, 60, 52, 59, 43, 55, 61, 45, 44, 49, 50, 70, 60, 47, 56, 52, 52, 53, 45, 59, 56, 55, 52, 92, 53, 47, 51, 44, 53, 57, 45, 48, 41, 59, 44, 65, 48, 41, 58, 40, 45, 49, 45, 55, 46, 44, 45, 51, 63, 41, 58, 50, 52, 51, 59, 53, 48, 49, 56, 49, 51, 76, 49, 54, 47, 48, 49, 49, 51, 46, 55, 70, 51, 43, 44, 56, 72, 47, 57, 59, 49, 48, 64, 61, 47, 56, 46, 44, 50, 54, 47, 51, 49, 44, 59, 52, 49, 47, 43, 65, 47, 43, 56, 54, 62, 51, 40, 56, 45, 44, 42, 47, 52, 46, 48, 55, 56, 48, 52, 40, 70, 55, 51, 45, 51, 61, 49, 74, 48, 47, 56, 47, 60, 48, 48, 50, 50, 66, 58, 46, 51, 60, 61, 46, 45, 46, 52, 55, 58, 55, 50, 56, 47, 54, 56, 56, 46, 62, 56, 45, 58, 50, 45, 49, 57, 69, 49, 42, 43, 49, 44, 47, 41, 55, 48, 60, 52, 51, 49, 54, 58, 53, 52, 48, 54, 46, 43, 45, 54, 46, 58, 51, 59, 51, 72, 51, 54, 45, 62, 59, 55, 64, 52, 58, 55, 72, 46, 55, 52, 44, 49, 44, 52, 50, 60, 49, 49, 47, 50, 46, 53, 50, 47, 51, 50, 47, 47, 60, 49, 41, 45, 45, 51, 46, 49, 48, 51, 52, 46, 54, 53, 39, 45, 45, 64, 69, 42, 49, 47, 58, 45, 51, 49, 46, 53, 46, 53, 55, 44, 46, 46, 50, 49, 56, 45, 50, 47, 46, 49, 62, 58, 56, 51, 45, 58, 46, 49, 47, 73, 47, 51, 45, 52, 58, 50, 52, 41, 51, 50, 48, 44, 47, 44, 65, 49, 42, 59, 45, 64, 50, 50, 74, 47, 57, 59, 51, 63, 44, 50, 65, 55, 46, 59, 51, 43, 48, 47, 61, 52, 45, 50, 50, 48, 58, 53, 52, 43, 45, 43, 53, 44, 55, 52, 47, 48, 50, 47, 55, 48, 55, 54, 65, 40, 50, 57, 58, 50, 49, 41, 52, 45, 51, 55, 42, 51, 45, 53, 57, 50, 53, 60, 59, 52, 63, 52, 63, 49, 62, 43, 50, 46, 44, 50, 50, 51, 44, 49, 48, 54, 48, 48, 64, 60, 51, 60, 51, 54, 44, 63, 49, 52, 52, 55, 51, 62, 43, 60, 49, 47, 64, 50, 47, 44, 50, 46, 65, 58, 52, 47, 58, 54, 53, 47, 46, 63, 48, 52, 50, 52, 68, 50, 54, 49, 56, 60, 47, 50, 52, 52, 41, 50, 53, 63, 50, 54, 69, 47, 44, 51, 46, 41, 51, 41, 56, 48, 57, 47, 48, 48, 60, 50, 69, 51, 52, 61, 44, 57, 40, 47, 51, 48, 54, 59, 51, 56, 58, 47, 48, 73, 47, 49, 47, 45, 60, 54, 58, 51, 51, 50, 43, 49, 62, 50, 52, 50, 52, 50, 41, 59, 50, 45, 57, 55, 49, 46, 56, 55, 49, 47, 51, 47, 63, 46, 44, 52, 45, 42, 53, 45, 48, 47, 46, 49, 50, 63, 42, 47, 39, 51, 49, 58, 46, 61, 52, 50, 52, 43, 49, 62, 49, 63, 54, 49, 56, 45, 58, 58, 52, 49, 51, 49, 58, 47, 43, 47, 52, 53, 45, 65, 52, 49, 45, 49, 46, 45, 46, 52, 45, 43, 55, 51, 61, 59, 53, 50, 60, 63, 50, 49, 54, 52, 66, 43, 57, 53, 46, 52, 46, 53, 52, 51, 44, 55, 56, 48, 48, 42, 61, 46, 57, 52, 53, 48, 58, 46, 53, 50, 60, 51, 52, 50, 61, 46, 58, 44, 59, 49, 50, 49, 45, 40, 50, 46, 48, 61, 70, 57, 50, 46, 47, 46, 49, 47, 52, 44, 44, 40, 48, 46, 52, 53, 42, 48, 42, 53, 49, 55, 53, 52, 51, 48, 54, 58, 47, 49, 73, 61, 49, 61, 73, 50, 49, 56, 47, 41, 47, 48, 55, 56, 52, 56, 57, 46, 46, 50, 52, 55, 43, 55, 50, 76, 51, 55, 57, 52, 59, 47, 57, 57, 64, 51, 45, 47, 54, 50, 49, 50, 53, 54, 57, 52, 50, 60, 48, 51, 52, 52, 50, 46, 43, 65, 46, 41, 47, 54, 49, 52, 58, 51, 66, 41, 57, 45]


# print generate_null_distribution(alg_HumanEyelessProtein,alg_FruitflyEyelessProtein,get_sc(),1000)
dat={}
for x in result:
	if x in dat.keys():
		dat[x]+=1
	else:
		dat[x]=1


dat=sorted(dat.iteritems(),key=lambda x:x[0],reverse=False)
def show_pic(dat):
	import matplotlib.pyplot as plt
	import numpy as np
	import math
	x=[]
	y=[]
	for s in dat:
		print s
		x.append(s[0])
		y.append(s[1])
		
	
	y_1=map(lambda y:float(y)/1000,y)
	
	plt1=plt.bar(x, y_1, alpha = 0.5, color = 'g',width = 0.8,align="center")
	ax=plt.gca() 
	plt.xticks(x,x)
	# ax.set_xticklabels( list(range(100)))
	
    # plt2,=plt.plot( x, f2, 'b',linewidth=2,label='hierarchical clustering')
    # plt3,=plt.plot( x, f3, 'g', linewidth=2,label='13')
    # print 'a'
    # plt.axis([-4, 4, -0.5, 8])
    # plt.text(1, 7.5, r'$10^x$', )
    # plt.text(2.2, 7.5, r'$e^x$')
    # plt.text(3.2, 7.5, r'$2^x$')
	# plt.legend([plt1,plt2], ["k-means",'hierarchical clustering'],loc=1)
	plt.legend([plt1], ["ratio"],loc=1)
	plt.xlabel('the ratio')
	plt.xlabel('score')
	plt.title('normalized version of this distribution')
	plt.show()


import math
mu=float(sum(result))/len(result)
s=0
for x in result:
	s+=(x-mu)*(x-mu)
	# s+=(x-mu)**(2)
sigma=math.sqrt(s/len(result))
print mu,sigma
m=fiel1.compute_alignment_matrix(alg_HumanEyelessProtein,alg_FruitflyEyelessProtein,get_sc(),False)
s=fiel1.compute_local_alignment(alg_HumanEyelessProtein,alg_FruitflyEyelessProtein,get_sc(),m)
print (s[0]-mu)/sigma