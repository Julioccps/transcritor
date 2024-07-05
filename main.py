from cript import Cript

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
