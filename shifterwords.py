def shifter(st):
    letters = ["H", "I", "N", "O", "S", "X", "Z", "M", "W"]
    
    shiftable = []
    for word in st.split():
        if all(letter in letters for letter in word):
            if not word in shiftable: shiftable.append(word)

    return len(shiftable), shiftable

print(shifter(""))