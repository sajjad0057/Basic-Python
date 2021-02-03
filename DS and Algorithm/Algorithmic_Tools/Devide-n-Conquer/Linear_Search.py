x = ["a","b","c","d","e"]
def linear_search(x,y):
    for i in range(len(x)):
        if x[i] == y:
            return f'{y} has been exist an {i+1} possition.'
    return f'Dose not exist'
print(linear_search(x,"b"))
