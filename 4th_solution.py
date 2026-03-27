if __name__ == '__main__':
    s = input()

    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))


# any() → retourne True si au moins un élément de l’itérable est True
# c.isalnum() → vrai si le caractère c est une lettre ou un chiffre
# for c in s → on parcourt tous les caractères de la chaîne