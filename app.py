import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine


API_TOKEN = 'YOUR_API_TOKEN'
WEBHOOK_URL = 'YOUR_WEBHOOK_URL '


app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
    states=[
        'user',
        'chat',
        'Station',
        's1',
        's2',
        's3',
        's4',
        's5',
        's6',
        's7',
        's8',
        's9',
        's10',
        's11',
        's12',
        'afterstation',
        'HSRailway',
        'HSRDate',
        'HSRStart',
        'HSREnd',
        'HSRTime',
        'HSRCheck',
        'HSRResult'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'user',
            'conditions': 'is_going_to_start'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'Station',
            'conditions': 'is_going_to_Station'
        },
        {
            'trigger': 'advance',
            'source': 'Station',
            'dest': 's1',
            'conditions': 'is_going_to_s1'
        },
        {
            'trigger': 'advance',
            'source': 'Station',
            'dest': 's2',
            'conditions': 'is_going_to_s2'
        },
        {
            'trigger': 'advance',
            'source': 'Station',
            'dest': 's3',
            'conditions': 'is_going_to_s3'
        },
        {
            'trigger': 'advance',
            'source': 'Station',
            'dest': 's4',
            'conditions': 'is_going_to_s4'
        },
        {
            'trigger': 'advance',
            'source': 'Station',
            'dest': 's5',
            'conditions': 'is_going_to_s5'
        },
        {
            'trigger': 'advance',
            'source': 'Station',
            'dest': 's6',
            'conditions': 'is_going_to_s6'
        },
        {
            'trigger': 'advance',
            'source': 'Station',
            'dest': 's7',
            'conditions': 'is_going_to_s7'
        },
        {
            'trigger': 'advance',
            'source': 'Station',
            'dest': 's8',
            'conditions': 'is_going_to_s8'
        },
        {
            'trigger': 'advance',
            'source': 'Station',
            'dest': 's9',
            'conditions': 'is_going_to_s9'
        },
        {
            'trigger': 'advance',
            'source': 'Station',
            'dest': 's10',
            'conditions': 'is_going_to_s10'
        },
        {
            'trigger': 'advance',
            'source': 'Station',
            'dest': 's11',
            'conditions': 'is_going_to_s11'
        },
        {
            'trigger': 'advance',
            'source': 'Station',
            'dest': 's12',
            'conditions': 'is_going_to_s12'
        },
        {
            'trigger': 'afterstation',
            'source': [
                's1',
                's2',
                's3',
                's4',
                's5',
                's6',
                's7',
                's8',
                's9',
                's10',
                's11',
                's12'
            ],    
            'dest': 'afterstation',
            
        },
        {
            'trigger': 'advance',
            'source': 'afterstation',
            'dest': 'Station',
            'conditions': 'is_going_to_Station2'
        },
        {
            'trigger': 'advance',
            'source': 'afterstation',
            'dest': 'user',
            'conditions': 'is_going_to_User2'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'HSRailway',
            'conditions': 'is_going_to_HSRailway'
        },
       
        {
            'trigger': 'advance',
            'source': 'HSRailway',
            'dest': 'HSRDate',
            'conditions': 'is_going_to_HSRDate'
        },
        {
            'trigger': 'advance',
            'source': 'HSRDate',
            'dest': 'HSRStart',
            'conditions': 'is_going_to_HSRStart'
        },
        {
            'trigger': 'advance',
            'source': 'HSRStart',
            'dest': 'HSREnd',
            'conditions': 'is_going_to_HSREnd'
        },
        {
            'trigger': 'advance',
            'source': 'HSREnd',
            'dest': 'HSRTime',
            'conditions': 'is_going_to_HSRTime'
        },
        {
            'trigger': 'go_to_HSRCheck',
            'source': 'HSRTime',
            'dest': 'HSRCheck'
            
        },
        {
            'trigger': 'advance',
            'source': 'HSRCheck',
            'dest': 'HSRResult',
            'conditions': 'is_going_to_HSRResult'
        },
        {
            'trigger': 'advance',
            'source': 'HSRResult',
            'dest': 'HSRailway',
            'conditions': 'is_going_to_HSRSearch'
        },
        {
            'trigger': 'advance',
            'source': 'HSRResult',
            'dest': 'user',
            'conditions': 'is_going_to_UserState'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'chat',
            'conditions': 'is_going_to_chat'
        },
        {
            'trigger': 'go_back',
             'source': [
                'chat',
                'Station',
                'HSRailway',
                'HSRDate',
                'HSRStart',
                'HSREnd',
                'HSRTime',
                'HSRCheck',
                'HSRResult'
            ],
            'dest': 'user'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))



@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    machine.advance(update)
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')


if __name__ == "__main__":
    _set_webhook()
    app.run()
