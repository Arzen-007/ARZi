from ARZi.utils.email.providers.mailgun import MailgunEmailProvider


def sendmail(addr, text, subject):
    print(
        "ARZi.utils.email.mailgun.sendmail will raise an exception in a future minor release of ARZi and then be removed in ARZi v4.0"
    )
    return MailgunEmailProvider.sendmail(addr, text, subject)
