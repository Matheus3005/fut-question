from ast import main
import tkinter as tk
from tkinter import messagebox
import random

# Lista de perguntas e respostas para cada nível de dificuldade
perguntas = {
    "Fácil": [
        {"pergunta": "Qual país ganhou a Copa do Mundo de 2002?", "opcoes": ["Brasil", "Alemanha", "França", "Itália"], "correta": "Brasil", "pontos": 1},
        {"pergunta": "Qual jogador é conhecido como 'O Rei do Futebol'?", "opcoes": ["Maradona", "Pelé", "Messi", "Cristiano Ronaldo"], "correta": "Pelé", "pontos": 1},
        {"pergunta": "Em que ano ocorreu a primeira Copa do Mundo?", "opcoes": ["1920", "1930", "1940", "1950"], "correta": "1930", "pontos": 1},
        {"pergunta": "Qual é o maior estádio de futebol do Brasil?", "opcoes": ["Maracanã", "Morumbi", "Mineirão", "Beira-Rio"], "correta": "Maracanã", "pontos": 1},
        {"pergunta": "Qual seleção tem o apelido de 'La Roja'?", "opcoes": ["Espanha", "Chile", "México", "Argentina"], "correta": "Espanha", "pontos": 1},
        {"pergunta": "Qual jogador brasileiro é conhecido como 'Fenômeno'?", "opcoes": ["Romário", "Rivaldo", "Ronaldinho", "Ronaldo"], "correta": "Ronaldo", "pontos": 1},
        {"pergunta": "Quantos minutos tem um tempo regular de uma partida de futebol?", "opcoes": ["45", "60", "90", "120"], "correta": "90", "pontos": 1},
        {"pergunta": "Qual clube é conhecido como 'O Rei de Copas'?", "opcoes": ["Real Madrid", "Barcelona", "Boca Juniors", "Liverpool"], "correta": "Boca Juniors", "pontos": 1},
        {"pergunta": "Qual país venceu a Copa do Mundo de 2018?", "opcoes": ["Brasil", "Croácia", "França", "Alemanha"], "correta": "França", "pontos": 1},
        {"pergunta": "Qual seleção é conhecida como 'Azzurra'?", "opcoes": ["Brasil", "Itália", "Argentina", "França"], "correta": "Itália", "pontos": 1}
    ],
    "Médio": [
        {"pergunta": "Quantas vezes o Brasil ganhou a Copa do Mundo?", "opcoes": ["3", "4", "5", "6"], "correta": "5", "pontos": 2},
        {"pergunta": "Quem ganhou a Bola de Ouro em 2021?", "opcoes": ["Messi", "Lewandowski", "Cristiano Ronaldo", "Neymar"], "correta": "Messi", "pontos": 2},
        {"pergunta": "Qual foi o placar da final da Copa do Mundo de 2014 entre Alemanha e Argentina?", "opcoes": ["1-0", "2-1", "3-1", "0-0"], "correta": "1-0", "pontos": 2},
        {"pergunta": "Qual jogador é conhecido como 'O Fenômeno'?", "opcoes": ["Rivaldo", "Romário", "Ronaldinho", "Ronaldo"], "correta": "Ronaldo", "pontos": 2},
        {"pergunta": "Quantos gols Pelé marcou em sua carreira profissional?", "opcoes": ["700", "1000", "1281", "1500"], "correta": "1281", "pontos": 2},
        {"pergunta": "Qual clube inglês é conhecido como 'Red Devils'?", "opcoes": ["Liverpool", "Arsenal", "Chelsea", "Manchester United"], "correta": "Manchester United", "pontos": 2},
        {"pergunta": "Qual seleção tem mais títulos da Copa América?", "opcoes": ["Brasil", "Uruguai", "Argentina", "Chile"], "correta": "Uruguai", "pontos": 2},
        {"pergunta": "Qual jogador marcou o 'Gol do Século' em 1986?", "opcoes": ["Maradona", "Pelé", "Zico", "Beckenbauer"], "correta": "Maradona", "pontos": 2},
        {"pergunta": "Qual foi o país anfitrião da Copa do Mundo de 1966?", "opcoes": ["Brasil", "Alemanha", "Inglaterra", "França"], "correta": "Inglaterra", "pontos": 2},
        {"pergunta": "Qual time foi campeão da Libertadores em 2019?", "opcoes": ["Grêmio", "River Plate", "Boca Juniors", "Flamengo"], "correta": "Flamengo", "pontos": 2}
    ],
    "Difícil": [
        {"pergunta": "Qual país sediou a Copa do Mundo de 1978?", "opcoes": ["Argentina", "Alemanha", "México", "Itália"], "correta": "Argentina", "pontos": 3},
        {"pergunta": "Qual clube tem mais títulos da UEFA Champions League?", "opcoes": ["Real Madrid", "Barcelona", "Milan", "Liverpool"], "correta": "Real Madrid", "pontos": 3},
        {"pergunta": "Quem é o maior artilheiro da história da Copa do Mundo?", "opcoes": ["Pelé", "Ronaldo", "Miroslav Klose", "Gerd Muller"], "correta": "Miroslav Klose", "pontos": 3},
        {"pergunta": "Qual foi o primeiro clube europeu a vencer a Copa Intercontinental?", "opcoes": ["Real Madrid", "Milan", "Benfica", "Barcelona"], "correta": "Real Madrid", "pontos": 3},
        {"pergunta": "Em que ano a UEFA Champions League foi criada?", "opcoes": ["1955", "1960", "1970", "1980"], "correta": "1955", "pontos": 3},
        {"pergunta": "Quantas Copas do Mundo Zinedine Zidane disputou?", "opcoes": ["1", "2", "3", "4"], "correta": "3", "pontos": 3},
        {"pergunta": "Quantos gols foram marcados na final da Copa do Mundo de 1958?", "opcoes": ["2", "5", "6", "7"], "correta": "7", "pontos": 3},
        {"pergunta": "Quem é o único jogador a ganhar a Copa do Mundo como jogador e técnico?", "opcoes": ["Beckenbauer", "Zidane", "Maradona", "Cruyff"], "correta": "Beckenbauer", "pontos": 3},
        {"pergunta": "Quem é o jogador com mais partidas em Copas do Mundo?", "opcoes": ["Cafú", "Maldini", "Lothar Matthäus", "Ronaldo"], "correta": "Lothar Matthäus", "pontos": 3},
        {"pergunta": "Qual foi o resultado da final da Liga dos Campeões de 2005 entre Milan e Liverpool?", "opcoes": ["3-3", "1-1", "2-2", "4-3"], "correta": "3-3", "pontos": 3}
    ]
}


