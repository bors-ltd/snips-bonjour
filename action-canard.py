#!/usr/bin/env python3
import random

from hermes_python.hermes import Hermes
from hermes_python.ontology import MqttOptions

import snips_common


class ActionCanard(snips_common.ActionWrapper):
    def action(self):
        preamble = random.choice(
            [
                "",
                "Ah oui, je la connais celle là.",
                "Attendez, ça va me revenir...",
                "On me l'a déjà racontée.",
            ]
        )
        answer = " Il a une patte plus courte que l'autre, surtout la gauche."
        self.end_session(preamble, answer)


if __name__ == "__main__":
    mqtt_opts = MqttOptions()

    with Hermes(mqtt_options=mqtt_opts) as h:
        h.subscribe_intent("borsltd:Canard", ActionCanard.callback).start()
