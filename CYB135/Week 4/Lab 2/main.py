def all_permutations(permList, nameList):
    # TODO: Implement method to create and output all permutations of the list of names.
    if len(nameList) == 0:
        p_str = ''
        for i in range(len(permList)):
            p_str += permList[i]
            if i < len(permList):
                p_str += ' '
        print(p_str)
    else:
        for i in range(len(nameList)):
            p_name = nameList[i]
            r_names = nameList[:i] + nameList[i+1:]
            all_permutations(permList + [p_name], r_names)
    
    

if __name__ == "__main__": 
    nameList = input().split(' ')
    permList = []
    all_permutations(permList, nameList)
