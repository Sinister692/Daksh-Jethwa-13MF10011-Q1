approvedLeaves = [
 {emp_id: 1, leaveFrom: 14-12-2020, leaveUpto: 18-12-2020},
 {emp_id: 3, leaveFrom: 22-12-2020, leaveUpto: 24-12-2020},
 {emp_id: 7, leaveFrom: 27-12-2020, leaveUpto: 30-12-2020},
 {emp_id: 29, leaveFrom: 02-12-2020, leaveUpto: 10-12-2020},
 {emp_id 45, leaveFrom: 24-02-2021, leaveUpto: 17-03-2021}
 ]
requestedLeave = {leaveFrom: 19-12-2020, leaveUpto : 20-12-2020}
l_1 = []
l_2 = []
for i in approvedLeaves:
  l_1.append(i['leaveFrom'])
for i in approvedLeaves:
  l_2.append(i['leaveUpto'])
l_3 = list(zip(l_1, l_2))
for i in range(0, len(l_3), 2):
  if (requestedLeave['leaveFrom'] >= l_3[i] and requestedLeave['leaveFrom'] <= l_3[i+1]) or (requestedLeave['leaveUpto'] >= l_3[i] and requestedLeave['leaveUpto'] <= l_3[i+1]):
    print('Leave Rejected')
    break


#First of all, we will import the leaveFrom key from the dictionary and save it in a list.
#We will save the leaveUpto values in a seperate list.
#We will use zip to match those values.
#We will check 2 values at a time by iterating through the range of length of our zipped list and giving range an increment of 2.
#If any of the leaveFrom/leaveUpto value in requestedLeave lies anywhere in between the above values, we will reject the leave, else we will add the values with the employee id to our list of dictionaries for future reference.
