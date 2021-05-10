import string
from collections import defaultdict
import copy




cnf_final = {}
rule_final = defaultdict(list)
fact_final = defaultdict(list)
res_h = defaultdict(list)
cnf_standardizer = [0]
cnf_rule = [0]
cnf_fact = [0]





class Block:
    def __init__(self):
        self.name = ""
        self.regular = False
        self.args = []




def extra(strToken, sentence):

    ll = strToken.split("&")
    for j in ll:
        stc = ""
        if(j[0] == '('):
            for i in range(1, strlen(j)-1):
                stc += j[i]
        else:
            stc = j
        cnf_final[sentence] = stc
        # strToken = strtok(None,"&")


    return


def map_st(current, is_query,cnum):
    letters = []
    i = 0
    current = current.replace(" ", "")
    while i < len(current):
        beg = 0
        end = 0
        if(current[i].isalpha()):
            beg = i
            j = i
            while(True):

                if(current[j] in string.punctuation):
                    end = j
                    break
                j = j+1
            let = ""
            for k in range(beg, end+1):
                let += current[k]
            letters.append(let)
            i = end + 1
        else:
            i = i+1
    rf_split(letters, current,cnum)
    return




def checkPara(x,y):
    if x and y:
        return True
    else:
        return False





def sumof(pred_name,x,y,letterf):
    for i in range(x, y):
        pred_name += letterf[i]
    return pred_name




def rf_split(letters,  current,cnum):

    lvalue = ""
    add_l = []
    firstname = ""
    ele = ""
    cpart = Block()
    temp = current
    cur = [len(temp)+1]
    cur = temp
    ll = cur.split("|")
    m = 0
    zz = 0
    kk = cur.split(" ")
    pp = 0
    status = False
    t = letters.copy()
    t1 = ""

    while(t):
        t1 = t[0]
        if(t1[0].islower()):
            status = True
            break
        t.pop(0)

    while(letters):
        tmp = str(cnf_standardizer[0])

        lvalue = letters[0]
        letterf = lvalue


        XX=letterf[0].isupper()
        YY=letterf[len(lvalue)-1] == '('
        pp=checkPara(XX,YY)
        if(pp):
            firstname=sumof(firstname,0, len(lvalue)-1,letterf)
            cpart.name = firstname

        else:
            ele=sumof(ele,0, len(lvalue)-1,letterf)

            if(letterf[0].islower()):
                ele += tmp
            add_l.append(ele)
            ele = ""
        pred_part = ll[zz]
        if(letterf[len(lvalue)-1] == ')'):
            while(pred_part != None):
                if(pred_part[0] == '~'):
                    cpart.regular = False
                else:
                    cpart.regular = True
                break
            zz = zz+1


            if(status):
                while(add_l):
                    cpart.args.append(add_l[0])
                    add_l.pop(0)
                tmmp = Block()
                tmmp.name = cpart.name
                tmmp.regular = cpart.regular

                tmmp.args = (cpart.args).copy()
                

                rule_final[current].append(tmmp)



                m = m+1
            else:
                while(add_l):
                    cpart.args.append(add_l[0])
                    add_l.pop(0)

                tmmp = Block()
                tmmp.name = cpart.name
                tmmp.regular = cpart.regular
                tmmp.args = (cpart.args).copy()




                fact_final[current].append(tmmp)

                m = m+1
            firstname = ""
            cpart.name = ""
            cpart.args = []

        letters.pop(0)
    if(status):
        while(m > cnf_rule[0]):
            cnf_rule.pop(0)
            cnf_rule.append(m)
            break
    else:
        while(m > cnf_fact[0]):
            cnf_fact.pop(0)
            cnf_fact.append(m)
            break

    zzz = cnf_standardizer[0]
    cnf_standardizer.pop(0)

    cnf_standardizer.append(zzz+1)





class Unity:
    def __init__(self):
	    self.var = ""
	    self.value = ""










def cnf_convert(rule):
    converted_rule = ""

    # check for implication in a rule
    if '=>' in rule:
        implied_part = rule.split('=>')  # split into two par

        if '&' in implied_part[0]:

            # start for add negation by splitting at every and
            first = implied_part[0].split('&')
            i = 0
            while(i < len(first)):
                first[i] = first[i].strip()
                if first[i][0] == '~':
                    first[i] = first[i][1:]  # put left since double negation
                else:
                    first[i] = '~'+first[i]  # have negation
                i = i+1
            # PART AFTER IMPLICATION STAYS SAME
            first.append(implied_part[1].strip())
            z = first  # add or in between each since ands become ors with negation
        else:
            i = 0
            x = implied_part[0]
            while(i < len(implied_part)):
                implied_part[i] = implied_part[i].strip()
                i = i+1
            rest = ""
            if '~' in x:
                rest = x[1:]
            else:
                rest = '~'+x
            implied_part[0] = rest
            z = implied_part

        converted_rule = ' | '.join(z)  # implication becomes or

        return converted_rule

    # and and negation only
    elif '&' in rule:
        converted_rule = check_and(rule)

        return converted_rule

    # negation only
    elif rule[0] != ' ~':
        return rule
    else:
        return rule[1:]  # just return rest

    return converted_rule


