# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from call_api import qna_api


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_answer_api"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        question = tracker.latest_message['text']
        temp = qna_api(question)
        print(temp)
        dispatcher.utter_template("utter_answer", tracker, answer=temp )

        return []
