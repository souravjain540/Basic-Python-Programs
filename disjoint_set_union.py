N = 1000
P = [i for i in range(0,N+1)] # parent
S = [1 for i in range(0,N+1)] # size of set

def find(u):
	if u == P[u]:
		return u
	else:
		P[u] = find(P[u])
		return P[u]

def union(u,v):
	u = find(u)
	v = find(v)
	if u != v:
		# merge smaller set into bigger set
		if S[u] < S[v]:
			P[u] = v
			S[v] += S[u]
		else:
			P[v] = u
			S[u] += S[v]
