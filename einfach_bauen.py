import eb
import config
import update_energy_database as em
import update_tinkerforge_database as tf


em.main(lehrstuhl=True)
tf.main(lehrstuhl=True)

send = False 

if send:
    eb.send_email(
        who=[config.emails['roman']],
        sender=config.emails['sender'],
        subject='Einfach Messen: Datenbank update durchgeführt',
        text='Hallo,\ndie Datenbank wurde automatisch geupdated.',
        password=config.password,
        smtp=config.smtp
        )