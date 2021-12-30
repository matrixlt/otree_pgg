from os import environ
SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=0.03, participation_fee=25)
SESSION_CONFIGS = [
    dict(name='production_diff', num_demo_participants=None, app_sequence=[
        'trust', 'trust2', 'survey'],
        treatment_group="production",
        init_more=24,
        init_less=24,
        unit_more=2,
        unit_less=1,
        threshold=36,
        profit=20),
    dict(name='endowmeat_diff', num_demo_participants=None, app_sequence=[
        'trust', 'trust2', 'survey'],
        treatment_group="endowment",
        init_more=32,
        init_less=16,
        unit_more=1,
        unit_less=1,
        threshold=24,
        profit=20),
    dict(name='control', num_demo_participants=None, app_sequence=[
        'trust', 'trust2', 'survey_control'],
        treatment_group="control",
        init_more=24,
        init_less=24,
        unit_more=1,
        unit_less=1,
        threshold=24,
        profit=20),
    dict(name='new_production_diff', num_demo_participants=None, app_sequence=[
        'trust', 'trust2', 'survey'],
        treatment_group="production",
        init_more=24,
        init_less=24,
        unit_more=3,
        unit_less=1,
        threshold=48,
        profit=20),
    dict(name='new_endowmeat_diff', num_demo_participants=None, app_sequence=[
        'trust', 'trust2', 'survey'],
        treatment_group="endowment",
        init_more=36,
        init_less=12,
        unit_more=1,
        unit_less=1,
        threshold=24,
        profit=20)]
LANGUAGE_CODE = 'zh-hans'
REAL_WORLD_CURRENCY_CODE = 'CNY'
USE_POINTS = True
POINTS_CUSTOM_NAME = "分"
DEMO_PAGE_INTRO_HTML = ''
PARTICIPANT_FIELDS = ['sum_points1', 'sum_points2', 'role']
SESSION_FIELDS = []
ROOMS = [dict(name='lab', display_name='lab',
              participant_label_file='_rooms/lab.txt')]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

SECRET_KEY = 'blahblah'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
