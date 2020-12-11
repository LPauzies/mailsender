# MailSender
A simple package to interact with mail sending

## Features:
- HTML and/or TXT content.
- TLS support.
- Multiple direct mail


## Installation
`pip install -i https://test.pypi.org/simple/ emailsender`

## Usage example

```Python
import os
from emailsender import MailSender

host = "smtp-mail.outlook.com"
port = 587
my_address = "example@example.com"
my_password = os.environ["PASSWORD"]

mail_sender = MailSender(host, port, my_address, my_password)

to_addresses = [
    "addr1",
    "addr2",
    "addr3"
]

mail_sender.send(to_addresses, "Subject", "Body")
```

## License

GNU GENERAL PUBLIC LICENSE  
Version 3, 29 June 2007

Copyright (C) 2020 Lucas Pauzies   
Everyone is permitted to copy and distribute verbatim copies
of this license document, but changing it is not allowed.