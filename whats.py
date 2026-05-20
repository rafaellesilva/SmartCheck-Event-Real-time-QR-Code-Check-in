import pywhatkit as kit
import time

# Lista de contatos
contacts = [
    "+5512988764245",
    "+5512992615456",
    "+5512991716114"
]

image_path = "C:/Whats/QRCode_001.png" 

# Mensagem a ser enviada
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

for contact in contacts:
    try:
        kit.sendwhatmsg_instantly(contact, message, 15, True, 5)  # Envio instantâneo com espera de 5s
        
        print(f"✅ Mensagem enviada para {contact}")
        time.sleep(10)  # Pequena pausa para evitar bloqueios do WhatsApp
    except Exception as e:
        print(f"❌ Erro ao enviar para {contact}: {e}")
