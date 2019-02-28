#!/usr/bin/env python3
from hermes_python.hermes import Hermes
from hermes_python.ontology import MqttOptions


def subscribe_intent_callback(hermes, intent_message):
    action_wrapper(hermes, intent_message)


def action_wrapper(hermes, intent_message):
    """ Write the body of the function that will be executed once the intent is recognized.
    In your scope, you have the following objects :
    - intent_message : an object that represents the recognized intent
    - hermes : an object with methods to communicate with the MQTT bus following the hermes protocol.
    - conf : a dictionary that holds the skills parameters you defined.
      To access global parameters use conf['global']['parameterName']. For end-user parameters use conf['secret']['parameterName']

    Refer to the documentation for further details.
    """
    print('debut')
    current_session_id = intent_message.session_id
    hermes.publish_end_session(current_session_id, "Bonjour à vous")
    print('fin')


if __name__ == "__main__":
    mqtt_opts = MqttOptions()
    with Hermes(mqtt_options=mqtt_opts) as h:
        h.subscribe_intent("borsltd:Salutation", subscribe_intent_callback).start()
