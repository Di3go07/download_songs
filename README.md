# download_songs
Código python para automatizar o download de música no Youtube

# 🖥️​ Ambiente virtual
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
