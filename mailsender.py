from email.mime.text import MIMEText
import smtplib
import re

from typing import List
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class MailSender:
    """Mail sender object able to send mails without much configurations
    """

    _EMAIL_REGEX = "[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?"

    def __init__(self, host: str, port: int, login_address: str, login_password: str):
        """Initialize mail sender object able to send mails without much configurations

        Args:\n
            host (str): The host of the smtp server. Example : "smtp-mail.outlook.com".
            port (int): The port where to deploy the smtp server.
            login_address (str): The address that will be used to send the mails.
            login_password (str): The password that will be used to authenticate the mail sender.
        """
        self.host = host
        self.port = port
        self.login_address = login_address
        self.login_password = login_password

    def send(self, to_addresses: List[str], subject: str, message: str) -> None:
        """Send mail to one or more addresses

        Args:\n
            to_addresses (List[str]): The addresses to send an email to.
            subject (str): The subject of the email.
            message (str): The body content of the email.
        """
        compiled_regex = re.compile(MailSender._EMAIL_REGEX)
        if self.login_address is None or compiled_regex.match(self.login_address) is None:
            raise smtplib.SMTPAuthenticationError(f"Cannot use this illegal address {self.login_address}")
        if to_addresses is None or len(to_addresses) == 0:
            raise smtplib.SMTPDataError(f"Cannot send this mail to missing addresses")
        else:
            for to_address in to_addresses:
                if to_address is None or compiled_regex.match(to_address) is None:
                    raise smtplib.SMTPAuthenticationError(f"Cannot use this illegal address {to_address}")
        if subject is None or len(subject) == 0:
            raise smtplib.SMTPDataError(f"Cannot send this mail without subject")
        if message is None or len(message) == 0:
            raise smtplib.SMTPDataError(f"Cannot send this mail without body")
        smtp_server = smtplib.SMTP(host=self.host, port=self.port)
        smtp_server.starttls()
        smtp_server.login(self.login_address, self.login_password) #From keyvault
        for to_address in to_addresses:
            sent_message = MIMEMultipart()
            sent_message["From"] = self.login_address
            sent_message["To"] = to_address
            sent_message["Subject"] = subject
            sent_message.attach(MIMEText(message, "plain"))
            smtp_server.send(sent_message)
            del sent_message
        smtp_server.close()
