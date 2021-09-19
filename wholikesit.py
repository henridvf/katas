def likes(names):
    cnt = len(names)
    
    if cnt == 0:
        display_text = 'no one likes this'
    elif cnt == 1:
        display_text = f'{names[0]} likes this'
    elif cnt == 2:
        display_text = f'{names[0]} and {names[1]} like this'
    elif cnt == 3:
        display_text = f'{names[0]}, {names[1]} and {names[2]} like this'
    elif cnt > 3:
        display_text = f'{names[0]}, {names[1]} and {str(cnt - 2)} others like this'
        
    return display_text



# print(likes([])) # must be "no one likes this"
# print(likes(["Peter"])) # must be "Peter likes this"
# print(likes(["Jacob", "Alex"])) # must be "Jacob and Alex like this"
# print(likes(["Max", "John", "Mark"])) # must be "Max, John and Mark like this"
print(likes(["Alex", "Jacob", "Mark", "Max"])) # must be "Alex, Jacob and 2 others like this"