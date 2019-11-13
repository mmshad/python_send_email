"""
Python code to send email.
"""

from datetime import datetime as dt    # date and time module for time purposes
import smtplib                         # SMTP lib to connect to email server
import base64                          # base64 data encodings
import email.mime.text                 # Multipurpose Internet Mail Extensions
import json                            # JSON module to import user settings
import socket                          # Socket module to get hostname
import itertools                       # Iteration tool module


def get_key(conf):
    """
    Get email key
    """

    tmp = conf['wd_key']
    for _ in itertools.repeat(None, conf['wd_key_iter']):
        tmp = base64.b64decode(tmp)
    key = tmp.decode()
    return key


def send_email(email_msg, conf, email_subj='Issue with your code'):
    """
    Function to send emails to users.
    """

    key = get_key(conf)
    body = ''.join(['Hi ', conf['name'], ',\n\n',
                    'There is an issue with your code.\n\n',
                    'What happened:\n\n', email_msg, '\n\n',
                    'When: ', dt.now().strftime('%Y-%m-%d %H:%M:%S'), '\n\n',
                    'Where: ', socket.gethostname(), '\n\n',
                    '- Watchdog'])

    msg = email.mime.text.MIMEText(body)
    msg['Subject'] = email_subj
    msg['From'] = conf['wd_email']
    msg['To'] = conf['email']

    if conf['ssl']:
        sm_con = smtplib.SMTP_SSL(conf['smtp'], conf['smtp_port'])
    else:
        sm_con = smtplib.SMTP(conf['smtp'], conf['smtp_port'])

    try:
        sm_con.ehlo()
        sm_con.login(conf['wd_email'], key)
        sm_con.sendmail(conf['wd_email'], conf['email'], msg.as_string())
        sm_con.close()
    except Exception as exp_err:
        print('   ... * EXCEPTION HAPPENED.')
        print('   ... * Sending email failed.')
        print('   ... * Check network connection and email credentials.')
        print('   ... * Error : %s: %s \n' % (exp_err.__class__, exp_err))

    print('   ... An email sent to: ' + conf['name'])


# --------------------- Main program

# Read JSON file
with open('input.json') as f:
    CONF = json.load(f)

# Send a test email
send_email('Test Error', CONF, 'Issue with your code.')
