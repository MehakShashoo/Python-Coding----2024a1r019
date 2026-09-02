# wap to fill given letter template with name and date
# letter = 
'''
Dear <Name>,
You are selected!
<Date>
'''

name = input("Enter name= ")
date = input("Enter date= ")
letter = '''
Dear <Name>,
You are selected!
<Date>
'''
letter = letter.replace("<Name>" , name)
letter = letter.replace("<Date>" , date)

# print(f"""
# Dear {name},
# You are selected!
# {date} 
# """)