class QuizGame:
    def __init__(self):
        self.pontuacao = 0
        self.perguntas_respondidas = 0
        self.perguntas_total = 0
        self.dificuldade_atual = ""
        self.nome_jogador = ""
        self.historico = []
        self.tempo_limite = 15
        self.tempo_restante = 0
        self.timer_label = None
        self.temporizador_ativo = False  # Controla se o temporizador está ativo
        self.pontuacao = 0
        self.resposta_correta = "resposta_exemplo"
        self.temporizador_ativo = True

    def iniciar_jogo(self):
        self.escolher_dificuldade()

    def selecionar_dificuldade(self, dificuldade):
        self.dificuldade_atual = dificuldade
        self.perguntas_total = len(perguntas[dificuldade])
        random.shuffle(perguntas[dificuldade])
        self.mostrar_pergunta(0)

    def mostrar_pergunta(self, indice):
        if indice < self.perguntas_total:
            pergunta_info = perguntas[self.dificuldade_atual][indice]
            self.pergunta_atual = pergunta_info
            pergunta_texto = pergunta_info["pergunta"]
            opcoes = pergunta_info["opcoes"]
            self.tempo_restante = self.tempo_limite

            pergunta_window = tk.Toplevel()
            pergunta_window.title("Perguntas de Futebol")
            pergunta_window.attributes('-fullscreen', True)
            pergunta_window.config(bg="#1e1e5e")

            frame_fundo = tk.Frame(pergunta_window, bg="#1e1e5e")
            frame_fundo.pack(fill="both", expand=True)

            pergunta_label = tk.Label(frame_fundo, text=pergunta_texto, bg="#1e1e5e", fg="#FFD700",
                                      font=("Arial", 36, "bold"), wraplength=800)
            pergunta_label.place(relx=0.5, rely=0.2, anchor="center")

            self.timer_label = tk.Label(frame_fundo, text=f"Tempo: {self.tempo_restante} s", bg="#1e1e5e", fg="white",
                                         font=("Arial", 24, "bold"))
            self.timer_label.place(relx=0.5, rely=0.1, anchor="center")

            for idx, opcao in enumerate(opcoes):
                opcao_button = tk.Button(frame_fundo, text=opcao,
                                         command=lambda o=opcao, i=indice: self.verificar_resposta(o, i),
                                         bg="#3a3ab7", fg="white", font=("Arial", 24, "bold"), relief="raised", bd=3)
                opcao_button.place(relx=0.5, rely=0.4 + (idx * 0.1), anchor="center")
                opcao_button.bind("<Enter>", lambda e, b=opcao_button: b.config(bg="#5a5ab7"))
                opcao_button.bind("<Leave>", lambda e, b=opcao_button: b.config(bg="#3a3ab7"))

            sair_button = tk.Button(frame_fundo, text="SAIR", command=pergunta_window.destroy, bg="#FF0000",
                                    fg="white", font=("Arial", 16, "bold"), relief="raised", bd=3)
            sair_button.place(relx=0.9, rely=0.05, anchor="center")

            self.iniciar_temporizador()

        else:
            self.finalizar_jogo()


    def iniciar_temporizador(self):
        self.temporizador_ativo = True
        self.atualizar_temporizador()

    def atualizar_temporizador(self):
        if self.tempo_restante and self.temporizador_ativo > 0:
            self.timer_label.config(text=f"Tempo restante: {self.tempo_restante} segundos")
            self.tempo_restante -= 1
            self.timer_label.after(1000, self.atualizar_temporizador)
        elif self.tempo_restante <= 0 :
            self.perguntas_respondidas += 1
            messagebox.showinfo("Tempo Esgotado", "Você não respondeu a tempo!")
            self.game_over()

    def verificar_resposta(self, opcao, indice):
        self.temporizador_ativo = False  # Desativa o temporizador ao responder
        if opcao == self.pergunta_atual["correta"]:
            self.pontuacao += self.pergunta_atual["pontos"]
            messagebox.showinfo("Resultado", f"Correto! Você ganhou {self.pergunta_atual['pontos']} pontos.")
            self.perguntas_respondidas += 1
            self.mostrar_pergunta(self.perguntas_respondidas)
        else:
            messagebox.showinfo("Resultado", f"Incorreto! A resposta correta é: {self.pergunta_atual['correta']}")            
            self.registrar_nome()  # Solicita o nome após a resposta errada
            self.game_over()  # Chama o método de game over após a solicitação do nome
                        
    def game_over(self):
        game_over_window = tk.Toplevel()
        game_over_window.title("Game Over")
        game_over_window.attributes('-fullscreen', True)

        frame_fundo = tk.Frame(game_over_window, bg="#1e1e5e")
        frame_fundo.pack(fill="both", expand=True)

        titulo_label = tk.Label(frame_fundo, text="Game Over", bg="#1e1e5e", fg="#FFD700",
                            font=("Arial", 72, "bold"), justify="center")
        titulo_label.place(relx=0.5, rely=0.4, anchor="center")

        pontuacao_label = tk.Label(frame_fundo, text=f"Sua Pontuação: {self.pontuacao}", bg="#1e1e5e", fg="white",
                               font=("Arial", 36))
        pontuacao_label.place(relx=0.5, rely=0.5, anchor="center")

        sair_button = tk.Button(frame_fundo, text="SAIR", command=game_over_window.destroy, bg="#FF0000",
                            fg="white", font=("Arial", 24, "bold"), relief="raised", bd=3)
        sair_button.place(relx=0.5, rely=0.6, anchor="center")

    def finalizar_jogo(self):
        if self.perguntas_respondidas == self.perguntas_total:
            self.registrar_nome()
        else:
            self.game_over()  # Chama a função de fim de jogo
            self.registrar_nome()
            self.salvar_pontuacao()

    def registrar_nome(self):
        registrar_window = tk.Toplevel()
        registrar_window.title("Registrar Nome")
        registrar_window.attributes('-fullscreen', True)

        frame_fundo = tk.Frame(registrar_window, bg="#1e1e5e")
        frame_fundo.pack(fill="both", expand=True)

        titulo_label = tk.Label(frame_fundo, text="Registrar Nome", bg="#1e1e5e", fg="#FFD700",
                                font=("Arial", 36, "bold"))
        titulo_label.place(relx=0.5, rely=0.2, anchor="center")

        nome_label = tk.Label(frame_fundo, text="Digite seu nome:", bg="#1e1e5e", fg="white",
                              font=("Arial", 24))
        nome_label.place(relx=0.5, rely=0.4, anchor="center")

        self.nome_entry = tk.Entry(frame_fundo, font=("Arial", 24))
        self.nome_entry.place(relx=0.5, rely=0.5, anchor="center")

        confirmar_button = tk.Button(frame_fundo, text="Confirmar", command=self.salvar_pontuacao,
                                      bg="#3a3ab7", fg="white", font=("Arial", 18, "bold"))
        confirmar_button.place(relx=0.5, rely=0.6, anchor="center")

        sair_button = tk.Button(frame_fundo, text="SAIR", command=registrar_window.destroy, bg="#FF0000",
                                fg="white", font=("Arial", 16, "bold"), relief="raised", bd=3)
        sair_button.place(relx=0.9, rely=0.05, anchor="center")

    def salvar_pontuacao(self):
        self.nome_jogador = self.nome_entry.get()
        if self.nome_jogador:
            resultado = f"{self.nome_jogador}: {self.pontuacao} pontos"
            self.historico.append(resultado)                    
            messagebox.showinfo("Pontuação Registrada", resultado)
            self.resetar_jogo()
        else:
            messagebox.showwarning("Atenção", "Por favor, digite um nome.")


    def resetar_jogo(self):
        self.pontuacao = 0
        self.perguntas_respondidas = 0
        self.dificuldade_atual = ""
        self.nome_jogador = ""
        print("Resetando jogo...")  # Verificação
        self.temporizador_ativo = False  # Certifica que o temporizador esteja parado ao resetar o jogo

    def escolher_dificuldade(self):
        dificuldade_window = tk.Toplevel()
        dificuldade_window.title("Escolha a Dificuldade")
        dificuldade_window.attributes('-fullscreen', True)

        frame_fundo = tk.Frame(dificuldade_window, bg="#1e1e5e")
        frame_fundo.pack(fill="both", expand=True)

        titulo_label = tk.Label(frame_fundo, text="Escolha a dificuldade", bg="#1e1e5e", fg="#FFD700",
                                font=("Arial", 36, "bold"), justify="center")
        titulo_label.place(relx=0.5, rely=0.2, anchor="center")

        facil_button = tk.Button(frame_fundo, text="Fácil", command=lambda: self.selecionar_dificuldade("Fácil"),
                                 bg="#3a3ab7", fg="white", font=("Arial", 24, "bold"), relief="raised", bd=3)
        facil_button.place(relx=0.5, rely=0.4, anchor="center")

        medio_button = tk.Button(frame_fundo, text="Médio", command=lambda: self.selecionar_dificuldade("Médio"),
                                 bg="#3a3ab7", fg="white", font=("Arial", 24, "bold"), relief="raised", bd=3)
        medio_button.place(relx=0.5, rely=0.5, anchor="center")

        dificil_button = tk.Button(frame_fundo, text="Difícil", command=lambda: self.selecionar_dificuldade("Difícil"),
                                   bg="#3a3ab7", fg="white", font=("Arial", 24, "bold"), relief="raised", bd=3)
        dificil_button.place(relx=0.5, rely=0.6, anchor="center")

        sair_button = tk.Button(frame_fundo, text="SAIR", command=dificuldade_window.destroy, bg="#FF0000",
                                fg="white", font=("Arial", 16, "bold"), relief="raised", bd=3)
        sair_button.place(relx=0.9, rely=0.05, anchor="center")

    def mostrar_historico(self):
        historico_window = tk.Toplevel()
        historico_window.title("Histórico de Pontuações")
        historico_window.attributes('-fullscreen', True)

        frame_fundo = tk.Frame(historico_window, bg="#1e1e5e")
        frame_fundo.pack(fill="both", expand=True)

        titulo_label = tk.Label(frame_fundo, text="Histórico de Pontuações", bg="#1e1e5e", fg="#FFD700",
                                font=("Arial", 36, "bold"))
        titulo_label.place(relx=0.5, rely=0.05, anchor="center")

        for idx, resultado in enumerate(self.historico):
            resultado_label = tk.Label(frame_fundo, text=resultado, bg="#1e1e5e", fg="white",
                                        font=("Arial", 24))
            resultado_label.place(relx=0.5, rely=0.15 + (idx * 0.05), anchor="center")

        sair_button = tk.Button(frame_fundo, text="SAIR", command=historico_window.destroy, bg="#FF0000",
                                fg="white", font=("Arial", 16, "bold"), relief="raised", bd=3)
        sair_button.place(relx=0.9, rely=0.05, anchor="center")

