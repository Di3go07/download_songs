# download_songs
Código python para automatizar o download de música .mp3 no Youtube. 

## 🖥️​ Ambiente virtual
Como criar o ambiente virtual Python desse programa
1. Abra no terminal a pasta do projeto, "donwload_songs"
   
3. Se ainda não tiver instalado, instale a ferramenta `virtualenv`:
   - No Windows:
   ```
   pip install virtualenv
   ```
   - No Linux:
   ```
   sudo apt install virtualenv
   ```
   
4. Crie um ambiente virtual na pasta do projeto:
   ```
   virtualenv nome_do_ambiente
   ```
   ou
   ```
   python3 -m venv nome_do_ambiente
   ```

5. Ative o ambiente virtual:
   - No Windows:
     ```
     .\nome_do_ambiente\Scripts\activate
     ```
   - No Linux/Mac:
     ```
     source nome_do_ambiente/bin/activate
     ```

6. Agora você está no ambiente virtual. Você pode instalar as dependências específicas do programa usando o `pip` e acessando o arquivo 'requirements'. Por exemplo:
   ```
   python3 -m pip install -r ./requirements.txt
   ```

Lembre-se de que, ao terminar o desenvolvimento, você pode desativar o ambiente virtual digitando `deactivate` no terminal.

O ambiente virtual ajuda a isolar as dependências do seu projeto, facilitando o gerenciamento e evitando conflitos entre diferentes projetos Python

## 🎵 Músicas 
Acesse o arquivo /musicas.json para configurar o ambiente de download e escolher as músicas que deverão ser baixadas.

Na variável "caminho", o usuário deve declarar o caminho para um diretório raiz onde as músicas serão baixadas. Dentro desse diretório, o próprio código organizará as músicas em pastas por artistas e renomea-las para o nome passado no arquivo.

Na variável "musicas", o usuário deve seguir o modelo de lista de dicionários fornecidos para passar à aplicação as informações necessárias para o donwload. É permitido colocar o número que o usuário desejar de músicas, mas a última na lista não pode conter vŕigula (,) após fechar as chaves ({}) do dicionário dela.

**Exemplo completo do JSON:**

```
{
    "caminho": "/home/user/Documentos/Musicas",  
    "musicas": [
        {"Nome_musica": "Run to the Hills", "Artista":  "Iron Maiden", "Link": "https://www.youtube.com/watch?v=Q3sJlr0kw8I"},
        {"Nome_musica": "Aces High", "Artista":  "Iron Maiden", "Link": "https://www.youtube.com/watch?v=bmXgLuTtazY"},
        {"Nome_musica": "Callifornicaion", "Artista":  "Red Hot Chillie Pepers", "Link": "https://www.youtube.com/watch?v=6L0LIo35sF4"}
    ]
}
```

## ⚙ Execução
Como rodar o código 

1. Abra a pasta "download_songs" do projeto no terminal, caso não esteja aberta
2. Execute o ambiente virtual caso ele não esteja ativo, utilizando o nome do ambiente que você criou anteriormente
   - No Windows:
     ```
     .\nome_do_ambiente\Scripts\activate
     ```
   - No Linux/Mac:
     ```
     source nome_do_ambiente/bin/activate
     ```
3.  Execute o código :
   ```
   python3 main.py
   ```

Logo após executar o código, a aplicação irá resgatar o link de cada música no JSON para realizar o download, bem como renoema-las corretaemnte e agrupa-las pelo artista. 

Todo o progresso pode ser acompanho pelo terminal e, caso o donwload de alguma música retorne um erro, um novo arquivo será gerado com o nome delas para caso o usuário deseja tentar baixa-las novamente. 

# 👨‍💻 Desenvolvedor

Diego Penna Andrade Barros <br>
PDITA 274
