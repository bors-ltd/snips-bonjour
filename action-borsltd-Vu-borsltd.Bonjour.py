#!/usr/bin/env python3
import random

from hermes_python.hermes import Hermes
from hermes_python.ontology import MqttOptions

import snips_common


class ActionVu(snips_common.ActionWrapper):
    def action(self):
        message = random.choice(
            [
                "Mon cul ? haha ! Très drôle...",
                "Mon cul ? Je suis morte de rire...",
                "Mon cul ? ça vous amuse ?",
            ]
        )
        self.end_session(message)


if __name__ == "__main__":
    mqtt_opts = MqttOptions()

    with Hermes(mqtt_options=mqtt_opts) as h:
        h.subscribe_intent("borsltd:Vu", ActionVu.callback).start()
