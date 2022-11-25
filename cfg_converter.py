# list terminal for testing
listerm = ['break','const','case','catch','continue','default','delete','else','false','finally','for','function','if','let','null','return','switch','throw','try','var','while','true','=',',',';','.',':','>','<','[',']','(',')','{','}','NaN',"'",'"','&','|','new','!','variable','operation','0','1','2','3','4','5','6','7','8','9','+','-','/','%','*','float','integer','string']


def rulesparser(file):
    cfgrule = dict()
    f = open(file,'r')
    lines = f.readlines()

    for line in lines:
        if (line != "\n") :
            left, right = line.strip().split(" -> ")
            if left not in cfgrule.keys():
                cfgrule[left] = [right.split(" ")]
            else:
                cfgrule[left].append(right.split(" "))

    return cfgrule

def convert(cfg):

    # eliminate start symbol
    lefts = list(cfg.values())
    new_start = False
    for left in lefts:
        for lf in left:
            if 'S' in lf:
                cfg.update({'S0': [['S']]})
                new_start = True
                break
    
    # eliminate unit production
    unit = list()
    """ delkey = list() """
    all = cfg.items()
    for left,right in all:
        for rule in right:
            if len(rule) == 1 and rule[0] not in listerm: 
                unit.append([left,rule[0]])
                cfg[left].remove(rule)
                """ delkey.append(rule[0]) """
    
    """ delkey = list(dict.fromkeys(delkey)) """
    for change in unit:
        if (change[0] != change[1]):
            for addition in cfg[change[1]]:
                cfg[change[0]].append(addition)

    """ for change in unit:
        for rules in cfg[change[0]]:
            rules = list(map(lambda x: x.replace(change[1],change[0]), rules))

    for key in list(cfg.keys()):
        if key in delkey:
            cfg.pop(key) """

        
    # eliminate useless production
    useful = ['S','S0']
    for term in useful:
        try:
            for prod in cfg[term]:
                for prodterm in prod:
                    if prodterm not in useful and (prodterm not in listerm):
                        useful.append(prodterm)
        except (KeyError):
            continue

    left = list(cfg.keys())
    for key in left:
        if key not in useful:
            cfg.pop(key)
    
    # eliminate terminal from RHS
    rightterm = list()
    
    for left, right in cfg.items():
        for rules in right:
            if len(rules) >= 2 and any(terminal in listerm for terminal in rules):
                for rule in rules:
                    if rule in listerm:
                        rightterm.append(rule)
            """ elif len(rules) == 1 and (rules[0] in listerm):
                ruleaddition[left] = [rules[0]] """

    rightterm = list(dict.fromkeys(rightterm))
    ruleaddition = list()
    i = 0
    for term in rightterm:
        ruleaddition.append([f'X{i}',term])
        i += 1

    for newrule in ruleaddition:
        for left in cfg.keys():
            nproduct = len(cfg[left])
            for j in range(nproduct):
                if len(cfg[left][j]) >= 2:
                    cfg[left][j] = list(map(lambda x: x.replace(newrule[1],newrule[0]), cfg[left][j]))
        
        cfg.update({newrule[0]: [[newrule[1]]]})

    #eliminate more than 2 non-terminal from RHS
    j = 0
    listnew = list()
    for left in cfg.keys():
        nproduct = len(cfg[left])
        for i in range(nproduct):
            while (len(cfg[left][i]) > 2):
                prev = cfg[left][i].copy()
                new = {f'Y{j}': [[prev[0],prev[1]]]}
                
                listnew.append(new)

                for key in cfg.keys():
                    n = len(cfg[key])
                    for k in range(n):
                        item = cfg[key][k]
                        if (len(item) > 2 and (item[0] == prev[0]) and (item[1] == prev[1])):
                            cfg[key][k].pop(0)
                            cfg[key][k].pop(0)
                            cfg[key][k].insert(0, f'Y{j}')
                j += 1

    for new in listnew:
        cfg.update(new)

    if new_start:
        start_symbol = "S0"
    else:
        start_symbol = "S"

    return cfg, start_symbol

    
# test CNF result
""" cfg = rulesparser("cfg.txt")
convert(cfg)
left = list(cfg.keys())
right = list(cfg.values())
print(cfg) """