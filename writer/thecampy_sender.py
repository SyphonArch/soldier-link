import thecampy

soldier = thecampy.Soldier('현재익', 2000_03_14, 2021_03_29)
user_id = 'jake.hyun@hotmail.com'
with open('thecampy_pw.secret', 'r') as f:
    user_pw = f.read().strip()


def send(message):
    try:
        title, content = message.get_header(), message.content

        msg = thecampy.Message(title, content)
        tc = thecampy.client()
        tc.login(user_id, user_pw)

        add_result = tc.add_soldier(soldier)
        get_result = tc.get_soldier(soldier)
        send_result = tc.send_message(soldier, msg)
        print(add_result, get_result, send_result)

    except Exception as p:
        pass
