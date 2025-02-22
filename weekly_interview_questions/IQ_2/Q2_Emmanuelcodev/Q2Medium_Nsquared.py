
def unique_pairs(int_list, target_sum):
    #check for None

    '''
        Time complexity: O(n^2).
        1) This is because I have a nested for loop. I search through int_list,
        and for each element in int_list I search through int_list again.
        N for the outer and n^2 with the inner.

        2) The second part of my algorithm which iteraters through the pairs and checks a dictionary is done in O(n) time.
        for x in pairs:
            if x in upairs
        I am checking n items (b/c of pairs), at O(1) time due to upairs being
        a dictionary. Overall, highest cost is O(n^2)

        Space complexity: O(n)
        1) I create another array and dictionary in the worst case n size.

    '''
    if None in (int_list, target_sum):
        raise Exception("int_list and target_sum cannot be of NoneType")

    if len(int_list) < 2:
        return []

    pairs = []

    for x in int_list:
        duplicate = False #only count num if it occurs more than once, since second loop will count current num as as second instance due it starting from begining and first loop counitng it as the first INSTANCE
        for y in int_list:

            if x == y:#counts current num in second loop, any more occurances are duplicates and therefore valid
                if duplicate == False:
                    duplicate = True
                else:
                    if x + y == target_sum:
                        pairs.append((x,y))

            else:
                if x + y == target_sum:#if current num (x) and y together == target_sum, then append group
                    pairs.append((x,y))

    #have duplicate pairs need to clean data

    upairs  = {}
    #print(pairs)
    for x in pairs:
        if x[0] < x[1]:# sorts tuple of size 2 , so n operationgs for entire loop
            if x in upairs:
                pass
            else:
                upairs[str(x)]=1
        else:
            if (x[1],x[0]) in upairs:
                pass
            else:
                upairs[str((x[1],x[0]))]=1
    pairs = []
    for x in upairs.keys():
        pairs.append(x)
    return pairs


            #duplicate pairs



print(unique_pairs([1, 3, 2, 2,3,5,5], 4))  # Returns [(3,1),(2,2)]
print(unique_pairs([3, 4, 19, 3, 4, 8, 5, 5], 6))#returns 1,1
print(unique_pairs([-1, 6, -3, 5, 3, 1], 2))  # Returns [(-1,3),(5,-3)]
print(unique_pairs([3, 4, 19, 3, 3, 3, 3], 6))  # Returns [(3,3)]
print(unique_pairs([-1, 6, -3, 5, 3, 1], 5000))  # Returns []
print(unique_pairs([], 10))  # Returns Exception
print(unique_pairs([4],54)) #returns []
print(unique_pairs(None,54))# raises Exception
