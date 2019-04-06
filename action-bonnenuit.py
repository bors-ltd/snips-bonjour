#!/usr/bin/env python3
import os
import threading

from hermes_python.hermes import Hermes
from hermes_python.ontology import MqttOptions

import snips_common


def poweroff():
    # "sudo visudo" and add "_snips-skills ALL = NOPASSWD: /sbin/poweroff"
    os.system("sudo poweroff")


class ActionVu(snips_common.ActionWrapper):
    def action(self):
        self.end_session("Bonne nuit")
        # Wait enough for the message to be said
        timer = threading.Timer(10, poweroff)
        timer.start()


if __name__ == "__main__":
    mqtt_opts = MqttOptions()

    with Hermes(mqtt_options=mqtt_opts) as h:
        h.subscribe_intent("borsltd:BonneNuit", ActionVu.callback).start()
