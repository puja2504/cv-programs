facts=[['croaks','frogs'],['eats flies','frogs'],['frogs','green'],['chirp','cannary'],['sing','cannary'],['cannary','yellow']]
def check(knowns,facts):
    R=[]
    for known in knowns:
        for A,B in facts:
            if known==A and (A,B) not in R:
                R.append((A,B))
                knowns.append(B)
    return R
print("Result:",check(['croaks','eats flies'],facts))
Result: [('croaks', 'frogs'), ('eats flies', 'frogs'), ('frogs', 'green')]

facts=[['croaks','frogs'],['eats flies','frogs'],['frogs','green'],['chirp','cannary'],['sing','cannary'],['cannary','yellow']]
def check(knowns,facts):
    R=[]
    for known in knowns:
        for A,B in facts:
            if known==B and (A,B) not in R:
                R.append((A,B))
                knowns.append(A)
    return R
print("Result:",check(['green'],facts))
Result: [('frogs', 'green'), ('croaks', 'frogs'), ('eats flies', 'frogs')]