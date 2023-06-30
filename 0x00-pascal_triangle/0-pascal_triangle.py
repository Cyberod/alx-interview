#!/usr/bin/python3
""" Pascal triangle """

def pascal_triangle(n):
	"""
	Function that prints pascal's triangle
	"""
	if n <= 0:
		return []

	""" initialize an empty resulting array """
    list1 = []
    for i in range(n):
		""" initialize an empty temporary array """
        temp_list = []
        for j in range(i+1):
			""" the first and last column is always set to 1 """
            if j == 0 or j == i:
                temp_list.append(1)
            else:
				""" Add each consecutive column numbers of the previous row """
                temp_list.append(list1[i-1][j-1] + list1[i-1][j])
        list1.append(temp_list)

	return list1
