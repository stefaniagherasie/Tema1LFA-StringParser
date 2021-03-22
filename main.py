import sys


# Genereaza lista de prefixe pornind de la pattern
def find_prefixes(pattern):
    prefixes = []
    for i in range(0, len(pattern)):
        prefixes.append(pattern[0:i])
    return prefixes


# Functie care ne arata starea urmatoare in matricea Delta
# pornind de la o cuvantul obtinut intr-o stare
def find_next_state(state_word, prefixes):
    # Se itereaza invers pentru a obtine prefixul cel mai lung
    for i in range(len(prefixes) - 1, 0, -1):
        if prefixes[i] in state_word:
            index = len(state_word) - len(prefixes[i])
            # Se testeaza daca prefixul se afla la sfarsitul cuvantului
            if state_word[index:len(state_word)] == prefixes[i]:
                return i
    return 0


# Genereaza matricea Delta
def compute_delta(pattern):
    delta = []
    prefixes = find_prefixes(pattern)
    
    # Se creeaza linie cu linie matricea Delta
    for i in range(0, len(prefixes)):
        line = []
        for j in range(65, 91):
            # Concatenare fiecare prefix cu fiecare majuscula din alfabet
            word = prefixes[i] + str(chr(j))
            # Se gaseste starea urmatoare pentru primirea fiecarei litere
            next_st = find_next_state(word, prefixes)
            line.append(next_st)
            
        delta.append(line)
    return delta


# Genereaza lista de offset-uri
def automata_matcher(pattern, text):
    delta = compute_delta(pattern)
    current_state = 0
    offset_list = []

    # Se gasesc offset-urile prin parcurgerea matricii Delta
    for i in range(0, len(text)-1):
        # Se obtine starea urmatoare
        current_state = delta[current_state][ord(text[i]) - 65]
        # Se testeaza daca se ajunge la starea finala
        if current_state == len(pattern)-1:
            offset = i-(len(pattern)-2)
            offset_list.append(str(offset))

    return offset_list


# Deschiderea fisierului de intrare si obtinerea celor 2 string-uri
input_file = open(str(sys.argv[1]), "r")
string1 = input_file.readline()
string2 = input_file.readline()
input_file.close()


# Obtinerea valorilor de decalaj
offset_list = automata_matcher(string1, string2)


# Deschiderea fisierului de iesire si scrierea informatiilor
output_file = open(str(sys.argv[2]), "w")
for offset in offset_list:
    output_file.write(offset)
    output_file.write(" ")
output_file.write("\n")
output_file.close()
