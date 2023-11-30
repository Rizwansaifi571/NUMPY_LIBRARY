"""                   ---> GETTING STARTED WITH NUMPY. <---                     """


# import numpy
# arr=numpy.array([1, 2, 3, 4, 5])
# print(arr)
# print(type(arr))


# import numpy as np
# print(np.__version__)

# import numpy
# arr=numpy.array({1, 2, 3, 4, 5})
# print(arr)
# print(type(arr))



"""                     --->   Dimension in Arrays   <---                     """

""" --> 0-D Array """

# import numpy as np
# arr=np.array(45)
# print(arr)

""" --> 1-D Array """

# import numpy as np
# arr=np.array([1, 2, 3, 4, 5])
# print(arr)

# --> 2-D Array

# import numpy as np
# arr=np.array([[1, 2, 3],[4, 5, 6]])
# print(arr)


""" --> 3-D Array  """

# import numpy as np
# arr=np.array([[[1, 2, 3],[4, 5, 6]],[[1, 2, 3],[4, 5, 6]]])
# print(arr)

"""----------------------------

Ques: Check Number Of Dimension? """
# import numpy as np
# a=np.array(48)
# b=np.array([1, 2, 3])
# c=np.array([[1, 2, 3],[4, 5, 6]])
# d=np.array([[[1, 2, 3],[4, 5, 6]],[[1, 2, 3],[4, 5, 6]]])
# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)


""" --> Higher Dimesional Array  """

# import numpy as np
# arr=np.array([1, 2, 3, 4],ndmin=5)
# print(arr)
# print("Number of dimension :",arr.ndim)



"""                     --->   NumPy Array Indexing   <---                    """

""" --> 1-D Array  """


# import numpy as np
# arr=np.array([1, 2, 3, 4])
# print(arr[1])
# print(arr[2]+arr[3])   


""" --> 2-D Array  """


# import numpy as np
# arr=np.array([[1, 2, 3, 4],[5, 6, 7, 8]])
# print("2nd Element on 1st Row : ",arr[0,1])


""" --> 3-D Array  """

# import numpy as np
# arr=np.array([[[1, 2, 3],[4, 5, 6]],[[7, 8, 9],[10, 11, 12]]])
# print(arr[0,1,2])


""" --> Negaive Indexing  """

# import numpy as np
# arr=np.array([[1, 2, 3, 4],[5, 6, 7, 8]])
# print("1st Element on 2nd Row : ",arr[1,0])
# print("1st Element on 2nd Row : ",arr[-1,-4])



"""                      --->   NumPy Array Slicing   <---                    """


# import numpy as np
# arr=np.array([1, 2, 3, 4, 5])
# print(arr[1:4])


# import numpy as np
# arr=np.array([1, 2, 3, 4, 5, 6, 7])
# print(arr[4: ])
# print(arr[ :4])
# print(arr[-3:-1])
# print(arr[1:5:2])
# print(arr[ : :2])


""" --> 2-D Array  """

# import numpy as np
# arr=np.array([[1, 2, 3, 4, 5],[6, 7, 8, 9, 10]])
# print(arr[1,1:4])


# import numpy as np
# arr=np.array([[1, 2, 3, 4, 5],[6, 7, 8, 9, 10]])
# print(arr[0:2,2])

# import numpy as np
# arr=np.array([[1, 2, 3, 4, 5],[6, 7, 8, 9, 10]])
# print(arr[0:2,1:4])


"""                      --->   Data Types in NumPy   <---                    """


""" --> Checking Data-Type  """

# import numpy as np
# arr1=np.array([1, 2, 3, 4])
# arr2=np.array(["apple","b","c"])
# print(arr1,arr1.dtype)
# print(arr2,arr2.dtype)


""" --> Creating Array With a Define Data Type  """

# import numpy as np
# arr=np.array([1, 2, 3, 4],dtype="S")
# print(arr)
# print(arr.dtype)

# import numpy as np
# arr1=np.array([1, 2, 3, 4])
# arr2=np.array([1, 2, 3, 4],dtype="i2")
# print(arr1)
# print(arr1.dtype)
# print(arr2)
# print(arr2.dtype)



"""              ---> Converting Data-Type on Exisitng Array <---             """

# import numpy as np
# arr=np.array([1, 2, 3, 4])
# newarr1=arr.astype("i")
# newarr2=arr.astype("int")
# print(newarr1,newarr2)
# print(newarr1.dtype)

# import numpy as np
# arr=np.array([1, 0, 3])
# newarr=arr.astype(bool)
# print(newarr)
# print(newarr.dtype)



