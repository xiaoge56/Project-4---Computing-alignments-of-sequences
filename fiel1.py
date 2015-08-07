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
	table=[[0 for x in range(len_m)] for dummy_y in range(len_n)]
	if len_m==0 or len_n==0:
		return [[0]]
	if global_flag:
		for index_i in range(len_m):
			table[index_i][0]=table[index_i-1,0]+scoring_matrix[seq_x[index_i-1]]['-']
		for index_j in range(len_m):
			table[0][index_j]=table[0,index_j-1]+scoring_matrix[seq_y[index_j-1]]['-']
		for index_i in range(len_m):
			for index_j in range(len_n):
				table[index_i][index_j]=max(table[index_i-1][index_j-1]+scoring_matrix[seq_x[index_i-1]][seq_y[index_j-1]],\
					table[index_i-1][index_j]+scoring_matrix[seq_x[index_i-1]]['-'],\
					table[index_i][index_j-1]+scoring_matrix['-'][seq_y[index_i-1]])
	else:
		pass
	return table
def ComputeGlobalAlignmentScores(seq_x,seq_y,scoring_matrix):
	

# matrix=build_scoring_matrix('ahcd-',3,2,1)
# print matrix
# print matrix['a']['h']
# table=[[0 for x in range(5)] for dummy_y in range(10)]
# print table[3][2]