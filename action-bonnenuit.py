#!/usr/bin/env python3
import os
import time

from hermes_python.hermes import Hermes
from hermes_python.ontology import MqttOptions

import snips_common


class ActionVu(snips_common.ActionWrapper):
    def action(self):
        self.end_session("Bonne nuit")
        # Wait a little for the message to be said
        time.sleep(5)
        # "sudo visudo" and add "_snips-skills ALL = NOPASSWD: /sbin/poweroff"
        os.system("sudo poweroff")


if __name__ == "__main__":
    mqtt_opts = MqttOptions()

    with Hermes(mqtt_options=mqtt_opts) as h:
        h.subscribe_intent("borsltd:BonneNuit", ActionVu.callback).start()
