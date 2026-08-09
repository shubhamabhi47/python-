# Python also support file handling like other languages which include different file operations like opening a file, 
# reading, writing and closing the file but before going into depth first 
# we need to understand why we do file handling what is the need of file handling.

# File is a named location on disk to store information.it store data in 
# a non-volatile memory like hard disk since we know that random access memory is a volatile 
# which will definitely losses its data when computer is turned off so that why we use files for future use of the data.

# In file handling when we want to read a file from or 
# we want to write a file first 
# we need to open that file first and when we are done 
# it needs to be closed, so that recourses that are tied with the file are freed.

# FILE OPERATIONS
# 1)Open a file
# 2)Read and Write (perform operations)
# 3)Close file




# Opening a File
# python has inbuild function to open a file. 
# This function returns a file object, also called handle. we call it handle as it is used to read or modify a file accordingly.

# f=open(‘file_name.txt’)

# we can also specify the mode in which we want to open the file. we can also specify if we want to open file in text mode or binary mode.


# Python File Mode
# ‘r’ open file for read (default)
# ‘w’ write , it create a new file if it does not exist or truncate the file if it exists.
# ‘x’ open a file for exclusive creation but if file already exists then the operation will fail.
# ‘a’ open for appending at the end of file without truncating it and if no file exist already then it create a new one.
# ‘t’ open file in text mode(default)
# ‘b’ open file in binary mode. we can use binary mode for storing matrix or list of data.
# ‘+’ open a file for updating (reading and writing)
# for example:


f=open('file_name.txt')   #equivalent to read
f=open('file_name.txt','r')
f=open('file_name.txt','w')



# Closing a File
# closing a file is done by mostly using close() method. 
# python has a garbage collector to clean up an referenced object but, we must not rely on it to close the file.

f=open('file_name.txt')
f.close()
# but the above mentioned method is not that safe and 
# we can not rely over it suppose consider a situation 
# if an exception occurs in performing some operation with the file, 
# then code exists without closing the file.so in that case 
# we should use Try…Finally block. In python when write data 
# it first go to RAM before it get stored to Hard disk and if we will not close file data will stuck to RAM which is volatile.

# we also have another way to do it using the with statement .
# it ensures that the file is closed when the block inside with is exited and 
# we do not need to explicitly call the close() method it will be done internally.







# Write to File
# we can write file by opening it in ‘w’ , ‘a’ or ‘x’ mode. 
# if we open it ‘w’ it overwrite into file if it already not exists and 
# all the previous data will be erased so we have to be more careful 
# with opening a file with ‘w’ mode. writing string or sequence of bytes 
# is done using write() method. write() returns the number of characters written to the file.

# above mention code will create a new file named “new.txt” if it is not created before. if it already exist, it is overwritten.




# Reading From a File
# There are various number of methods available for this purpose. 
# we can use read(size) method to read the size of data. if size is not specified then it returns up to the end of the file.
