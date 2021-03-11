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

        tc.add_soldier(soldier)
        tc.get_soldier(soldier)
        tc.send_message(soldier, msg)

    except Exception as p:
        pass
