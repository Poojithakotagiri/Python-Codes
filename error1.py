# Python code to catch an exception and handle it using try and except code blocks  
	   
a = ["Python", "Exceptions", "try and except"]  
    try:  
	#looping through the elements of the array a, choosing a range that goes beyond the length of the array  
	    for i in range( 4 ):  
	    print( "The index and element from the array is", i, a[i] )  
	#if an error occurs in the try block, then except block will be executed by the Python interpreter       
    except:  
	print ("Index out of range")  
