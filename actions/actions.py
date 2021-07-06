

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class Action_cc_number(Action):

    def name(self) -> Text:
        return "action_cc_number"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        access_level = tracker.get_slot("access_level")
        CC_number = tracker.get_slot("CC_number")

        if access_level == 'access level 1':
            dispatcher.utter_message(text=f"Here is your credit card number {CC_number}")

        else:
            dispatcher.utter_message(text="Access Denied")
        return []

class Action_acc_balance(Action):
    
    def name(self) -> Text:
        return "action_acc_balance"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        access_level = tracker.get_slot("access_level")
        acc_balance = tracker.get_slot("acc_balance")

        if access_level == 'access level 2':
            dispatcher.utter_message(text=f"Here is your account balance {acc_balance}")

        else:
            dispatcher.utter_message(text="Access Denied")
        return []