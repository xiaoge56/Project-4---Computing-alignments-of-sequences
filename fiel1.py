'project4'
#coding:utf-8
def build_scoring_matrix(alphabet, diag_score, off_diag_score, dash_score):
	'build a scoring matrix which will be used in project4'
	scoring_matrix={}
	new_alphabet=set(alphabet)
	new_alphabet.add('-') 
	for charactor_row in new_alphabet:
		scoring_matrix[charactor_row]={}
		for charator_col in new_alphabet:
			# print charactor_row,charator_col
			if charactor_row ==charator_col :
				if '-' ==charactor_row:
					scoring_matrix[charactor_row][charator_col]=dash_score
				else:
					scoring_matrix[charactor_row][charator_col]=diag_score
			else:
				if '-' in [charactor_row,charator_col]:
					scoring_matrix[charactor_row][charator_col]=dash_score
				else:
					scoring_matrix[charactor_row][charator_col]=off_diag_score
	return scoring_matrix
def compute_alignment_matrix(seq_x, seq_y, scoring_matrix, global_flag):
	'computes either a global alignment matrix or a local alignment matrix depending on the value of global_flag.'
	len_m=len(seq_x)
	len_n=len(seq_y)
	# table=[[0 for x in range(len_m)] for dummy_y in range(len_n)]
	if len_m==0 or len_n==0:
		return [[0]]
	if global_flag:
		gas=ComputeGlobalAlignmentScores(seq_x,seq_y,scoring_matrix)
		return computAlingment(seq_x,seq_y,scoring_matrix,gas)
	else:
		gas=ComputeLocalAlignmentScores(seq_x,seq_y,scoring_matrix)
		
	return gas
	


def ComputeGlobalAlignmentScores(seq_x,seq_y,scoring_matrix):
	'compute the socre for alignment matrix '
	len_m=len(seq_x)
	len_n=len(seq_y)
	print seq_x,seq_y
	alignment_matrix=[[0 for dummy_x in range(len_n+1)] for dummy_y in range(len_m+1)]
	print len_m,len_n,scoring_matrix,alignment_matrix
	alignment_matrix[0][0]=0
	print alignment_matrix
	for x in range(1,len_m+1):
		alignment_matrix[x][0]=alignment_matrix[x-1][0]+scoring_matrix[seq_x[x-1]]['-']
	for y in range(1,len_n+1):
		alignment_matrix[0][y]=alignment_matrix[0][y-1]+scoring_matrix['-'][seq_y[y-1]]
	for x in range(1,len_m+1):
		for y in range(1,len_n+1):
			alignment_matrix[x][y]=max(alignment_matrix[x-1][y]+scoring_matrix[seq_x[x-1]]['-'],alignment_matrix[x][y-1]+scoring_matrix['-'][seq_y[y-1]],alignment_matrix[x-1][y-1]+scoring_matrix[seq_x[x-1]][seq_y[y-1]])
	return alignment_matrix

def ComputeLocalAlignmentScores(seq_x,seq_y,scoring_matrix):
	'compute the socre for alignment matrix '
	len_m=len(seq_x)
	len_n=len(seq_y)
	alignment_matrix=[[0 for x in range(len_n+1)] for dummy_y in range(len_m+1)]
	alignment_matrix[0][0]=0
	for x in range(1,len_m+1):
		alignment_matrix[x][0]=max(alignment_matrix[x-1][0]+scoring_matrix[seq_x[x-1]]['-'],0)
	for y in range(1,len_n+1):
		alignment_matrix[0][y]=max(alignment_matrix[0][y-1]+scoring_matrix['-'][seq_y[y-1]],0)
	for x in range(1,len_m+1):
		for y in range(1,len_n+1):
			alignment_matrix[x][y]=max(0,alignment_matrix[x-1][y]+scoring_matrix[seq_x[x-1]]['-'],alignment_matrix[x][y-1]+scoring_matrix['-'][seq_y[y-1]],alignment_matrix[x-1][y-1]+scoring_matrix[seq_x[x-1]][seq_y[y-1]])
	return alignment_matrix

def computAlingment(seq_x,seq_y,scoring_matrix,AlignmentScores):
	'use the correct socre to retun the alingment X and Y'

	len_m=len(seq_x)
	len_n=len(seq_y)
	X=''
	Y=''
	while len_m!=0 and len_n!=0:
		if AlignmentScores[len_m][len_n]==AlignmentScores[len_m-1][len_n-1]+scoring_matrix[seq_x[len_m-1]][seq_y[len_n-1]]:
			X=seq_x[len_m-1]+X
			Y=seq_y[len_n-1]+Y
			len_m=len_m-1
			len_n=len_n-1
		else:
			if AlignmentScores[len_m][len_n]==AlignmentScores[len_m-1][len_n]+scoring_matrix[seq_x[len_m-1]]['-']:
				X=seq_y[len_m-1]+X
				Y='-'+Y
				len_m=len_m-1
			else:
				X='-'+X
				Y=seq_y[len_n-1]+Y
				len_n=len_n-1
	while len_m!=0:
		X=seq_x[len_m-1]+X
		Y='-'+Y
		len_m=len_m-1
	while len_n!=0:
		Y=seq_y[len_n-1]+Y
		X='-'+X
		len_n=len_n-1
	return (X,Y)
			
def	compute_global_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix):
	'compute the global alignment for input seq_x,seq_y'
	gas=compute_alignment_matrix(seq_x, seq_y, scoring_matrix,True)
	return computAlingment(seq_x,seq_y,scoring_matrix,gas)
	
def compute_local_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix):
	'compute the local alignment for input seq_x,seq_y'
	gas=compute_alignment_matrix(seq_x, seq_y, scoring_matrix,False)
	return computAlingment(seq_x,seq_y,scoring_matrix,gas)
	
# alphabet=set(list('ACGT'))
# diag_score=5
# off_diag_score=2
# dash_score=-2
# sc=build_scoring_matrix(alphabet, diag_score, off_diag_score, dash_score)
# sc['-']['A']=(-4)
# sc['-']['C']=(-4)
# sc['-']['G']=(-4)
# sc['-']['T']=(-4)
# sc['-']['-']=(5)
# as1=ComputeGlobalAlignmentScores('AC','TAG',sc)	
# xx=computAlingment('AC','TAG',sc,as1)
# print xx



# aa=compute_alignment_matrix('AC','TAG',sc,0)
# print aa









# matrix=build_scoring_matrix('ahcd-',3,2,1)
# print matrix
# print matrix['a']['h']
# table=[[0 for x in range(5)] for dummy_y in range(10)]
# print table[3][2]