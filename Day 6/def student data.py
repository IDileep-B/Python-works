def student_data(info):
    print(f'Name:{info[0]}')
    print(f'Course:{info[1]}')
    print(f'Gra_Year:{info[2]}')
    print('--------End--------')

data = [['Dileep','PFS','2026'],
        ['Ravi','JFS','2025'],
        ['Pavan','DA','2026'],
        ['Akhil','DS','2025'],
        ]
for i in data:
    student_data(i)
    
