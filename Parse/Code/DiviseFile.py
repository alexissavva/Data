import re

class DiviseFile :
    
    def __init__(self,fichier,s):
        self.name_file = fichier
        self.regex = s
    
    def parse_file(self):
        fregex = open("regex_binetflow2.txt", "w")
        no_regex = open("noregex_binetflow2.txt", "w")
        with open(self.name_file, 'r') as file:
            for ligne in file:
                if self.regex in ligne:
                    fregex.write(ligne)
                else:
                    no_regex.write(ligne)
        fregex.close()
        no_regex.close()
        print('Fin')