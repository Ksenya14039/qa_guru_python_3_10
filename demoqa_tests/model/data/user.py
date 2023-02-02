import datetime
from dataclasses import dataclass
from datetime import date

@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    phone: str
    address: str
    birthday: datetime.date
    gender: str
    subject: str
    hobbies: str
    image: str
    state: str
    city: str


test_user = User(
    first_name='Ksenia',
    last_name='Kapranova',
    email='ksenya14039@mail.ru',
    gender='Female',
    phone='9973655228',
    birthday=date(1997, 10, 9),
    subject='English',
    hobbies='Reading',
    image='wepk.jpeg',
    address='Moscow',
    state='NCR',
    city='Delhi')