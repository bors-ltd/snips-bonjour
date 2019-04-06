#!/usr/bin/env python3
import random

from hermes_python.hermes import Hermes
from hermes_python.ontology import MqttOptions

import snips_common


class ActionVu(snips_common.ActionWrapper):
    def action(self):
        message = random.choice(
            [
                "Vive l'apéro !",
                "Sans alcool pour moi, j'ai encore du chemin à faire.",
                "Vous avez pensé à mettre de la bière au frais ?",
                "Vous avez pensé à sortir la bière en avance ?",
                "Il reste encore des pistaches ?",
                "Je finis un calcul et j'arrive.",
                "Déjà ? Je n'ai pas vu le temps passer.",
                "N'oubliez pas les croquettes de Théo.",
            ]
        )
        self.end_session(message)


if __name__ == "__main__":
    mqtt_opts = MqttOptions()

    with Hermes(mqtt_options=mqtt_opts) as h:
        h.subscribe_intent("borsltd:Apero", ActionVu.callback).start()
