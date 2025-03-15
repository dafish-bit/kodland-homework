print('Bienvenido a el diccionario meme,  escribe la palabra que no entienda y se le dira el significado de tal palabra')
meme_dict = {
    'CRINGE': 'Es la verguenza ajena',
    'LOL': 'Es reirse a carcajadas',
    'BRB': '"Be Right Back", es vuelvo al tiro', 
    'ROFL': 'Es una respuesta a una broma',
    'SHEEESH': 'Es una ligera desaprobacion',
    'AGGRO': 'Ponerse agresivo/enojado',
    'CREEPY': 'Es espeluznante en español'
}
for i in range(5):
    word = input('Escribe una palabra que no entiendas:').upper()
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print('Esa palabra no la conozco')
