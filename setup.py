from setuptools import setup, find_packages

setup(
    name='telegram_notificator',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    description='Модуль для оповещения пользователя в Telegram боте через chat_id и bot_token.',
    author='cherseroff',
    author_email='proffitm1nd@gmail.com',
    url='https://github.com/cherseroff27/module-telegram_notificator.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)