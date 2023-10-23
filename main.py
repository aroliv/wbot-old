from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# Variável de estado
bot_state = {}

@app.route('/sms', methods=['POST'])
def webhook():
    # Recebe a mensagem do usuário
    user_message = request.values.get('Body', '').lower()
    
    # Inicializa uma resposta
    response = MessagingResponse()
    message = response.message()

    # Função para iniciar uma nova conversa
    def start_conversation():
        message.body("Oi, tudo bem? Seja bem-vindo ao canal de atendimento da Uaumarte. Como posso ajudar?")
        bot_state['conversa_iniciada'] = True

    # Verifica se a conversa foi iniciada
    if 'conversa_iniciada' not in bot_state:
        start_conversation()
    else:
        if "e você?" in user_message or "e vc?" in user_message or "e vc" in user_message:
            message.body("Dado que sou tão somente um bot, creio que não consiga responder corretamente esta pergunta.")
        elif "fone" in user_message or "fone de ouvido" in user_message:
            message.body("Entendo que você esteja com problemas com fones de ouvido. Pode nos contar mais sobre o problema?")
        elif "quebrou" in user_message or "direito" in user_message:
            message.body("Preciso localizar seu pedido. Pode me informar seu nome? Preciso que você mande no formato 'Nome: Fulano Oliveira'")
        elif "Nome" in user_message or "nome" in user_message:
            message.body("Obrigado por me informar seu nome. Pode me informar seu e-mail? Preciso que você mande no formato 'E-mail: fulanooliveira@gmail.com'")
        elif '@' in user_message:
            message.body("Obrigado por fornecer as informações. Parece que o problema ocorreu no seu último pedido. Você prefere que seja devolvido em uma agência próxima ou que os Correios retirem na sua casa?")
        elif "agência" in user_message or "casa" in user_message or "agencia" in user_message:
            message.body("Perfeito! Seu código de rastreio é: NB123456BR. Mais informações serão enviadas por e-mail! Nossa interação se encerra por aqui. Volte para o Qualtrics e continue com a pesquisa.")
            # Envie uma imagem como resposta
            message.media("https://github.com/aroliv/whatsapp-bot-old/blob/main/data/img/Velho.png?raw=true")
            bot_state.clear()
        else:
            message.body("Desculpe, não entendi. Como posso ajudar?")
    
    return str(response)

if __name__ == '__main__':
    app.run(debug=True)