def negation(query_line):

    ql = ""
    if(query_line[0] != '~'):
        ql = '~'+query_line
    else:
        ql = query_line[1:]

    return ql






def checker1(j):
    if j == ',' :
        return True
    
    if j == ')':
        return True
    return False



def analysis(neg):
    blockpart = Block()
    t_str = ""
    begin = -1

    temp = neg
    c_neg = []
    c_neg = temp
    ll = c_neg.split("|")

    epoint = -1
    status = False
    curr_res = defaultdict(list)
    
    for ff in range(0, len(ll)):
        pred = ll[ff]


        i = 0
        while(pred!=""):
            blockpart.regular = not (pred[0] == '~')
            i=0
            while(pred[0] == '~'):
                i = 1

                break
           
            while(i < len(pred)):
                while(pred[i].isalpha()):
                    begin = i
                    for j in range(i+1, len(pred)):
                        if(pred[j] == '('):
                            epoint = j
                            status = True
                            break
                        elif(checker1(pred[j])):
                            epoint = j
                            status = False
                            break

                    i = epoint + 1
                    t_str = ""
                    for jj in range(begin, epoint):
                        t_str += pred[jj]
                    if(status):
                        blockpart.name = t_str
                    else:
                        blockpart.args.append(t_str)
                    break
                else:
                    i = i+1
            
            tmmp = Block()
            tmmp.name = blockpart.name
            tmmp.regular = blockpart.regular
            tmmp.args = (blockpart.args).copy()

            res_h[neg].append(tmmp)
            curr_res[neg].append(tmmp)
            
            blockpart.args.clear()
            break


    return curr_res


def cmp(a, b):
    return (a > b) - (a < b)



def pred_solve(pred,value2): 
    pred += value2.name + "("
    for dd in range(0,len(value2.args)):
        if(dd > 0):
            pred += ","
        pred += value2.args[dd]
    pred += ")"
    return pred









def unity_finish(rblock,  temp,  clist,limit):
    pred = ""
    signal = True
    zzz=0
    for key2, v2 in temp.items():
        while(key2==limit):
            for value2 in v2:
                signal= not (cmp(value2.name,rblock.name) == 0 and value2.regular != rblock.regular and value2.args == rblock.args)

                while(signal):

                    if(zzz != 0):
                        pred += "|"
                    if( value2.regular==False):
                        pred += "~"
                    

                    pred=pred_solve(pred,value2)
                    break
                    


                zzz=zzz+1
            break



    for key2, v2 in clist.items():
        for value2 in v2:
            signal= not (cmp(value2.name,rblock.name) == 0 and value2.regular == rblock.regular and value2.args == rblock.args)
            while(signal):
                if(pred != ""):
                    pred += "|"
                if( value2.regular ==False):
                    pred += "~"


                pred=pred_solve(pred,value2)
                break
               

    return pred












def checkCasing(x):
    if(x.islower()):
        return "lower"
    elif(x.isupper()):
        return "upper"






def rcheck( res1,  res2,  curr_res):
    temp={}
    count = 0
    plug_in=Unity()
    uni=list()
    flag = True
    zxx=rule_final



    temp=copy.deepcopy(rule_final)
    for key2, v2 in temp.items():
        if key2==res1:
            for value2 in v2: 
                while(cmp(value2.name,res2.name) == 0 and value2.regular != res2.regular):
                    for k in range(0,len(res2.args)):
                        if((checkCasing(value2.args[k][0])=="lower")):
                            plug_in.var = value2.args[k]
                            plug_in.value = res2.args[k]
                            value2.args[k] = res2.args[k]
                            tmmp=Unity()
                            tmmp.var=plug_in.var
                            tmmp.value=plug_in.value
                            uni.append(tmmp)
                            count=count+1
                        elif(checkCasing(value2.args[k][0])=="upper"):
                            if((res2.args[k][0]).isupper() and cmp(value2.args[k],res2.args[k]) == 0):
                                count=count+1
                            elif(checkCasing(res2.args[k][0])=="lower"):
                                plug_in.var = res2.args[k]
                                plug_in.value = value2.args[k]
                                res2.args[k] = value2.args[k]
                                tmmp=Unity()
                                tmmp.var=plug_in.var
                                tmmp.value=plug_in.value
                                uni.append(tmmp)
                                count=count+1
                    break
    
    
    
    
    if(count != len(res2.args)):
        return res2.name
    for key2, value2 in curr_res.items():
        for value2 in v2:
            for k in range(0,len(uni)):
                for h in range(0, len(value2.args)):
                    if(cmp(value2.args[h], uni[k].var) == 0):
                        value2.args[h] = uni[k].value
    for key2, v2 in temp.items():
        if key2==res1:
            for value2 in v2:
                for k in range(0,len(uni)):
                    for h in range(0,len(value2.args)):
                        while(cmp(value2.args[h], uni[k].var) == 0):
                            value2.args[h] = uni[k].value
                            break
    return unity_finish(res2, temp, curr_res,res1)








