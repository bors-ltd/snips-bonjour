#!/usr/bin/env python3
import os

from hermes_python.hermes import Hermes
from hermes_python.ontology import MqttOptions

import snips_common


class ActionVu(snips_common.ActionWrapper):
    def action(self):
        self.end_session("Bonne nuit")
        os.system("sudo poweroff")


if __name__ == "__main__":
    mqtt_opts = MqttOptions()

    with Hermes(mqtt_options=mqtt_opts) as h:
        h.subscribe_intent("borsltd:BonneNuit", ActionVu.callback).start()
