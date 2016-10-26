from __future__ import print_function
import json
import urllib2
import time

POST_URL = "http://35.160.215.28/harambe/"

GREETING = "Welcome to Echo Lock!"

# --------------- Functions that control the skill's behavior ----------------


def get_welcome_response():
    return build_response(build_speechlet_response("Welcome", GREETING, False))


def handle_session_end_request():
    return build_response(build_speechlet_response("Session Ended", "Goodbye", True))



# --------------- Intent Events ------------------


def on_intent(intent_request, session):
    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']
    
    if intent_name == "GoIntent":
        card_title = intent['name']
        data = json.dumps({
            'api_key': 'C9YQZ91S000DUMR3VS69GCAFV0GRBL',
        })
        req = urllib2.Request(POST_URL+"authorize", data, {'Content-Type': 'application/json'})
        f = urllib2.urlopen(req)
        d = json.load(f)
        f.close()
        return build_response(build_speechlet_response(card_title, "Logging you in!", True))
    elif intent_name == "StartIntent":
        found = False
        message = "hi"

        while not found:
            data = json.dumps({
                'api_key': 'C9YQZ91S000DUMR3VS69GCAFV0GRBL',
                'site_name': 'www.ratatype'
            })
            req = urllib2.Request(POST_URL+"poll_logged_in", data, {'Content-Type': 'application/json'})
            f = urllib2.urlopen(req)
            d = json.load(f)
            f.close()
            if d['status'] == "0":
                message = d['message']
                found = True
            else:
                time.sleep(3) 
        return build_response(build_speechlet_response(intent['name'], message, False))
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


# --------------- Other Events ------------------


def on_session_started(session_started_request, session):
    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    return get_welcome_response()


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.
    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


def build_speechlet_response(title, output, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
        },
        'shouldEndSession': should_end_session
    }


def build_response(speechlet_response):
    return {
        'version': '1.0',
        'response': speechlet_response
    }


# --------------- Main handler ------------------


def lambda_handler(event, context):
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])
    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])
    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])