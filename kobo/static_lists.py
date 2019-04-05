# -*- coding: utf-8 -*-
# 😬

from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _

# This file is a place to store static, translatable strings
#import pydevd
#pydevd.settrace('192.168.0.104')

SECTORS = (
    # (value, human-readable label)
    ("Private sector", _("Private sector")),
)

# You might generate such a list of countries with code like this:
#
#     from __future__ import print_function
#     import requests
#     import sys
#
#     url = 'https://www.humanitarianresponse.info/api/v1.0/locations?filter[admin_level]=0'
#     while url:
#         print('Fetching', url, file=sys.stderr)
#         response = requests.get(url)
#         j = response.json()
#         if 'next' in j:
#             url = j['next']['href']
#         else:
#             url = None
#         for d in j['data']:
#             print("({}, _({}))".format(repr(d['iso3']), repr(d['label'])))
COUNTRIES = (
    # (value, human-readable label)
    ('ECU', _('Ecuador')),
)

# You might generate such a list of languages with code like this:
#
#     import requests
#     url = 'http://loc.gov/standards/iso639-2/ISO-639-2_utf-8.txt'
#     response = requests.get(url)
#     for line in response.iter_lines():
#         # Wow, the LOC does not specify an encoding in the response!
#         line = line.decode(response.apparent_encoding)
#         fields = line.strip().split('|')
#         if fields[2]:
#             print '({}, _({})),'.format(repr(fields[2]), repr(fields[3]))
LANGUAGES = (
    # (value, human-readable label)
    ('aa', _('Afar')),
    ('ab', _('Abkhazian')),
    ('af', _('Afrikaans')),
    ('ak', _('Akan')),
    ('sq', _('Albanian')),
    ('am', _('Amharic')),
    ('ar', _('Arabic')),
    ('an', _('Aragonese')),
    ('hy', _('Armenian')),
    ('as', _('Assamese')),
    ('av', _('Avaric')),
    ('ae', _('Avestan')),
    ('ay', _('Aymara')),
    ('az', _('Azerbaijani')),
    ('ba', _('Bashkir')),
    ('bm', _('Bambara')),
    ('eu', _('Basque')),
    ('be', _('Belarusian')),
    ('bn', _('Bengali')),
    ('bh', _('Bihari languages')),
    ('bi', _('Bislama')),
    ('bs', _('Bosnian')),
    ('br', _('Breton')),
    ('bg', _('Bulgarian')),
    ('my', _('Burmese')),
    ('ca', _('Catalan; Valencian')),
    ('ch', _('Chamorro')),
    ('ce', _('Chechen')),
    ('zh', _('Chinese')),
    ('cu', _('Church Slavic; Old Slavonic; Church Slavonic; Old Bulgarian; Old Church Slavonic')),
    ('cv', _('Chuvash')),
    ('kw', _('Cornish')),
    ('co', _('Corsican')),
    ('cr', _('Cree')),
    ('cs', _('Czech')),
    ('da', _('Danish')),
    ('dv', _('Divehi; Dhivehi; Maldivian')),
    ('nl', _('Dutch; Flemish')),
    ('dz', _('Dzongkha')),
    ('en', _('English')),
    ('eo', _('Esperanto')),
    ('et', _('Estonian')),
    ('ee', _('Ewe')),
    ('fo', _('Faroese')),
    ('fj', _('Fijian')),
    ('fi', _('Finnish')),
    ('fr', _('French')),
    ('fy', _('Western Frisian')),
    ('ff', _('Fulah')),
    ('ka', _('Georgian')),
    ('de', _('German')),
    ('gd', _('Gaelic; Scottish Gaelic')),
    ('ga', _('Irish')),
    ('gl', _('Galician')),
    ('gv', _('Manx')),
    ('el', _('Greek, Modern (1453-)')),
    ('gn', _('Guarani')),
    ('gu', _('Gujarati')),
    ('ht', _('Haitian; Haitian Creole')),
    ('ha', _('Hausa')),
    ('he', _('Hebrew')),
    ('hz', _('Herero')),
    ('hi', _('Hindi')),
    ('ho', _('Hiri Motu')),
    ('hr', _('Croatian')),
    ('hu', _('Hungarian')),
    ('ig', _('Igbo')),
    ('is', _('Icelandic')),
    ('io', _('Ido')),
    ('ii', _('Sichuan Yi; Nuosu')),
    ('iu', _('Inuktitut')),
    ('ie', _('Interlingue; Occidental')),
    ('ia', _('Interlingua (International Auxiliary Language Association)')),
    ('id', _('Indonesian')),
    ('ik', _('Inupiaq')),
    ('it', _('Italian')),
    ('jv', _('Javanese')),
    ('ja', _('Japanese')),
    ('kl', _('Kalaallisut; Greenlandic')),
    ('kn', _('Kannada')),
    ('ks', _('Kashmiri')),
    ('kr', _('Kanuri')),
    ('kk', _('Kazakh')),
    ('km', _('Central Khmer')),
    ('ki', _('Kikuyu; Gikuyu')),
    ('rw', _('Kinyarwanda')),
    ('ky', _('Kirghiz; Kyrgyz')),
    ('kv', _('Komi')),
    ('kg', _('Kongo')),
    ('ko', _('Korean')),
    ('kj', _('Kuanyama; Kwanyama')),
    ('ku', _('Kurdish')),
    ('lo', _('Lao')),
    ('la', _('Latin')),
    ('lv', _('Latvian')),
    ('li', _('Limburgan; Limburger; Limburgish')),
    ('ln', _('Lingala')),
    ('lt', _('Lithuanian')),
    ('lb', _('Luxembourgish; Letzeburgesch')),
    ('lu', _('Luba-Katanga')),
    ('lg', _('Ganda')),
    ('mk', _('Macedonian')),
    ('mh', _('Marshallese')),
    ('ml', _('Malayalam')),
    ('mi', _('Maori')),
    ('mr', _('Marathi')),
    ('ms', _('Malay')),
    ('mg', _('Malagasy')),
    ('mt', _('Maltese')),
    ('mn', _('Mongolian')),
    ('na', _('Nauru')),
    ('nv', _('Navajo; Navaho')),
    ('nr', _('Ndebele, South; South Ndebele')),
    ('nd', _('Ndebele, North; North Ndebele')),
    ('ng', _('Ndonga')),
    ('ne', _('Nepali')),
    ('nn', _('Norwegian Nynorsk; Nynorsk, Norwegian')),
    ('nb', _('Bokm\xe5l, Norwegian; Norwegian Bokm\xe5l')),
    ('no', _('Norwegian')),
    ('ny', _('Chichewa; Chewa; Nyanja')),
    ('oc', _('Occitan (post 1500); Proven\xe7al')),
    ('oj', _('Ojibwa')),
    ('or', _('Oriya')),
    ('om', _('Oromo')),
    ('os', _('Ossetian; Ossetic')),
    ('pa', _('Panjabi; Punjabi')),
    ('fa', _('Persian')),
    ('pi', _('Pali')),
    ('pl', _('Polish')),
    ('pt', _('Portuguese')),
    ('ps', _('Pushto; Pashto')),
    ('qu', _('Quechua')),
    ('rm', _('Romansh')),
    ('ro', _('Romanian; Moldavian; Moldovan')),
    ('rn', _('Rundi')),
    ('ru', _('Russian')),
    ('sg', _('Sango')),
    ('sa', _('Sanskrit')),
    ('si', _('Sinhala; Sinhalese')),
    ('sk', _('Slovak')),
    ('sl', _('Slovenian')),
    ('se', _('Northern Sami')),
    ('sm', _('Samoan')),
    ('sn', _('Shona')),
    ('sd', _('Sindhi')),
    ('so', _('Somali')),
    ('st', _('Sotho, Southern')),
    ('es', _('Spanish; Castilian')),
    ('sc', _('Sardinian')),
    ('sr', _('Serbian')),
    ('ss', _('Swati')),
    ('su', _('Sundanese')),
    ('sw', _('Swahili')),
    ('sv', _('Swedish')),
    ('ty', _('Tahitian')),
    ('ta', _('Tamil')),
    ('tt', _('Tatar')),
    ('te', _('Telugu')),
    ('tg', _('Tajik')),
    ('tl', _('Tagalog')),
    ('th', _('Thai')),
    ('bo', _('Tibetan')),
    ('ti', _('Tigrinya')),
    ('to', _('Tonga (Tonga Islands)')),
    ('tn', _('Tswana')),
    ('ts', _('Tsonga')),
    ('tk', _('Turkmen')),
    ('tr', _('Turkish')),
    ('tw', _('Twi')),
    ('ug', _('Uighur; Uyghur')),
    ('uk', _('Ukrainian')),
    ('ur', _('Urdu')),
    ('uz', _('Uzbek')),
    ('ve', _('Venda')),
    ('vi', _('Vietnamese')),
    ('vo', _('Volap\xfck')),
    ('cy', _('Welsh')),
    ('wa', _('Walloon')),
    ('wo', _('Wolof')),
    ('xh', _('Xhosa')),
    ('yi', _('Yiddish')),
    ('yo', _('Yoruba')),
    ('za', _('Zhuang; Chuang')),
    ('zu', _('Zulu')),
)

# Whenever we add a translation that Django itself does not support, add
# information about the language here. This dictionary will be used to update
# `django.conf.locale.LANG_INFO`
EXTRA_LANG_INFO = {
    'ku': {
        'bidi': True,
        'code': 'ku',
        'name': 'Kurdish',
        'name_local': 'كوردی',
    },
}
