# Mundo DevOps - Code Challenge #
## IPData - Busca, localização e histórico de pesquisa de IP's


### Como visualizar o projeto?

• Para que você consiga executar o código em sua máquina, é necessário que você tenha a linguagem [Python](https://www.python.org/downloads/) instalada em seu computador, de preferência versões 3.x.
- Após isso, clone o projeto através do endereço HTTPS, SSH ou apenas baixe e descompacte o ZIP do projeto.
- Feito isso, abra o projeto em sua IDE favorita ( recomendo [Visual Studio Code](https://code.visualstudio.com/) )
 ![](https://i.ibb.co/zrrVy8P/estrutura.png)
• Com o projeto aberto em sua IDE nessa estrutura, abra um console de sua preferência e digite o seguinte comando: 

		`python -m venv venv`

	• Dessa forma, você criou um ambiente virtual e assim pode instalar as dependências necessárias para a execução do projeto sem que tenham conflito com outras já instaladas de sua máquina.
• Para acessar o ambiente virtual criado, digite no console: 
	 - Caso você esteja usando PowerShell: *venv/Scripts/activate.ps1* 
	 - Caso você esteja usando CMD: *venv/Scripts/activate.bat* 
	 - Caso você esteja usando shell Linux: *venv/Scripts/activate* 

   • Seu ambiente virtual estará sendo utilizado se você estiver com um ***venv*** no seu terminal.
   • Finalmente, agora podemos instalar as dependências usando o requirements.txt do projeto:
   
    - `pip install -r requirements.txt`
  
   • Seguindo todas as instruções, seu terminal deverá se parecer com o meu:
     ![.](https://i.ibb.co/nmQqfcQ/Captura-de-tela-2022-02-17-000105.png)
• Após tudo ter sido instalado, escreva os seguintes comandos no terminal:

		python manage.py migrate 
		python manage.py runserver
		
	- Porque executar esses comandos?
	   - Criamos as bases de dados onde vamos armazenar as informações dos IP's que os usuários irão pesquisar usando um comando próprio do Django chamado migrate, simplificadamente falando, e então finalmente executamos `runserver` para que o servidor local do projeto esteja sendo executado no seu localhost de porta 8000. 
	   - `localhost:8000`
	   
• Observação: 
   - Estamos usando o banco de dados padrão do Django (sqlite3), então você não deve se preocupar em instalar nada relacionado a persistência de dados.




###  - Telas do IPData - 

Tela principal
![Tela principal](https://i.ibb.co/SyQF0dk/index.png)

Tela de histórico
![Tela do histórico](https://i.ibb.co/0Y08v6x/log.png)
