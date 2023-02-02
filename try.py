# # #FIFO page replacement algorithm implementation in python
# # #Created By: Suman Adhikari

# # print("Enter the number of frames: ",end="")
# # capacity = int(input())
# # f,fault,top,pf = [],0,0,'No'
# # print("Enter the reference string: ",end="")
# # s = list(map(int,input().strip().split()))
# # print("\nString|Frame →\t",end='')
# # for i in range(capacity):
# #     print(i,end=' ')
# # print("Fault\n   ↓\n")
# # for i in s:
# #     if i not in f:
# #         if len(f)<capacity:
# #             f.append(i)
# #         else:
# #             f[top] = i
# #             top = (top+1)%capacity
# #         fault += 1
# #         pf = 'Yes'
# #     else:
# #         pf = 'No'
# #     print("   %d\t\t"%i,end='')
# #     for x in f:
# #         print(x,end=' ')
# #     for x in range(capacity-len(f)):
# #         print(' ',end=' ')
# #     print(" %s"%pf)
# # print("\nTotal requests: %d\nTotal Page Faults: %d\nFault Rate: %0.2f%%"%(len(s),fault,(fault/len(s))*100))


# #LRU page replacement algorithm implementation in python
# #Created By: Suman Adhikari

# print("Enter the number of frames: ",end="")
# capacity = int(input())
# f,st,fault,pf = [],[],0,'No'
# print("Enter the reference string: ",end="")
# s = list(map(int,input().strip().split()))
# print("\nString|Frame →\t",end='')
# for i in range(capacity):
#     print(i,end=' ')
# print("Fault\n   ↓\n")
# for i in s:
#     if i not in f:
#         if len(f)<capacity:
#             f.append(i)
#             st.append(len(f)-1)
#         else:
#             ind = st.pop(0)
#             f[ind] = i
#             st.append(ind)
#         pf = 'Yes'
#         fault += 1
#     else:
#         st.append(st.pop(st.index(f.index(i))))
#         pf = 'No'
#     print("   %d\t\t"%i,end='')
#     for x in f:
#         print(x,end=' ')
#     for x in range(capacity-len(f)):
#         print(' ',end=' ')
#     print(" %s"%pf)
# print("\nTotal Requests: %d\nTotal Page Faults: %d\nFault Rate: %0.2f%%"%(len(s),fault,(fault/len(s))*100))


# #Optimal page replacement algorithm (OPT or OPR) implementation in python
# #Created By: Suman Adhikari

# # print("Enter the number of frames: ",end="")
# # capacity = int(input())
# # f,fault,pf = [],0,'No'
# # print("Enter the reference string: ",end="")
# # s = list(map(int,input().strip().split()))
# # print("\nString|Frame →\t",end='')
# # for i in range(capacity):
# #     print(i,end=' ')
# # print("Fault\n   ↓\n")
# # occurance = [None for i in range(capacity)]
# # for i in range(len(s)):
# #     if s[i] not in f:
# #         if len(f)<capacity:
# #             f.append(s[i])
# #         else:
# #             for x in range(len(f)):
# #                 if f[x] not in s[i+1:]:
# #                     f[x] = s[i]
# #                     break
# #                 else:
# #                     occurance[x] = s[i+1:].index(f[x])
# #             else:
# #                 f[occurance.index(max(occurance))] = s[i]
# #         fault += 1
# #         pf = 'Yes'
# #     else:
# #         pf = 'No'
# #     print("   %d\t\t"%s[i],end='')
# #     for x in f:
# #         print(x,end=' ')
# #     for x in range(capacity-len(f)):
# #         print(' ',end=' ')
# #     print(" %s"%pf)
# # print("\nTotal requests: %d\nTotal Page Faults: %d\nFault Rate: %0.2f%%"%(len(s),fault,(fault/len(s))*100))

# fcfs cpu schadulig algorithum

p_name = ['p1','p2','p3','p4']

a_time = [1,2,3,2]

b_time = [6,3,4,8]

p_q = []

s_q = []

flag = True

c_b_t = 0

for i in range(sum(b_time)):
    if(i in a_time):
        for j in range(len(a_time)):
            if(i == a_time[j]):
                p_q.append(p_name[j])
    print(s_q," <==> ",p_q)
    if(len(p_q)!=0 and flag == True):
        flag =False
        name = p_q[0]
        c_b_t = b_time[p_name.index(p_q[0])]
        p_q.remove(p_q[0])
    if(c_b_t != 0):
        s_q.append(name)
        c_b_t = c_b_t - 1
        if(c_b_t == 0):
            flag = True