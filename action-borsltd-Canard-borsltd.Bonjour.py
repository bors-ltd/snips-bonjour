#!/usr/bin/env python3
import random

from hermes_python.hermes import Hermes
from hermes_python.ontology import MqttOptions


def subscribe_intent_callback(hermes, intent_message):
    action_wrapper(hermes, intent_message)


def action_wrapper(hermes, intent_message):
    print('debut')
    message = random.choice(
        [
            "",
            "Ah oui, je la connais celle-là.",
            "Attendez, ça va me revenir...",
            "On me l'a déjà racontée.",
        ]
    )
    message += " Il a une patte plus courte que l'autre, surtout la gauche."
    current_session_id = intent_message.session_id
    hermes.publish_end_session(current_session_id, message)
    print('fin')


if __name__ == "__main__":
    mqtt_opts = MqttOptions()
    with Hermes(mqtt_options=mqtt_opts) as h:
        h.subscribe_intent("borsltd:Canard", subscribe_intent_callback).start()
