# Sa se afiseze index-ul elementului cautat in Array, chiar daca acesta apare de mai multe ori.
# Date de intrare: 1, 2, 2, 3, 4, 5, 2
# Date de iesire: 1, 2, 6
# Punctul il obtine prima persoana care incarca codul in Assigment. Asta nu trebuie sa va impiedice sa incarcati codul.

haystack = [1, 2, 2, 3, 4, 5, 2]
needle = 2
indexFind = []
for i in range(len(haystack)):
    if (int(haystack[i]) == int(needle)):
        indexFind.append(i)

print("afisare pozitii element gasit: ", indexFind)

# daca trebuie formatate exact ca si in cerinta "1, 2, 6"
converted_list = [str(element) for element in indexFind]
joined_string = ", ".join(converted_list)

print("lista concatenata:", joined_string)
