from pytubefix import YouTube
from pytubefix.exceptions import VideoUnavailable, RegexMatchError
import json
import os

def baixarMusica(arquivo_json):
    arquivo = open(arquivo_json, "r")
    musicas = json.load(arquivo)

    total_musicas = len(musicas["musicas"])
    musicas_falhas = [] #lista com as músicas que falharem o download
    caminho_musicas = musicas["caminho"] #caminho para o diretório onde serão salvas as músicas

    print(f"Inciando dowload de {total_musicas} músicas")
    print("="*100)

    #--Baixar músicas -- 
    for i, item in enumerate(musicas["musicas"], 1):    
        #Resgatando os dados da música
        musica = item["Nome_musica"] 
        artista = item["Artista"]
        link = item["Link"]

        #Criando o diretório do artista se não existir
        if not os.path.exists(f"{caminho_musicas}{artista}"):
            os.makedirs(f"{caminho_musicas}{artista}")

        #Verifica se a música ja foi baixada
        if os.path.exists(f"{caminho_musicas}{artista}/{musica}.mp3"):
            print(f"A música \033[32m{musica}\033[0m já foi baixada")
            continue

        #Baixando a música
        try:
            print(f"\033[36m{i}/{total_musicas}\033[0m")
            print(f"Tentando baixar a música \033[32m{musica}\033[0m do \033[35m{artista}\033[0m ")
            print("Baixando...")

            yt = YouTube(link)
            audio_stream = yt.streams.filter(only_audio=True).first()
            caminho = audio_stream.download(output_path=f"{caminho_musicas}{artista}")

            #Renomeando a música
            print("Renomeando arquivo...")
            novo_arquivo = musica + ".mp3"
            os.rename(caminho, f"{caminho_musicas}{artista}/{novo_arquivo}")
            
            print(f"\033[32mA música \033[32m{musica} foi baixada com sucesso\033[0m")
        except VideoUnavailable:
            print(f"\033[31m  ✗ Vídeo indisponível: '{musica}'\033[0m")
            falha = {"Nome_musica": musica, "artista":artista, "error": "VideoUnvaliable"} #dados da música que falhou
            musicas_falhas.append(falha)
            continue
        except RegexMatchError:
            print(f"\033[31m  ✗ Link inválido ou formato não reconhecido: '{musica}'\033[0m")
            falha = {"Nome_musica": musica, "artista":artista, "error": "Link Invalid"}
            musicas_falhas.append(falha)
            continue
        except Exception as e:
            print(f"\033[31m  ✗ Erro ao baixar '{musica}': {type(e).__name__} - {str(e)}\033[0m")
            falha = {"Nome_musica": musica, "artista":artista, "error": "error"}
            musicas_falhas.append(falha)
            continue   

    #-- Retornar músicas que falharam --
    if musicas_falhas:
        with open('musicas_falhas.json', 'w') as f: #cria um json com as informações das músicas que falharam
            json.dump({"refazer": musicas_falhas}, f, indent=2, ensure_ascii=False) 

            print("\033[31m Arquivo criado com os downloads falhos \033[0m")
    else:
        print("\033[32m Sucesso ao baixar todas as músicas! \033[0m")

    arquivo.close()


baixarMusica("musicas.json")