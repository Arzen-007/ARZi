from ARZi.utils.email.providers.smtp import SMTPEmailProvider


def sendmail(addr, text, subject):
    print(
        "ARZi.utils.email.smtp.sendmail will raise an exception in a future minor release of ARZi and then be removed in ARZi v4.0"
    )
    return SMTPEmailProvider.sendmail(addr, text, subject)
