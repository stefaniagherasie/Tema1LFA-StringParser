# Tema1LFA-StringParser
[Tema1 Limbaje Formale si Automate (2020-2021, seria CB) 


Tema presupune implementarea unui parser de string-uri folosind metoda Boyer-Moore.
Pe baza lui string1 se genereaza matricea delta care se foloseste pentru a calcula
decalajul la parsarea lui string2.

#### RULARE
> ```shell
> python main.py  <input-file>  <output-file>
> ```
> **Fisierul de input** va contine:
>  - Pe prima linie se află ```string1``` pe baza căruia urmează se realizeaza funcția delta
>  - Pe a doua linie se află ```string2``` în care trebuie să se caute string1
>  
> **Fisierul de output** va contine:
>  - Pe prima linie ```valorile de decalaj``` (offset) la care se gasește string1 în string2
>    separate de câte un spațiu
    
#### IMPLEMENTARE
Constructia matricei Delta se realizeaza prin functia ```compute_delta``` care o
genereaza linie cu linie. Initial se gasesc toate prefixele posibile din pattern
(ex: pt LFA , prefixes = {0:"", 1:"L", 2:"LF", 3:"LFA"}). Apoi se creeaza fiecare linie din matrice. 
Se concateneaza fiecare prefix cu literele majuscule ale alfabetului. Pentru cuvintele obtinute se afla starea urmatoare
prin functia ```find_next_state``` care reprezinta indicele celui mai lung prefix cu care a
facut match cuvantul nostru(ex: pt word="LF" => next_st=2, pt word="LL" => next_st=0).

Functia ```find_next_state``` ia fiecare prefix din lista, in ordine inversa deoarece se
cauta cel mai lung prefix cu care se face match. Daca cuvantul dat contine un prefix,
se obtine indexul la care acesta se afla si se testeaza daca prefixul se afla la
sfarsitul cuvantului, fiind astfel cel mai lult prefix gasit. Starea urmatoare este
reprezentata de indicele prefixului gasit. Daca nu se gaseste niciunul se pune 0.

Functia ```automata_matcher``` parcurge prin o
stare curenta matricea delta, obtinand o insiruire de stari. Cand se ajunge la starea
finala, adica s-a facut match cu pattern-ul dat, se adauga intr-o lista ```offset_list```
valorile de decalaj. Acestea se scriu apoi in fisierul de iesire.
