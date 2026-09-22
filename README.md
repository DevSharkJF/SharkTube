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
Caso ocorra algum erro durante a execução do código, verifique os seguintes pontos:

* **Conexão com a internet:** certifique-se de que sua conexão está estável.
* **URL:** verifique se a URL informada está correta e acessível.
* **Yt-dlp:** certifique-se de que o yt-dlp está atualizado. Para atualizar, execute: ``pip install --upgrade yt-dlp``
* **Restrições do vídeo:** verifique se o vídeo não é privado, possui restrição de idade ou alguma outra limitação de acesso.

# Observações
Ao fornecer o link de um vídeo que pertence a uma playlist, todos os vídeos dessa playlist poderão ser baixados. Isso pode resultar em um número elevado de downloads e, consequentemente, aumentar consideravelmente o tempo necessário para concluir a operação.

Evite realizar um grande número de downloads em sequência. O YouTube pode identificar um volume elevado de requisições e solicitar autenticação (login) para permitir o download dos vídeos.

# Print do Terminal
<div align="center">
    <img width="511" height="468" alt="Image" src="https://github.com/user-attachments/assets/2e283a6c-dcca-4ede-8dad-dc0dc2927d19" />
</div>