"""                   ---> NumPy Array Copy VS View <---                      """

""" --> Copy  """

# import numpy as np
# arr=np.array([1, 2, 3, 4, 5])
# x=arr.copy()
# arr[0]=9
# print(arr)
# print(x)


""" --> View  """

# import numpy as np
# arr=np.array([1,2,3,4,5])
# x=arr.view()
# arr[0]=9
# print(arr)
# print(x)


""" --> If Array owns its Data  """

# import numpy as np
# arr=np.array([1, 2, 3, 4, 5])
# x=arr.copy()
# y=arr.view()
# print(x.base)
# print(y.base)



"""                        ---> NumPy Array Shape <---                        """

# import numpy as np
# arr=np.array([[1, 2, 3, 4],[5, 6, 7, 8]])
# print(arr.shape)


# import numpy as np
# arr=np.array([1, 2, 3, 4],ndmin=5)
# print(arr)
# print("shape of array :",arr.shape)


""" --> Reshaping From 1-D to 2-D  """

# import numpy as np
# arr=np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# newarr=arr.reshape(4,3)
# print(newarr)


""" --> Reshaping From 1-D to 3-D  """

# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# newarr = arr.reshape(2, 3, 2)
# print(newarr)


""" --> Reshaping of array is copy or view? """

# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# arr=arr.reshape(2, 4)
# print(arr.base)
# print(arr)


""" --> Unkown Dimension """

# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# newarr = arr.reshape(2, 2, -1)
# print(newarr)


""" --> Flatering The Array """

# import numpy as np
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# newarr = arr.reshape(-1)
# print(newarr)


"""                    ---> NumPy Array Iterating <---                        """

""" --> Iterating 1-D Array """

# import numpy as np
# arr=np.array([1, 2, 3])
# for x in arr:
#     print(x)


""" --> Iterating 2-D Array """

# import numpy as np
# arr=np.array([[1, 2, 3],[4, 5, 6]])
# for x in arr:
#     print(x)


# import numpy as np
# arr=np.array([[1, 2, 3],[4, 5, 6]])
# for x in arr:
#     for y in x:
#         print(y)



""" --> Iterating 3-D Array """

# import numpy as np
# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# for x in arr:
#   print("x represents the 2-D array:")
#   print(x)


# import numpy as np
# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# for x in arr:
#   for y in x:
#     for z in y:
#       print(z)


""" --> Iterating Array using nditer() """

# import numpy as np
# arr=np.array([[[1, 2],[3, 4]],[[5, 6],[7, 8]]])
# for x in np.nditer(arr):
#     print(x)


""" --> Iterating Array with different data type """

# import numpy as np
# arr=np.array([1, 2, 3])
# for x in np.nditer(arr,flags=['buffered'],op_dtypes=["S"]):
#     print(x)


""" --> Iterating Array with different step size """

# import numpy as np
# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# for x in np.nditer(arr[:, ::2]):
#   print(x)


""" --> ndenumerate function. """

# import numpy as np
# arr=np.array([1, 2, 3])
# for idx,x in np.ndenumerate(arr):
#     print(idx,x)

# import numpy as np
# arr=np.array([[1, 2, 3, 4],[5, 6, 7, 8]])
# for idx,x in np.ndenumerate(arr):
#     print(idx,x)


"""                       ---> NumPy Joining Array <---                       """

""" --> for 1-D """

# import numpy as np
# arr1=np.array([1, 2, 3])
# arr2=np.array([4, 5, 6])
# arr=np.concatenate((arr1,arr2))
# print(arr)

""" --> for 2-D """

# import numpy as np
# arr1=np.array([[1, 2],[3, 4]])
# arr2=np.array([[5, 6],[7,8]])
# arr=np.concatenate((arr1,arr2),axis=0)
# arr3=np.concatenate((arr1,arr2))
# print(arr)
# print(f"\n{arr3}")


""" --> Joining array using stack function """

# import numpy as np
# arr1=np.array([1, 2, 3])
# arr2=np.array([4, 5, 6])
# arr3=np.stack((arr1,arr2),axis=1)
# arr4=np.stack((arr1,arr2))
# arr5=np.concatenate((arr1,arr2))
# print(arr3)
# print(f"\n{arr4}")
# print(f"\n{arr5}")


""" --> Stacking Along Rows """

# import numpy as np
# arr1=np.array([1, 2, 3])
# arr2=np.array([4, 5, 6])
# arr=np.hstack((arr1,arr2))
# print(arr)


""" --> Stacking Along Columns """

