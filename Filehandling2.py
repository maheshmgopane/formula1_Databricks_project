
'''
file= open("/Users/hp/source/repos/Python/formula1_Databricks_project/Sample.txt",'r')
content = file.read()
print(content)
file.close()

file= open("/Users/hp/source/repos/Python/formula1_Databricks_project/Sample2.txt",'w')
content = input('Enter data to write:')
file.write(content)
print('File created and data stored')
file.close()


with open("/Users/hp/source/repos/Python/formula1_Databricks_project/Sample3.txt",'w') as file:
    content = input('Enter data to write:')
    file.write(content)
    print('File created and data stored')
with open("/Users/hp/source/repos/Python/formula1_Databricks_project/Sample3.txt",'a') as file:
    content = input('Enter data to write:')
    file.write(content)
    print('File created and data stored')

with open("/Users/hp/source/repos/Python/formula1_Databricks_project/Sample3.txt",'x') as file:
    content = input('Enter data to write:')
    file.write(content)
    print('File created and data stored')

'''

with open("/Users/hp/source/repos/Python/formula1_Databricks_project/Sample3.txt",'a') as file:
    content = input('Enter data to write:')
    file.write(content)
    print('File created and data stored')


with open("/Users/hp/source/repos/Python/formula1_Databricks_project/Sample3.txt",'a') as file:
    content = input('Enter data to write:')
    file.write(content)
    print('File created and data stored')