def fact_check( res1,  r2,  c2):
    temp={}
    instance = 0
    u=Unity()
    uni=list()
    flag = True

    res2=copy.deepcopy(r2)
    temp = copy.deepcopy(fact_final)
    for key2, v2 in temp.items():
        if key2==res1:
            for value2 in v2: 
                if(cmp(value2.name,res2.name) == 0 and value2.regular != res2.regular):
                    for k in range(0,len(res2.args)):
                        if(cmp(value2.args[k], res2.args[k]) == 0):
                            instance=instance+1
                        elif((res2.args[k][0]).islower()):
                            u.var = res2.args[k]
                            u.value = value2.args[k]
                            res2.args[k] = value2.args[k]
                            tmmp=Unity()
                            tmmp.var=u.var
                            tmmp.value=u.value
                            uni.append(tmmp)
                            instance=instance+1
    while(instance != len(res2.args)):
        return res2.name

    cr = copy.deepcopy(c2)
    for key2, v2 in cr.items():
        for value2 in v2:
            for k in range(0,len(uni)):
                for h in range(0, len(value2.args)):
                    while(cmp(value2.args[h], uni[k].var) == 0):
                        value2.args[h] = uni[k].value
                        break
				
    return unity_finish(res2, temp, cr,res1)



















def calculate(x,y):
    return x+y-2

def check1(v1,v2,v11,v22):
    return (v1 != v2 and cmp(v11,v22) == 0)




def resolution(neg):




    if(neg == ""):
        return True
    for key, value in fact_final.items():
        
        xx=cmp(neg,key)
        if(xx != 0):
            continue
        else:
            return False



    while(res_h):
        for key, value in res_h.items():
            xx=cmp(neg,key)
            if(xx != 0):
                continue
            else: 
                return False
        break
    curr_res = analysis(neg)
    
    count = 0
    
    for key, v2 in curr_res.items():
        for value2 in v2:

            count=count+1
    ee=calculate(cnf_rule[0],cnf_fact[0])
    if(count <= ee):
        checkr = ""
        part1 = ""
        block_part=Block()
        status = True
    else:
        return False

    
    for key, v in curr_res.items():
        for value in v:
        
            for key2, v2 in fact_final.items():
                for value2 in v2:
                    if(not check1(value.regular,value2.regular,value.name,value2.name)):
                        continue
                    else:
                        part1 = key2
                        block_part = value
                        
                        checkr = fact_check(part1, block_part, curr_res)
                        
                        

                        while(cmp(checkr,block_part.name)):
                        
                            status = resolution(checkr)
                            if(status):
                                return True
                            break
        

    

    if(status):
        for key, v in curr_res.items():
            for value in v:
                for key2, v2 in rule_final.items():
                    for value2 in v2:
                        if(check1(value.regular,value2.regular,value.name,value2.name)):

                            res1 = key2
                            block_part = value
                            checkr = rcheck(res1, block_part, curr_res)

                        while(cmp(checkr,block_part.name)):
                            status = resolution(checkr)

                            if(status):
                                return True
                            break
    return False				
				
			
		
	































def resol_path( query_line):
    rcheck = resolution(negation(query_line))



    for key2, value2 in fact_final.items():
        if(cmp(query_line,key2) != 0):
            continue
        elif(cmp(query_line,key2) == 0):
            return rcheck
    if(rcheck):
        curr_res = analysis(query_line)
        for key, v in curr_res.items():
            for value in v:
                fact_final[key].append(value)
		
	
    return rcheck


















def main():

    # open file
    file_in = open("input.txt", "r")
    file_out = open("output.txt", "w")







    # number of queries want to prove
    N= int(file_in.readline())
    write_len=N-1


    # read queries
    query_list = []
    for i in range(N):
        current_query = file_in.readline().rstrip()
        query_list.append(current_query)
    

    # read rules
    K = int(file_in.readline())
    knowledge = []
    i = 0
    while i < K:
        sentence = file_in.readline().rstrip()
        # create knowledge base

        

        # knowledge.append(cnf_convert(sentence))
        extra(cnf_convert(sentence),sentence)

       
        i += 1
    cnum=0
    for key, value in cnf_final.items():
        map_st(value, False,cnum)
        cnum=cnum+1
	
# a, resolutio, uni 3, analys. neate when
    



    result = False
    res_h.clear()
    for i in range(0,N):
        
        result = resol_path(query_list[i])

        if i == write_len and result==True:
            file_out.write('TRUE')
        elif i != write_len and result==True:
            file_out.write("TRUE\n")
        elif i == write_len and result==False:
            file_out.write('FALSE')
        else:
            file_out.write("FALSE\n")
        res_h.clear()
		





if __name__ == "__main__":
    main()
