from bottle import post, run, request

import mail_sender


@post("/send_mail")
def send_mail():
    try:
        mail_sender.send_mail(receiver_email=request.forms.get("receiver_email"),
                              message_subject=request.forms.get("message_subject"),
                              message_text=request.forms.get("message_text"),
                              message_html=request.forms.get("message_html"))
        return "OK"
    except:
        return "Sending are fallen"


if __name__ == "__main__":
    run(host="0.0.0.0", port=80)
