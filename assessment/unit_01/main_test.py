
import util

# -----------------------------------------------
# loading data and preparing to analyze
# -----------------------------------------------
# list of objects
opt = []

# total number of options
totalSysNum = 5

nameList = ['Amazon','SpaceX','NASA','Raytheon','Northrop Grumman']
procList = [5, 6, 1, 2, 3]
speedList = [10, 10, 10, 10, 15]
switchList = [1, 1, 3, 4, 2]


# loop through list of objects
# loop through 5 numbers
# i = 0, 1, 2, 3, 4, 5
for i in range(totalSysNum):
    option = util.Option()

    # load data from specific file
    option.set_name(nameList[i])
    option.set_processors(procList[i])
    option.set_speed(speedList[i])
    option.set_switches(switchList[i])

    opt.append(option)

# opt = [option1, option2, option3, ...]

# -----------------------------------------------
# massage the data
# -----------------------------------------------
# obj = option1, option2, option3, ...

# we want the option with the most processors
maxProcIdx = 0
maxNumProc = 0
for idx in range(totalSysNum):
    currentProcNum = opt[idx].processors

    if currentProcNum > maxNumProc:
        maxNumProc = currentProcNum
        maxProcIdx = idx

print('The Company that offers the most processors is: {}'.format( opt[maxProcIdx].name ))
#print(opt[maxProcIdx])