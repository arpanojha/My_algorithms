from string import ascii_lowercase

def breadth_first(start, goal, d, prev): # BFS adapted from CSCI B551 Fall 2021
  visited = set([start])
  fringe = [start]
  d[start] = 0
  while len(fringe) > 0:
    successor = fringe.pop(0)
    for i in graph[successor]:
      if not i in visited:
        visited.add(i)
        prev[i] = successor
        d[i] = d[successor] + 1 
        if i == goal:
          break
        fringe.append(i)
  return 

def shortest_path(start, goal):
    prev = [-1]*len(index_dict)
    d = [-1]*len(index_dict)
    if start == goal:
      return start
    breadth_first(start, goal, d, prev)
    i = goal
    return_ans=[]
    if d[goal] != -1:
      while i != -1:
        return_ans.append(index_dict[i])
        i = prev[i]
    return return_ans[::-1]

dictionary = [{} for i in range(17)]
from_to_values = []
index_dict = []
second_index = 0
while True:
	try:
		k = input()
		if k=='':
			break
		dictionary[len(k)][k] = second_index
		index_dict.append(k) 
		second_index+=1
	except EOFError:
		break

graph = [[] for i in range(len(index_dict))]
for i in range(1,17):
	items_this_list = list(dictionary[i].items())
	for j in range(len(items_this_list)):
		w,w_i = items_this_list[j]
		for m in range(i):
			for h in ascii_lowercase:
				if w[:m]!=h:
					n_w = w[:m] + h+w[m+1:]
					if n_w in dictionary[i]:
						graph[w_i].append(dictionary[i][n_w])
						graph[dictionary[i][n_w]].append(w_i)

while True:
  try:
    k = list(input().split())
    from_to_values.append([k[0],k[1]])
    #print(shortest_path(dictionary[len(k[0])][k[0]],dictionary[len(k[1])][k[1]]))
    ans = shortest_path(dictionary[len(k[0])][k[0]],dictionary[len(k[1])][k[1]])
    if ans!=[]:
      for i in ans:
        print(i)
    else:
      print("No solution.")
    print()
  except EOFError:
	  break
#print(graph)
#print(dictionary)
#print(index_dict)
#print(from_to_values)
