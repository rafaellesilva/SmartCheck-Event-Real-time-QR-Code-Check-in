import pywhatkit as kit
import time

message = "\U0001F48D Olá! Seu convite especial chegou! \U0001F389\n\n" \
          "Estamos muito felizes em te receber para esse momento único! ❤️✨\n\n" \
          "📍 Local: Rua Benedito de Oliveira, número 500 - Freitas (Salão de Festas Ranario)\n\n" \
          "Aqui está o seu QR Code de entrada 🎟️📲\n\n" \
          "📌 Como usar?\n" \
          "1️⃣ Apresente este QR Code na entrada do evento\n" \
          "2️⃣ Nossa equipe fará a leitura e pronto, é só aproveitar! \U0001F37C\n\n" \
          "Mal podemos esperar para celebrar esse dia incrível com você! 🎊💖\n\n" \
          "✨ Deus é bom o tempo todo, e o tempo todo Deus é bom! ✨\n\n" \
          "Nos vemos lá! 💕\n\n" \
          "Com carinho,\nEvelyn & Marcos"


kit.sendwhats_image("+5512981126830","QRCode_001.png",message,15, True, 5)