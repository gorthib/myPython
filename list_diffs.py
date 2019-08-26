#!/usr/bin/python

'''This program takes in 2 lists as input (listA and listB) and returns three lists as output

   	Common : All elements which are common between listA and listB

   	Removed : In listA but not in listB

	Added : In listB but not in listA
'''

import sys, ast

from collections import Counter


#--------------------------------------
#  Functions 
#--------------------------------------

def usage():

  print("\tThis function takes two lists as parameters\n")

  print("\tUsage: ./list_diffs.py \"[listA]\" \"[listB]\"\n")

  print("\tEx: ./list_diffs.py \"[5, 5, 6, 7, 7, 8, 9, 9, 9]\"  \"[5, 6, 7, 9, 9, 9, 9]\" \n")

  exit(1)


def validate_args(arg):

    arr = ast.literal_eval( arg )

    if type(arr).__name__ != 'list':
		print "\n\tERROR:\n\n\tInvalid Argument type: \n"
		usage()
		
    return arr


def sub_lists(list1):

    """
    This function returns a sub lists of 
    :param listA: list
    :returns: sorted list 
    """
    sublist = [[]]

    for i in range(len(list1) + 1):
        for j in range(i + 1, len(list1) + 1):
            sub = list1[i:j]
            sublist.append(sub)

    return sorted(sublist, key=len)


def diff_lists(list1, list2):
    """
    This function collects items in list1, but not in list2
    :param listA: list
    :returns: sorted list 
    """
    sublist = [[]]

    count = Counter(list1) # Total count in list1

    count.subtract(list2)  # subtract items that are in list2

    diff = []

    for x in list1:
    	if count[x] > 0:
    		count[x] -= 1
    		diff.append(x)

    return diff

#--------------------------------------
#  Main 
#--------------------------------------

def main():

    listA = validate_args(sys.argv[1])

    listB = validate_args(sys.argv[2])
    
    new_list = []

    for item in sub_lists(listB):
    	if item in sub_lists(listA):
    		new_list.append(item)

    sorted_items = sorted([list(item) for item in set(tuple(row) for row in new_list)], key=len)

    #--------------------------------------
    # Get common items from listA and listB 
    #--------------------------------------
	
    common_items = []

    for item in sorted_items:
		if len(item) == len(sorted_items[-1]):
			common_items.extend(item)

    print "\n\tCommon items:  " + str(common_items)  + "\n"


    #-----------------------------------------------
    # Get removed items from listA, but not in listB 
    #-----------------------------------------------
	
    removed_items = diff_lists(listA, common_items)

    print "\n\tRemoved items:  " + str(removed_items)  + "\n"


    #-------------------------------------------
    # Get added items in listB, but not in listA 
    #-------------------------------------------
	
    added_items = diff_lists(listB, common_items)

    print "\n\tAdded items:  " + str(added_items)  + "\n"


if __name__ == "__main__":
    sys.exit(main())


# Local Variables:
# tab-width:4
# indent-tabs-mode:nil
# End:
# vim: set expandtab tabstop=4 shiftwidth=4
