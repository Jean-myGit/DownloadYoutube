#### pip install pytube

from pytube import YouTube

# Solicitando link do video e o local para salvar
link = input("Digite o link do Vídeo que deseja baixar: ")
path = input("Digite o Diretório em que deseja salvar o Vídeo: ")
yt = YouTube(link)

# Exibir informações do Vídeo
print("Título: ", yt.title)
print("Número de view: ", yt.views)
print("Tempo de vídeo: ", yt.length, "segundos")
print("Avaliação do vídeo: ", yt.rating)

# Baixar com a Maior Resoluçao
ys = yt.streams.get_highest_resolution()

# Iniciar o Download do Vídeo
print ("Baixando...")
ys.download(path)
print ("Download Concluído! ;)")