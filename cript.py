
class Cript:
    def __init__(self):
        pass
    @staticmethod
    def cript_txt(palavra: str):
        txt_cript = ''

        u_palavra = palavra.upper()
        for i in range(len(palavra)):
            if u_palavra[i] == 'A':
                txt_cript += 'ekr5r'
            elif u_palavra[i] == 'B':
                txt_cript += '4r4r4'
            elif u_palavra[i] == 'C':
                txt_cript += 'pqqqp'
            elif u_palavra[i] == 'D':
                txt_cript += '4rrr4'
            elif u_palavra[i] == 'E':
                txt_cript += '5q5q5'
            elif u_palavra[i] == 'F':
                txt_cript += '5q5qq'
            elif u_palavra[i] == 'G':
                txt_cript += 'pqxrp'
            elif u_palavra[i] == 'H':
                txt_cript += 'rr5rr'
            elif u_palavra[i] == 'I':
                txt_cript += '5eee5'
            elif u_palavra[i] == 'J':
                txt_cript += '5eeuz'
            elif u_palavra[i] == 'K':
                txt_cript += 'suyus'
            elif u_palavra[i] == 'L':
                txt_cript += 'qqqq5'
            elif u_palavra[i] == 'M':
                txt_cript += 'r1vrr'
            elif u_palavra[i] == 'N':
                txt_cript += 'ryvtr'
            elif u_palavra[i] == 'O':
                txt_cript += 'orrro'
            elif u_palavra[i] == 'P':
                txt_cript += '4r4qq'
            elif u_palavra[i] == 'Q':
                txt_cript += 'orroc'
            elif u_palavra[i] == 'R':
                txt_cript += 'or4sr'
            elif u_palavra[i] == 'S':
                txt_cript += 'pqob4'
            elif u_palavra[i] == 'T':
                txt_cript += '5eeee'
            elif u_palavra[i] == 'U':
                txt_cript += 'rrrro'
            elif u_palavra[i] == 'V':
                txt_cript += 'aarke'
            elif u_palavra[i] == 'W':
                txt_cript += 'rr1vr'
            elif u_palavra[i] == 'X':
                txt_cript += 'rkekr'
            elif u_palavra[i] == 'Y':
                txt_cript += 'rkeee'
            elif u_palavra[i] == 'Z':
                txt_cript += '5cei5'
            elif u_palavra[i] == ' ':
                txt_cript += 'aaaaa'
            if i < (len(palavra) - 1):
                txt_cript += "'"
                
            
        return txt_cript
    @staticmethod
    def enterp_cript(txt_crip: str):
        linhas_ltr = []

        for i in range(0, len(txt_crip)):
            if txt_crip[i] == 'a':
                linha_ltr = ('     ')
                linhas_ltr.append(linha_ltr)
            elif txt_crip[i] == 'b':
                linha_ltr = ('    #')
                linhas_ltr.append(linha_ltr)
            elif txt_crip[i] == 'c':
                linha_ltr = ('   # ')
                linhas_ltr.append(linha_ltr)
            elif txt_crip[i] == 'd':
                linha_ltr = ('   ##')
                linhas_ltr.append(linha_ltr)
            elif txt_crip[i] == 'e':
                linha_ltr = ('  #  ')
                linhas_ltr.append(linha_ltr)
            elif txt_crip[i] == 'f':
                linha_ltr = ('  # #')
                linhas_ltr.append(linha_ltr)
            elif txt_crip[i] == 'g':
                linha_ltr = ('  ## ')
                linhas_ltr.append(linha_ltr)
            elif txt_crip[i] == 'h':
                linha_ltr = ('  ###')
                linhas_ltr.append(linha_ltr)
            elif txt_crip[i] == 'i':
                linha_ltr = (' #   ')
                linhas_ltr.append(linha_ltr)
            elif txt_crip[i] == 'j':
                linha_ltr = (' #  #')
                linhas_ltr.append(linha_ltr)
            elif txt_crip[i] == 'k':
                linha_ltr = (' # # ')
                linhas_ltr.append(linha_ltr)
            elif txt_crip[i] == 'l':
                linha_ltr = (' # ##')
                linhas_ltr.append(linha_ltr)
            elif txt_crip[i] == 'm':
                linha_ltr = (' ##  ')
                linhas_ltr.append(linha_ltr)
            elif txt_crip[i] == 'n':
                linha_ltr = (' ## #')
                linhas_ltr.append(linha_ltr)
            elif txt_crip[i] == 'o':
                linha_ltr = (' ### ')
                linhas_ltr.append(linha_ltr)
            elif txt_crip[i] == 'p':
                linha_ltr = (' ####')
                linhas_ltr.append(linha_ltr)
            elif txt_crip[i] == 'q':
                linha_ltr = ('#    ')
                linhas_ltr.append(linha_ltr)
            elif txt_crip[i] == 'r':
                linha_ltr = ('#   #')
                linhas_ltr.append(linha_ltr)
            elif txt_crip[i] == 's':
                linha_ltr = ('#  # ')
                linhas_ltr.append(linha_ltr)
            elif txt_crip[i] == 't':
                linha_ltr = ('#  ##')
                linhas_ltr.append(linha_ltr)
            elif txt_crip[i] == 'u':
                linha_ltr = ('# #  ')
                linhas_ltr.append(linha_ltr)
            elif txt_crip[i] == 'v':
                linha_ltr = ('# # #')
                linhas_ltr.append(linha_ltr)
            elif txt_crip[i] == 'w':
                linha_ltr = ('# ## ')
                linhas_ltr.append(linha_ltr)
            elif txt_crip[i] == 'x':
                linha_ltr = ('# ###')
                linhas_ltr.append(linha_ltr)
            elif txt_crip[i] == 'y':
                linha_ltr = ('##   ')
                linhas_ltr.append(linha_ltr)
            elif txt_crip[i] == 'z':
                linha_ltr = ('##  #')
                linhas_ltr.append(linha_ltr)
            elif txt_crip[i] == '0':
                linha_ltr = ('## # ')
                linhas_ltr.append(linha_ltr)
            elif txt_crip[i] == '1':
                linha_ltr = ('## ##')
                linhas_ltr.append(linha_ltr)
            elif txt_crip[i] == '2':
                linha_ltr = ('###  ')
                linhas_ltr.append(linha_ltr)
            elif txt_crip[i] == '3':
                linha_ltr = ('### #')
                linhas_ltr.append(linha_ltr)
            elif txt_crip[i] == '4':
                linha_ltr = ('#### ')
                linhas_ltr.append(linha_ltr)
            elif txt_crip[i] == '5':
                linha_ltr = ('#####')
                linhas_ltr.append(linha_ltr)
            elif txt_crip[i] == "'":
                linha_ltr = ('     ')
                linhas_ltr.append(linha_ltr)
        return linhas_ltr
    
    def draw(self, txt_crip: str, modo: int):
        if modo == 1:
            parts = txt_crip.split("'")
            separated_texts = ['' for _ in range(5)]
            
            for part in parts:
                for i in range(5):
                    separated_texts[i] += part[i] + "'"
            
            separated_texts = [text.rstrip("'") for text in separated_texts]

            interpreted_lines = [''.join(self.enterp_cript(line)) for line in separated_texts]

            final_result = '\n'.join(interpreted_lines)
            
            return final_result


cript = Cript()

def main():
    escl = input('O que você quer fazer? criptografar, descriptografar ou transcrever? (crip/descrip/transc)')
    if escl == 'crip':
        txt1 = input('Digite o txto que você quer criptografar:')
        crip_txt1 = cript.cript_txt(txt1)
        print(crip_txt1)
    elif escl == 'descrip':
        txt2 = input('Digite o texto que você quer descriptografar: ')
        desc_txt1 = cript.draw(txt2, 1)
        print(desc_txt1)
    elif escl == 'transc':
        txt3 = input('Digite o texto que você quer transcrever: ')
        crip_txt2 = cript.cript_txt(txt3)
        desc_txt2 = cript.draw(crip_txt2, 1)
        print(desc_txt2)
    resp = input('Mais algo (s/n)')
    if resp == 's':
        main()

if __name__ == '__main__':
    main()
