import eb
import schedule
import config
import update_energy_database as em
import update_tinkerforge_database as tf
import time

def run():
    em.main()
    tf.main()
    eb.send_email(
        who=[config.emails['roman']],
        sender=config.emails['sender'],
        subject='Einfach Messen: Datenbank update durchgeführt',
        text='Hallo,\ndie Datenbank wurde automatisch geupdated.',
        password=config.password,
        smtp=config.smtp
        )

schedule.every().day.at('21:50').do(run())

while True:
	schedule.run_pending()
	time.sleep(1)