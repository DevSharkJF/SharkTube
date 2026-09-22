# SharkTube
Código que faz download de vídeos do YouTube, podendo escolher a qualidade.

Utilização do código em terminal, interface com tkinter ainda será construída.

# Instalação
Instalar a biblioteca `yt-dlp`:

    pip install yt-dlp

Instale o Chocolatey Package Manager para Windows:

    https://chocolatey.org/install

Pelo terminal:

    choco install ffmpeg

Verifique a versão do ffmpeg com:

    ffmpeg -version

# Erros
Caso ocorra algum erro na hora de executar o código, tente sempre verificar os seguintes tópicos:
* Verificar conexão com a internet
* Verificar URL (Acessível e Correto)
* Verifique se o yt-dlp está atualizado. Atualize com: `pip install --upgrade yt-dlp`
* Verifique se o vídeo não está privado ou com restrição de idade

# Observações
Caso cole link de qualquer vídeo, que esteja em playlist, toda os vídeos contidos nessa playlist, serão baixados, o que pode ocasionar em um longo tempo de download.

Não é recomendado fazer um grande número de downloads, pois o you tube pode acabar requisitando login para que o vídeo consiga ser baixado.

# Print do Terminal
<div align="center">
    <img width="511" height="468" alt="Image" src="https://github.com/user-attachments/assets/2e283a6c-dcca-4ede-8dad-dc0dc2927d19" />
</div>