from port_entries import util
import sys
# from port_entries import find


# def diff_dates(port_code, date1, date2):
#     data = util.parse_data()
#     monthly_data = data[port_code]["monthly_data"][date1]
#     monthly_data1 = data[port_code]["monthly_data"][date2]
    
# #     for d in data[port_code]:
# #         if d == "monthly_data":
            
# #         else :
# #             continue
#     s = set()
#     for k in port_month:
#         s.add(k)
#     for k in port1_month:
#         s.add(k)
#     res_dict = dict()
#     if len(monthly_data) >= len(monthly_data1):
#         for k in monthly_data:
#             if k in monthly_data1.keys():
#                 res_dict[k] = monthly_data[k] - monthly_data1[k]
#             else :
#                 res_dict[k] = 0
#     else :
#         for k in monthly_data1:
#             if k in monthly_data.keys():
#                 res_dict[k] = monthly_data[k] - monthly_data1[k]
#             else :
#                 res_dict[k] = 0
    
#     return res_dict


def diff_dates(port_code, date1, date2):
    data = util.parse_data()
    monthly_data = data[port_code]["monthly_data"][date1]
    monthly_data1 = data[port_code]["monthly_data"][date2]
    
#     for d in data[port_code]:
#         if d == "monthly_data":
            
#         else :
#             continue
    # print(monthly_data)
    # print()
    # print(monthly_data1)
    s = set()
    for k in monthly_data:
        s.add(k)
    for k in monthly_data1:
        s.add(k)
    res_dict = dict()
    if len(monthly_data) >= len(monthly_data1):
        for k in s:
            if k in monthly_data1.keys():
                res_dict[k] = monthly_data[k] - monthly_data1[k]
            else :
                res_dict[k] = monthly_data[k]
    else :
        for k in s:
            if k in monthly_data.keys():
                res_dict[k] = monthly_data[k] - monthly_data1[k]
            else :
                res_dict[k] = 0 - monthly_data1[k]
    
    return res_dict




def diff_ports(port_code, port_code1, date):
    data = util.parse_data()
    port_month = data[port_code]["monthly_data"][date]
    port1_month = data[port_code1]["monthly_data"][date]
    res1_dict = dict()
    # print(port_month)
    # print()
    # print(port1_month)
    # if len(port_month) >= len(port1_month):
    #     for k in port_month:
    s = set()
    for k in port_month:
        s.add(k)
    for k in port1_month:
        s.add(k)

    if len(port_month) >= len(port1_month):
        for k in s:
            if k in port1_month.keys():
                res1_dict[k] = port_month[k] - port1_month[k]
            # elif k in port_month.keys():
            #     res1_dict[k] = port1_month[k] - port_month[k]
            else :
                res1_dict[k] = port_month[k]
    else :
        for k in s:
            if k in port_month.keys():
                res1_dict[k] = port_month[k] - port1_month[k]
            # elif k in port1_month.keys():
            #     res1_dict[k] = port1_month[k] - port_month[k]
            else :
                res1_dict[k] = 0 - port1_month[k]
    
    
    return res1_dict

def filter_by_measure(res, measure):
    measure = measure.replace("*", "")
    me = [i for i in res.keys() if measure in i]
    # print(me)
    # print(res)
    # print()
    # print()
    
    last_dict= dict()
    for m in me:
        last_dict[m] = res[m]
    return last_dict
    # for m in me:
    #     print('{:>27} : {:>10}'.format(m,res[m]))
        
        
    # print(monthly_data)
    # print(monthly_data1)
    # print(len(monthly_data))
    # print(len(monthly_data1))
    
    
    
    
def usage():
    le = len(sys.argv)
    # print(le)
    if sys.argv[1] == "-d" and sys.argv[2] and le == 5:
        res = diff_dates(int(sys.argv[2]),sys.argv[3],sys.argv[4])
        for j in res:
            # print(j, ": " ,res[j])
            s ='{:>27}'.format(j)
            print(f'{s} : {res[j]:+10d}')
            # print('{:>27} : {:>10}'.format(j,res[j]))
        # print()
        # print(res)
    elif sys.argv[1] == "-p" and sys.argv[2] and le ==5:
        res = diff_ports(int(sys.argv[2]),int(sys.argv[3]),str(sys.argv[4]))
        for j in res:
            # print(j, ": ", res[j])
            s = '{:>27}'.format(j)
            # print('{s} : {:>10}'.format(j,res[j]))
            print(f'{s} : {res[j]:+10d}')
    elif "-m" in sys.argv and len(sys.argv) == 7:
        # print(sys.argv[1:])
        if '-d' in sys.argv:
            i = sys.argv.index('-d')
            j = sys.argv.index('-m')
            res = diff_dates(int(sys.argv[i+1]), sys.argv[i+2], sys.argv[i+3])
            res1 = filter_by_measure(res,sys.argv[j+1])
            for h in res1:
                s ='{:>27}'.format(h)
                print(f'{s} : {res1[h]:+10d}')
        elif '-p' in sys.argv:
            i = sys.argv.index('-p')
            j = sys.argv.index('-m')
            res = diff_dates(int(sys.argv[i+1]), int(sys.argv[i+2]), sys.argv[i+3])
            res1 = filter_by_measure(res,sys.argv[j+1])
            for h in res1:
                s ='{:>27}'.format(h)
                print(f'{s} : {res1[h]:+10d}')
        else :
            print("Usage: python -m port_entries.compare [-d <port-code>, <date1>, <date1>] [-p <port-code1>, <port-code2>, <date>]")
        # res = diff_dates(103, "Jan 2021", "Feb 2021")
        # me = filter_by_measure(res, "*Containers*")
        
        # for m in me:
        #     print('{:>27} : {:>10}'.format(m,res[m]))
        
    else:
        print("Usage: python -m port_entries.compare [-d <port-code>, <date1>, <date1>] [-p <port-code1>, <port-code2>, <date>]")
        # print(le)
    
        
        
usage()