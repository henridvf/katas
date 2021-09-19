
# 1. sort list to make split immediately useable
# 2. split each list item on '/'
# 3. loop through each part and create (nested) folder if needed

def directoryTree(lst):
    
    tree = 'Desktop\n'

    for item in sorted(lst):
        
        for part in item.split('/'):
            if not part in tree:
                if not '.' in part:
                    tree += f'\{part}'
                else:
                    

    return tree





files = [
        'meetings/2021-01-12/notes.txt',
        'meetings/2020_calendar.xlsx',
        'meetings/2021-01-12/report.pdf',
        'misc/photos/forest_20130430.jpg',
        'misc/photos/sunset_20130412.jpg',
        'scripts/tree.py',
        'meetings/2021-01-24/report.pdf',
    ]

print(directoryTree(files))
