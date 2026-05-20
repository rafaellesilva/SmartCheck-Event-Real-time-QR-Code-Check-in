import pywhatkit as kit
import time

# Dicionário com números de telefone como chave e caminhos das imagens como valor
contatos = {
    
    "+55(12) 98169-9688": "QRCode_075.png"
    # Adicione mais números e imagens aqui
}

message = "\U0001F48D Olá! Seu convite especial chegou! \U0001F389\n\n" \
          "Estamos muito felizes em te receber para esse momento único! ❤️✨\n\n" \
          "📍 Local: Rua Benedito de Oliveira, número 500 - Freitas (Salão de Festas Ranario)\n\n" \
          "Aqui está o seu QR Code de entrada 🎟️📲\n\n" \
          "📌 Como usar?\n" \
          "1️⃣ Apresente este QR Code na entrada do evento\n" \
          "2️⃣ Nossa equipe fará a leitura e pronto, é só aproveitar!\n\n" \
          "Mal podemos esperar para celebrar esse dia incrível com você! 🎊💖\n\n" \
          "✨ Deus é bom o tempo todo, e o tempo todo Deus é bom! ✨\n\n" \
          "Nos vemos lá! 💕\n\n" \
          "Com carinho,\nEvelyn & Marcos"

# Loop para enviar uma imagem para cada número
for numero, imagem in contatos.items():
    kit.sendwhats_image(
        numero,  # Número de telefone
        imagem,  # Caminho para o arquivo de imagem
        message,  # Legenda opcional
        25, 
        True, 
        5  
    )
    time.sleep(2)  # Aguarda 2 segundos entre os envios para evitar erros
