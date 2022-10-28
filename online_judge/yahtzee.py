
def ones(throw): 
    return sum([i for i in throw if i==1])|0

def twos(throw): 
    return sum([i for i in throw if i==2])|0

def threes(throw): 
    return sum([i for i in throw if i==3])|0

def fours(throw):
    return sum([i for i in throw if i==4])|0

def fives(throw): 
    return sum([i for i in throw if i==5])|0

def sixes(throw): 
    return sum([i for i in throw if i==6])|0

def three_of_a_kind(throw):
    # takes care of three-five of a kind
    for i in throw:
        if throw.count(i)>=3:
            return sum(throw)
    return 0

def four_of_a_kind(throw):
    # takes care of three-five of a kind
    for i in throw:
        if throw.count(i)>=4:
            return sum(throw)
    return 0

def five_of_a_kind(throw):
    # takes care of three-five of a kind
    for i in throw:
        if throw.count(i)>=5:
            return 50
    return 0

def chance(throw):
    #takes care of chance
    return sum(throw)

def short_straight(throw):
    test = [[1,2,3,4],[2,3,4,5],[3,4,5,6]]
    for i in test:
        if all([x in throw for x in i]):
            return 25
    return 0
def long_straight(throw):
    throw.sort()
    if throw==[1,2,3,4,5] or throw==[2,3,4,5,6]:
        return 35
    return 0

def full_house(throw):
    k = {}
    for i in throw:
        if i in k.keys():
            k[i]+=1
            if k[i]>3:
                return 0
        else:
            k[i]=1
        if len(k.keys())>2:
            return 0
    return 40
scores = [ones, twos, threes, fours, fives, sixes, chance, three_of_a_kind, four_of_a_kind, five_of_a_kind, short_straight, long_straight, full_house]

def yahtzee_scores(throws):
    table=[]
    for i in throws:
        t = []
        for f in scores:
            t.append(f(i))
        table.append(t)
    return table

#memo={}
def find_best_score(games):
    s_t = yahtzee_scores(games)
    memo = {}
    total, bonus, first_cat = best_sc(0, [1]*13, 0, memo, s_t)
    b=0
    if bonus>=63:
        b=35
    score = []
    available_categories = [1]*13
    while len(score)<13:
        best_score, _, i = memo[(len(score), tuple(available_categories))]
        available_categories[i]=0
        score.append((i, s_t[len(score)][i]))
    score.sort()
    total+=b
    score = [value for cat, value in score]+[b]+[total]
    return score

def best_sc(roll, available_categories, top6, memo, s_t):
    if roll==13:
        return 0, 0, 0
    if (roll,tuple(available_categories)) in memo.keys():
        return memo[roll, tuple(available_categories)]
    scores = []
    i=0
    for free in available_categories:
        if free==0:
            i+=1
            continue
        cat_score = s_t[roll][i]
        latest_6 = top6
        if i<6:
            latest_6+=cat_score
        available_categories[i]=0 
        last_6_sc, last_6, _ = best_sc(roll+1, available_categories, latest_6, memo, s_t) 
        total = cat_score+last_6_sc        
        total_6 = latest_6+last_6   
        bonus = 0
        if total_6>=63:
            bonus+=35
        scores.append((total+bonus, total, total_6-top6, i))
        available_categories[i]=1
        i+=1
    _, best_sc_so_far, best_top_6, best_cat = max(scores)
    memo[(roll, tuple(available_categories))] = (best_sc_so_far, best_top_6, best_cat)
    return memo[(roll, tuple(available_categories))]



score = []
while True:
    i = 1
    games = []
    while i<14:
        try:
            k = [int(x) for x in input().split()]
        except EOFError:
            break
        games.append(k)
        i+=1
    if i<2:
        break
    score = find_best_score(games)
    output_string = str(score[0])
    for s in range(1,len(score)):
        output_string+=" "+str(score[s])
    #print(score)
    print(output_string)
