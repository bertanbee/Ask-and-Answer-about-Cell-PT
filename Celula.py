import random
print(" ------------------------------------------------------------------------------------------------------\n | Seja bem vindo! Nesse quiz você deverá acertar a organela celular em que se fala.                  | \n | Serão informadas as características dessa organela e um espaço para que seja informada a resposta. |\n | Boa sorte!                                                                                         |\n ------------------------------------------------------------------------------------------------------\n\n")
while True:
    words = {
        'citoplasma': 'O espaço intracelular entre a membrana plasmática e o invólucro nuclear em seres eucariontes, enquanto nos procariontes corresponde à totalidade da área intracelular.',
        'membrana plasmática': 'Controla o que entra e o que sai do interior da célula, uma propriedade conhecida como permeabilidade seletiva. Por ser formada por uma bicamada lipídica, ela é impermeável\nà maior parte das moléculas solúveis em água.',
        'núcleo': 'Região da célula eucarionte em que ocorre o controle das atividades celulares.',
        'citoesqueleto': 'Possuem filamentos protéicos, como microtúbulos, responsáveis por dar forma à célula. Além disso, participa do transporte de substâncias.',
        'ribossomos': 'São formados a partir do RNA ribossômico e são responsáveis pela produção de proteínas. Podem ser encontrados ou aderidos a paredes do retículo endoplasmático rugoso, ou livres.',
        'retículo endoplasmático rugoso' : 'Por apresentar ribossomos ligados à sua membrana externa, também é responsável pela síntese proteica, mas a maioria das proteínas será secretada.',
        'retículo endoplasmático liso' : 'Destaca-se a síntese de lipídeos como fosfolipídeos, óleos e esteroides (incluindo os hormônios sexuais estrogênio e testosterona).',
        'complexo de golgi' : 'Localiza-se próximo ao núcleo celular e é formado por sáculos achatados e vesículas. É a organela responsável pela secreção celular.',
        'lisossomos' : 'São bolsas membranosas que contêm enzimas capazes de digerir substâncias orgânicas. Estas organelas são as responsáveis pela digestão intracelular e a sua produção excessiva pode \ndestruir uma célula por autodigestão.',
        'mitocôndria' : 'Encontrada em quase todas as células eucariotas, incluindo animais, plantas, fungos e a maioria dos protistas. Assim como os cloroplastos, esta organela possuem material genético \npróprio. Produz energia (ATP) a partir de processos metabólicos.',
        'peroxissomos' : 'Estas organelas são bolsas membranosas que contêm alguns tipos de enzimas digestivas e, além das enzimas que degradam gorduras e aminoácidos, eles possuem grande quantidade da \nenzima denominada catalase.',
        'centríolos' : 'Não são envolvidos por membrana, atuam no processo de divisão celular e também estão ligados à organização do citoesqueleto e aos movimentos de flagelos e cílios.'
    }
    sort, sorttwo = random.choice(list(words.items()))
    tries = 3
    print(sorttwo)
    guess = input("Fale a parte da célula corretamente acentuada: ")
    while guess.lower() != sort:
        tries -= 1
        if tries <= 0:
            print("Game Over! A resposta era ", "\"", sort, "\"", "!")
            break
        else:
            print("Incorreto! Tente novamente!")
            guess = input("Fale a parte a célula: ")

    if guess.lower() == sort:
        print("Correto!")