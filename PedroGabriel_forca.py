import tkinter as tk
from random import choice
from PIL import Image, ImageTk
from tkinter.messagebox import *
run = True
while run:
    #SORTEIA A PALAVRA SECRETA
    with open("forca.txt") as arquivo:
        palavras = arquivo.readlines()
    palavraSorteada = choice(palavras).strip()
    sem_repeticao = set(palavraSorteada)
    letras_erradas = ""
    letras_utilizadas = ""
    dificuldade = None
    #PEGA A DIFICULDADE ESCOLHIDA PELO JOGADOR
    def start_game(difficulty):
        global dificuldade
        dificuldade = difficulty
        print(f"Jogador escolheu {difficulty}")   
        # Destroi a janela 
        difficulty_window.destroy()
    #FUNÇÃO RESPONSÁVEL POR ATUALIZAR A LETRA LA PALAVRA SECRETA
    def atualizar_palavra(letra):
        global palavraSorteada
        
        for i, char in enumerate(palavraSorteada.strip()):
            if char == letra:
                letras_label[i].config(text=letra)
    #FUNÇÃO RESPONSÁVEL POR CHECAR SE A LETRA ESTÁ NA PALAVRA SECRETA
    #Checa se a letra está na palavra
    def checar_letra(letra):
        global palavraSorteada
        for i, char in enumerate(palavraSorteada.strip()):
            if char == letra:
                return True
        return False
    # FUNÇÃO QUE GUARDA AS LETRAS CLICADAS E REDICIONA-AS
    def letra_capturada(letra):
        global palavraSorteada, letras_erradas, letras_utilizadas
        if checar_letra(letra):
            atualizar_palavra(letra)
            letras_utilizadas += letra
            letras_utilizadas_label.config(text="Letras corretas: " + letras_utilizadas)
        #VERIFICAR SE ELE VENCEU!!!!
            if len(letras_utilizadas) == len(sem_repeticao):
                letras_utilizadas_label.config(text="Letras Corretas - VOCÊ ACERTOU A PALAVRA!")
                jogarNovamente()
        else:
            max_erros = set_max_errors(dificuldade)
            letra_errada(letra, max_erros)
    #MEMORIZA A DIFICULDADE ESCOLHIDA E GUARDA A QUANTIDADE MAXIMA DE ERROS QUE O JOGADOR PODE POSSUIR
    def set_max_errors(dificuldade):
        if dificuldade == "normal":
            return 6
        elif dificuldade == "tormento":
            return 4
        elif dificuldade == "inferno":
            return 2
        elif dificuldade == "nightmare":
            return 1
        #SE A LETRA ESTIVER ERRADA ELE VEM PARA CÁ
    erros = 0
    def letra_errada(letra, max_erros):
        global letras_erradas, erros
        #ADICIONA AS LETRAS AS LETRAS ERRADAS
        letras_erradas += letra
        # VERIFICA SE O NUMERO DE ERROS E IGUAL AO MAXIMO PERMITIDO
        if len(letras_erradas) == max_erros:
            letras_erradas_label.config(text="Letras erradas - VOCÊ PERDEU!")
            atualizar_imagem(erros=6)
            jogarNovamente()
            for button in buttons:
                button.config(state="disabled")
        else:
            erros += 1
            atualizar_imagem(erros) #ATUALIZA IMAGEM DA FORCA
            # AATUALIZA LABEL DE PALAVRAS ERRADAS
            letras_erradas_label.config(text="Letras erradas: " + letras_erradas)
    def jogarNovamente():
        global run
        result = tk.messagebox.askquestion(title="Jogar novamente", message="Deseja jogar novamente?")
        if result =='yes':
            run = True
            window.destroy()
        else:
            run = False
            window.destroy()

    # CRIA JANELA DE DIFICULDADE
    difficulty_window = tk.Tk()
    difficulty_window.title("Escolha a dificuldade")
    difficulty_window.geometry("300x300")

    difficulty_title = tk.Label(difficulty_window, text="Escolha a dificuldade:")
    difficulty_title.pack(pady=20)
    instruction_text = tk.Label(difficulty_window, text="Selecione a dificuldade do jogo:")
    instruction_text.pack()

    # CRIA OS BOTOES DE DIFICULDADE
    normal_button = tk.Button(difficulty_window, text="Normal", command=lambda: start_game("normal"))
    normal_button.pack(side="top", pady=10)
    torment_button = tk.Button(difficulty_window, text="Tormento", command=lambda: start_game("tormento"))
    torment_button.pack(side="top", pady=10)
    inferno_button = tk.Button(difficulty_window, text="Inferno", command=lambda: start_game("inferno"))
    inferno_button.pack(side="top", pady=10)
    nightmare_button = tk.Button(difficulty_window, text="Nightmare", command=lambda: start_game("nightmare"))
    nightmare_button.pack(side="top", pady=10)

    difficulty_window.mainloop()

    #JANELA PRINCIPAL
    window = tk.Tk()
    window.title("Jogo Da Forca")
    window.geometry("1000x850")


    #COR E FUNDO
    background_color = "#2ecc71"
    foreground_color = "#ffffff"
    foreground_color2= "#000"

    #COFIG DOS BOTOES
    button_width = 2
    button_height = 1 
    button_font = ("Helvetica", 16)
    button_color = ("#2ecc71")

    #CONFIGURAÇÕES DOS FRAMES
    top_frame = tk.Frame(window)
    top_frame.pack(side="top", fill="both", expand=True)
    title_frame = tk.Frame(top_frame)
    title_frame.pack(side="top", fill="both", expand=True)
    title_label = tk.Label(title_frame, text="BEM VINDO AO JOGO DA FORCA", font=("Helvetica", 20, "bold"), bg=background_color, fg=foreground_color)
    title_label.pack(side="top", pady=15)

    #CONFIG DAS LABELS
    letras_utilizadas_label = tk.Label(title_frame, text="Letras corretas: ", font=("Helvetica", 20, "bold"), bg=background_color, fg=foreground_color)
    letras_utilizadas_label.pack(side="top", pady=15)
    word_frame = tk.Frame(top_frame)
    word_frame.pack(side="bottom")
        #FRAME PARA AS PALAVRAS ERRADAS
    wrong_frame = tk.Frame(window)
    wrong_frame.pack(side="left", fill="both")
    #FRAME BOTOES
    button_frame = tk.Frame(word_frame)
    button_frame.pack(side="bottom", fill="both", expand=True)
        #PALAVRAS ERRADAS
    letras_erradas_label = tk.Label(wrong_frame, text="Letras erradas:", font=("Helvetica", 20, "bold"), bg=background_color, fg=foreground_color)
        #CONFIG PALAVRAS ERRADAS
    letras_erradas_label.pack(side="left", pady=20)

        #SETANDO A PRIMEIRA FOTO DA FORCA
    image_label = tk.Label(title_frame)
    image_label.pack(side="top", pady=15)
    image = Image.open("forca0.png")
    photo = ImageTk.PhotoImage(image)
    image_label.config(image=photo)
    image_label.image = photo  # Evita o garbage collector remover a imagem da memória ME SALVOU ISSO AAAAAAAAAA

    def atualizar_imagem(erros):
        image = Image.open(f"forca{erros}.png")
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.image = photo

        #SETANDO AS LETRAS NA TELA
    buttons = []
    for i in range(26):
        letra = chr(65 + i)
        button = tk.Button(button_frame, text=letra, width=button_width, height=button_height, font=button_font, bg=button_color, fg=foreground_color2, command=lambda letra=letra: letra_capturada(letra))
        button.grid(row=i//13, column=i%13)
        buttons.append(button)
        # DESABILITA O BOTAO APOS O PRIMEIRO CLICK
        button.config(state="normal", command=lambda button=button, letra=letra: [letra_capturada(letra), button.config(state="disabled")])


        # FRAME PARA A PALAVRA SECRETA
    word_frame = tk.Frame(top_frame)
    word_frame.pack(side="bottom")

        # LINHA PARA CADA LETRA DA PALAVRA SECRETA
    letras_label = []
    for i in range(len(palavraSorteada)):
        letter_label = tk.Label(word_frame, text="_", font=("Helvetica", 20),fg=foreground_color2)
        letter_label.grid(row=0, column=i, padx=10, pady=90)
        letras_label.append(letter_label)
    window.mainloop()