def main():
    game = QuizGame()
    root = tk.Tk()
    root.title("Fut Question")
    root.attributes('-fullscreen', True)

    frame_fundo = tk.Frame(root, bg="#1e1e5e")
    frame_fundo.pack(fill="both", expand=True)

    titulo_label = tk.Label(frame_fundo, text="FUT\nQUESTION", bg="#1e1e5e", fg="#FFD700",
                            font=("Arial", 72, "bold"), justify="center")
    titulo_label.place(relx=0.5, rely=0.3, anchor="center")

    jogar_button = tk.Button(frame_fundo, text="JOGAR", command=game.iniciar_jogo, bg="#FF9800",
                             fg="white", font=("Arial", 24, "bold"), relief="raised", bd=3)
    jogar_button.place(relx=0.5, rely=0.6, anchor="center")

    historico_button = tk.Button(frame_fundo, text="HISTÓRICO", command=game.mostrar_historico, bg="#3a3ab7",
                                 fg="white", font=("Arial", 24, "bold"), relief="raised", bd=3)
    historico_button.place(relx=0.5, rely=0.7, anchor="center")

    sair_button = tk.Button(frame_fundo, text="SAIR", command=root.destroy, bg="#FF0000",
                            fg="white", font=("Arial", 16, "bold"), relief="raised", bd=3)
    sair_button.place(relx=0.9, rely=0.05, anchor="center")

    root.mainloop()

if __name__ == "__main__":
    main()
