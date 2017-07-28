def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/YOUR_DOMAIN_NAME/messages",
        auth=("api", "key-7e8383ec319a4ab564df204fc04722c1"),
        data={"from": "Excited User <mailgun@YOUR_DOMAIN_NAME>",
              "to": ["cooproton@gmail.com", "cooproton@gmail.com"],
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness! Hey whats happening!"})
