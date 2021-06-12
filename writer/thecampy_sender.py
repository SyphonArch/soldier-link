import thecampy

soldier = thecampy.Soldier('현재익', 2000_03_14, 2021_03_29, '육군훈련소')
user_id = 'jake.hyun@hotmail.com'
with open('thecampy_pw.secret', 'r') as f:
    user_pw = f.read().strip()


def send(message):
    try:
        title, content = message.get_header(), message.content
        content = '<p>' + content.replace('\n', '</p><p>') + '</p>'
        content = content.replace('<p></p>', '<p>&nbsp</p>')

        msg = thecampy.Message(title, content)
        tc = thecampy.client()
        tc.login(user_id, user_pw)

        tc.get_soldier(soldier)
        send_result = tc.send_message(soldier, msg)

        message.sent = True
        return True

    except Exception as p:
        return False

    finally:
        message.send_attempt_over = True
        message.save()