# import numpy as np
# arr1=np.array([1, 2, 3])
# arr2=np.array([4, 5, 6])
# arr=np.vstack((arr1,arr2))
# print(arr)


""" --> Stacking Along Height """

# import numpy as np
# arr1=np.array([1, 2, 3])
# arr2=np.array([4, 5, 6])
# arr=np.dstack((arr1,arr2))
# print(arr)



"""                    ---> NumPy Spilitting Array <---                       """

# import numpy as np
# arr=np.array([1, 2, 3, 4, 5, 6])
# newarr=np.array_split(arr,3)
# print(newarr)


""" --> Array with less element """

# import numpy as np
# arr=np.array([1, 2, 3, 4, 5, 6])
# newarr=np.array_split(arr,4)
# print(newarr)


""" --> Only split function """

"""Not recommended in numpy"""
# import numpy as np
# arr=np.array([1, 2, 3, 4, 5, 6])
# newarr=np.split(arr,3)
# print(newarr)


""" --> Split Into Array """

# import numpy as np
# arr=np.array([1, 2, 3,4 , 5, 6])
# newarr=np.array_split(arr,3)
# print(newarr)
# print(newarr[0])
# print(newarr[1])
# print(newarr[2])


""" --> Splitting 2-D Array """

# import numpy as np
# arr=np.array([[1, 2],[3, 4],[5, 6],[7, 8],[9, 10],[11, 12]])
# newarr=np.array_split(arr,3)
# print(newarr)


""" --> Splitting 2-D Array with axis """

# import numpy as np
# arr=np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9],[10, 11, 12],[13, 14, 15],[16, 17, 18]])
# newarr1=np.array_split(arr,3,axis=1)
# newarr2=np.array_split(arr,3,axis=0)
# print(newarr1)
# print(f"\n{newarr2}")


""" --> Splitting 2-D Array with h,v,d split() """

# import numpy as np
# arr=np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9],[10, 11, 12],[13, 14, 15],[16, 17, 18]])
# newarr1=np.hsplit(arr,3)
# newarr2=np.vsplit(arr,3)
# # newarr3=np.dsplit(arr,3)  """not work minimum 3 dimesnion need."""
# print(newarr1)
# print(f"\n{newarr2}")
# # print(f"\n{newarr3}")



"""                    ---> NumPy Searching Array <---                       """


# import numpy as np
# arr=np.array([1, 2, 3, 4, 5, 4, 4])
# x=np.where(arr==4)
# print(x)

# import numpy as np
# arr=np.array([1, 2, 3, 4, 5, 6, 7, 8])
# x=np.where(arr%2==0)
# y=np.where(arr%2==1)
# print("odd",y)
# print("even",x)


""" --> Search Sorted """

# import numpy as np
# arr=np.array([6, 7, 8, 9])
# x=np.searchsorted(arr,7)
# print(x)


""" --> Search from right side """

# import numpy as np
# arr=np.array([6, 7, 8, 9])
# x=np.searchsorted(arr,7,side='right')
# print(x)


""" --> Multiple Values """

# import numpy as np
# arr=np.array([1, 3, 5, 7])
# x=np.searchsorted(arr,[2, 4, 6])
# print(x)
# print(arr)



"""                    ---> NumPy Sorting Array <---                       """

# import numpy as np
# arr=np.array([3, 2, 0, 1])
# print(np.sort(arr))

# import numpy as np
# arr1=np.array(["banana","cherry","apple"])
# arr2=np.array([ True,True,False ])
# print(np.sort(arr1))
# print(np.sort(arr2))


""" --> for 2D Array """

# import numpy as np
# arr=np.array([[3, 2, 4],[5, 0, 1]])
# print(np.sort(arr))



"""                    ---> NumPy Filter Array <---                       """

# import numpy as np
# arr=np.array([41, 42, 43, 44])
# x=[True, False, True, False]
# newarr=arr[x]
# print(newarr)

# import numpy as np
# arr=np.array([41, 42, 43, 44])
# f_arr=[]
# for elements in arr:
#     if elements>42:
#         f_arr.append(True)
#     else:
#         f_arr.append(False)
# newarr=arr[f_arr]
# print(f_arr)
# print(newarr)


""" --> Directly Substitute """

# import numpy as np
# arr=np.array([41, 42, 43, 44])
# f_arr=arr>42
# newarr=arr[f_arr]
# print(f_arr)
# print(newarr)






"""------------------------------------------------------------
---------------------------------------------------------------
---------------------------------------------------------------
---------------------------------------------------------------
---------------NUMPY TUTORIAL THE END-----------------------"""