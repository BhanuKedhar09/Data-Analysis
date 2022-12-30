from port_entries import util
import sys

def ports_by_state(state):
    data = util.parse_data()
    s = set()
    for d in data:
        if state in data[d]["state"]:
            t = (d, data[d]["name"] ,state)
            s.add(t)
    
    return list(s)


def ports_by_name(port_name):
    data = util.parse_data()
    state = state if state is not None else None
    se = set()
    for d in data:
        if port_name in data[d]["name"]:
            t = (d,data[d]["name"], data[d]["state"])
            se.add(t)
    return list(se)


def ports_by_name(port_name,state = None):
    data = util.parse_data()
    state = state if state is not None else None
    se = set()
    if state is not None:
        for d in data:
            if port_name in data[d]["name"] and state in data[d]["state"]:
                t = (d,data[d]["name"], data[d]["state"])
                se.add(t)
    else :
        for d in data: 
            if port_name in data[d]["name"]:
                t = (d,data[d]["name"], data[d]["state"])
                se.add(t)
    return list(se)

# ports_by_state("Idaho")
# ports_by_name('Eastport')
# ports_by_name('Eastport', state='Idaho')



# def usage():
#     l = len(sys.argv)
#     if l == 1 :
#         ports_by_state("Idaho")
#         ports_by_name('Eastport')
#         ports_by_name('Eastport', state='Idaho')
#         return False
#     elif l>1 :
    
        
    
    
    
    

# if (usage()):
#     le = len(sys.argv) 
#     if sys.argv[1] == '-s' and sys.argv[2] and le == 3:
#         res = ports_by_state(sys.argv[2])
#     elif sys.argv[1] == "-n" and sys.argv[2] and le >=3:
#         if le == 5 and sys.argv[3] == "-s" and sys.argv[4]:
#             ports_by_name(sys.argv[2],state = sys.argv[4])
#         else :
#             ports_by_name(sys.argv[2])
#     else :
#         print("Usage: python -m port_entries.find [-n <port-name>] [-s <state>]")\





def usage() :
    le = len(sys.argv) 
    if sys.argv[1] == '-s' and sys.argv[2] and le == 3:
        res = ports_by_state(sys.argv[2])
        for j in res:
            print(j[0] , ": " , j[1] , "," , j[2])
    elif sys.argv[1] == "-n" and sys.argv[2] and le >=3:
        if le == 5 and sys.argv[3] == "-s" and sys.argv[4]:
            res = ports_by_name(sys.argv[2],state = sys.argv[4])
            for j in res:
                print(j[0] , ": " , j[1] , "," , j[2])
        else :
            res = ports_by_name(sys.argv[2])
            for j in res:
                print(j[0] , ": " , j[1] , "," , j[2])
    else :
        print("Usage: python -m port_entries.find [-n <port-name>] [-s <state>]")
        
usage()