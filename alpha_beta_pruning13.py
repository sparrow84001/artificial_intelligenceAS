MAX, MIN = 1000, -1000

def abp(depth, node_id, max_player,values, alpha, beta):

	if depth == 3:
		return values[node_id]

	if max_player: #for max player
	
		best = MIN
		for i in range(0, 2):
			
			val = abp(depth + 1, node_id * 2 + i,False, values, alpha, beta)
			best = max(best, val)
			alpha = max(alpha, best)
			if beta <= alpha: #for Pruning
				break
		
		return best
	
	else: #for min player

		best = MAX
		for i in range(0, 2):
		
			val = abp(depth + 1, node_id * 2 + i,True, values, alpha, beta)
			best = min(best, val)
			beta = min(beta, best)
			if beta <= alpha: #for Pruning
				break
		
		return best

if __name__ == "__main__":

	values = [2,3,5,9,0,1,7,5]
	print('The optimal value is -> ', abp(0, 0, True, values, MIN, MAX))
