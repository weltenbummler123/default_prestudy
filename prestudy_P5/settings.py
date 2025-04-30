from os import environ
from os import popen

SESSION_CONFIGS = [
    dict(
        name='demographics',
        display_name="demographics only",
        app_sequence=['demographics'],
        num_demo_participants=6,
        use_browser_bots=False,
        oTree_version_used=popen('otree --version').read().strip()
    ),
dict(
        name='prestudy_framing_sms',
        display_name="Prestudy framing (SMS)",
        app_sequence=['prestudy_framing_sms'],
        num_demo_participants=6,
        use_browser_bots=False,
        oTree_version_used=popen('otree --version').read().strip()
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'de'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = True

#DEBUG = False

ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
    ),
    dict(name='live_demo',
         display_name='Room for live demo (no participant labels)'),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""


SECRET_KEY = '5046931017203'

INSTALLED_APPS = ['otree']