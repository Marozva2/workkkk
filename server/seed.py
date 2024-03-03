# seed.py

from models import db, User
from app import app


users = [{
    "id": 1,
    "firstname": "Boothe",
    "lastname": "Norcross",
    "email": "bnorcross0@vimeo.com",
    "password": "$2a$04$6LQzL.Lw8jX.Kk3jmoQy1enHg88ijL3gSQusLjMMT59NqAleXHP4e"
}, {
    "id": 2,
    "firstname": "Hoebart",
    "lastname": "Corringham",
    "email": "hcorringham1@ed.gov",
    "password": "$2a$04$0k7vWJGCkwFtomEj3mQNO.WAzt8eoGNIHBjsJxnO37H3ABMcPb/Yy"
}, {
    "id": 3,
    "firstname": "Lynea",
    "lastname": "Trivett",
    "email": "ltrivett2@vkontakte.ru",
    "password": "$2a$04$/v/rdtt6se9GSmRFQZCZI.1OkSM6LncevxBoB0m2MS/DkVf3FrW4G"
}, {
    "id": 4,
    "firstname": "Bridgette",
    "lastname": "Tendahl",
    "email": "btendahl3@google.nl",
    "password": "$2a$04$GiEkqreBGLsWRes6zEH7Ee1LmvjHyQzEyDjiYXFf3nlml50muQB/S"
}, {
    "id": 5,
    "firstname": "Reube",
    "lastname": "Heers",
    "email": "rheers4@apache.org",
    "password": "$2a$04$77PoIxgoE7gDBd08dSiiQOmm4/xW0grZ08uu9RklC.K/QuDUgd4gi"
}, {
    "id": 6,
    "firstname": "Willow",
    "lastname": "Drury",
    "email": "wdrury5@nationalgeographic.com",
    "password": "$2a$04$EGV.djdAU4XJ2.z2E.LMreHdwMJgXWYbQbgLBQFal5LEcdo5A3MIy"
}, {
    "id": 7,
    "firstname": "Marrilee",
    "lastname": "Yitzhok",
    "email": "myitzhok6@unicef.org",
    "password": "$2a$04$ZrQ8WHt9c3FXvAZ8yfUqb.HuUkuuOVLY7Hrzhyd5AqxWppTC2ZUXq"
}, {
    "id": 8,
    "firstname": "Vicky",
    "lastname": "Vasyukhin",
    "email": "vvasyukhin7@nbcnews.com",
    "password": "$2a$04$SYYup8Eq2XXl3.sWYNro/u8eQc8SiLJJJZwdmHyafrcjQryVSayIu"
}, {
    "id": 9,
    "firstname": "Olivie",
    "lastname": "Helks",
    "email": "ohelks8@nifty.com",
    "password": "$2a$04$sdYT6byWFmCwNKIGg077mucGqCeCwuScVJijF56egR5d1HUrWXdzu"
}, {
    "id": 10,
    "firstname": "Natty",
    "lastname": "Akerman",
    "email": "nakerman9@t.co",
    "password": "$2a$04$Q0V7xHCF3DveMog5wW5noOQQbWJ1hNKSJN3qb1LIJtU34MuvrPf4W"
}]


with app.app_context():
    db.session.add_all([User(**user) for user in users])
    db.session.commit()
