# multiplayer_snake_game
Operating Systems Project


Para exutar o programa deve ser necesário rodar primeiro o arquivo **testeserver.py** e depois os arquivos **client1.py** e **client2.py**. Além disso, para o programa funcionar devem ser instaladas as biliotecas *pygame* e *tkinter*.


![Captura de tela de 2019-10-23 16-36-15](https://user-images.githubusercontent.com/44793167/67441013-8af82900-f5d1-11e9-9b58-5321df7037d2.png)


  A atividade do trabalho prático consiste em implementar através de sockets e de networking I/O o jogo PySnakes, que seria um jogo da cobrinha mas com múltiplas snakes em um mesmo tabuleiro. Durante o desenvolvimento do trabalho, algumas abordagens foram adotadas para conseguir fazer a conexão entre cliente e servidor, sendo necessário implementar o jogo em três cenários distintos, tendo como primeiro cenário uma I/O programada, o segundo I/O orientada à interrupção e o terceiro I/O orientada à DMA.


### 1ª Abordagem

  Primeiramente, pensamos em deixar toda a lógica de jogo para os clientes, que processaria normalmente o jogo, mas com a adição de uma segunda cobra que seria controlada via informações do servidor. Os clientes mandariam para o servidor a tecla pressionada, e o servidor passaria a informação para o outro cliente.
Como com essa abordagem não seria possível responder às questões levantadas sobre os 3 cenários solicitados, essa abordagem foi deixada de lado.

 

### 2ª Abordagem
  Para implementar os cenários solicitados, mudamos a lógica do jogo inteiramente do cliente para o servidor. O jogo roda no servidor, recebendo as direções das cobras, dadas pelo usuário, pelos clientes. Ao atualizar o estado do jogo, o servidor manda a imagem de como está o tabuleiro para os clientes, que mostram o jogo aos usuários.
Para isso usamos funções do pygames, que, resumidamente, transformam o tabuleiro numa string que pode ser enviada e convertida novamente para um tabuleiro, pronto para ser “desenhado” na tela.
Porém essa não é uma abordagem eficiente, e provavelmente por isso o jogo é um tanto travado e às vezes não responde bem.
Cada cliente tem um ID, que é constantemente enviado para o servidor, o que impede que um socket bloqueie outro. Com o ID sozinho nada é feito, mas este pode vir acompanhado com a informação de qual tecla foi pressionada pelo usuário, e então a direção da cobra com o respectivo ID é alterado.
	Além dos problemas de desempenho, há um problema em que *a cobra, ao tocar na borda, não reaparece do lado oposto*, é como se o tabuleiro fosse maior que o mostrado.
	Apesar dos problemas essa é a base do trabalho daqui em diante.

 
### Colaboradores:
- Marcos Delgado - https://github.com/marcosdelgado0408 
- Weverson Paulo - https://github.com/Versinho
- Daniele Carvalho - https://github.com/daniele-mc
 
