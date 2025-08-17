def data_types():
    a = 21
    c = "sber"
    b =21.21
    h = True
    d =['sber','alhpa','vtb']
    g = {"тигр": "кошачьи", "питон": "пресмыкающиеся"}
    e = (0,1,2,2)
    f = {1,2,3}
    
    
    types = [
        type(a).__name__, 
        type(c).__name__,
        type(b).__name__,
        type(h).__name__,
        type(d).__name__, 
        type(g).__name__,
        type(e).__name__, 
        type(f).__name__]

    # Выводим список
    print(types)

if __name__ == "__main__":
    data_types()