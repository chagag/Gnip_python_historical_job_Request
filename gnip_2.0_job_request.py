<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
# date: Wed Sep 19 10:37:34 2015
# last update: Thurs 3.10.17
# author: danyang / modified by amit goldenberg
# parts of the code are modified from: CreateHistoricalJob.py, MonitorJobStatus.py and AcceptRejectHistoricalJob.py
#                                      https://github.com/gnip/support/tree/master/Historical%20PowerTrack/Python
# description: (1) post job, (2) get quotes (duration and size of files), (3) accept/reject job (4) output job url for monitoring and downloading
# inputs: UN, PWD, account (individual's information)
#         request: fromDate, toDate, jobTitle, rules (search keywords etc)
# output: jobTitle.txt with job url for monitoring progress and downloading upon completion
"""

import urllib.request
import base64
import json
import sys
import time

def request_url(url, jobString, base64string):
    base64string = base64.encodebytes(('%s:%s' % (UN, PWD)).encode()).decode().replace('\n', '')
    req = urllib.request.Request(url=url, data=jobString)
    req.add_header('Content-type', 'application/json')
    req.add_header("Authorization", "Basic %s" % base64string)
# automatizing the usl analysis.
    try:
        response = urllib.request.urlopen(req)
        the_page = response.read()
        return the_page
    except urllib.error.HTTPError as e:
        print (e.read())


if __name__ == "__main__":

    UN = 'exmple@email.com' # change to my email and my password
    PWD = 'password'
    account = 'account name'
    base64string = base64.encodebytes(('%s:%s' % (UN, PWD)).encode()).decode().replace('\n', '')

    # create job
    url = 'https://gnip-api.gnip.com/historical/powertrack/accounts/' + account + '/publishers/twitter/jobs.json'
    publisher = "twitter"
    streamType = "track_v2"
    dataFormat = "activity_streams" #raceriotsUSA
    fromDate = "201408112359" # This time is inclusive -- meaning the minute specified will be included in the data returned
    toDate =   "201408122359" # This time is exclusive -- meaning the data returned will not contain the minute specified, but will contain the minute immediately preceding it
    jobTitle = "test-job-python_amit5"
    rules = [{"value":"Amit Goldenberg"}]
    job = {"publisher":publisher,"streamType":streamType,"dataFormat":dataFormat,"fromDate":fromDate,"toDate":toDate,"title":jobTitle,"rules":rules}
    jobString = json.dumps(job).encode()
    print (jobString)
#the job string includes all the information you put above.
    print ('\n' + 'creating job: ' + jobTitle + '\n')
    job_page = request_url(url, jobString, base64string)
    parse_job_page = json.loads(job_page)
    job_url = parse_job_page['jobURL'] # This is the getting the job url from the page, whose' content is in a jason format.

    # wait for 30s first before checking - request taking time to complete and calculate
    time.sleep(60)  # 60s

    # monitor status
    print ('requesting a quote for the job ...')

    job_status = ''
    while job_status !='quoted':

        time.sleep(60)

        status_page = request_url(job_url, None, base64string)
        parse_status_page = json.loads(status_page)
        job_status = parse_status_page['status']

    print ('job quoted - ')
    print ('    estimated downloading time: ' + parse_status_page['quote']['estimatedDurationHours'] + ' (hr)')
    print ('    estimated file size:' + parse_status_page['quote']['estimatedFileSizeMb'] + ' Mb')
    print ('\n')

    # check for accepting job
    # check for quoted size
    quoted_hours = float(parse_status_page['quote']['estimatedDurationHours'])
    quoted_size = float(parse_status_page['quote']['estimatedFileSizeMb'])
    if quoted_hours > 15*24:   # the file will expire after 15 days
        choice = 'reject'
    else:
        choice = 'accept'

    print ('job ' + choice + 'ed' + '\n')

    payload = '{"status":"' + choice + '"}'

    job_url2 = parse_status_page['jobURL']

    #output to text file:
    file_name = jobTitle + '.txt'
    f = open(file_name,'w')
    f.write(job_url2)
    f.write('\n')
    f.close()
=======
# -*- coding: utf-8 -*-
"""
# date: Wed Sep 19 10:37:34 2015
# last update: Thurs 3.10.17
# author: danyang / modified by amit goldenberg
# parts of the code are modified from: CreateHistoricalJob.py, MonitorJobStatus.py and AcceptRejectHistoricalJob.py
#                                      https://github.com/gnip/support/tree/master/Historical%20PowerTrack/Python
# description: (1) post job, (2) get quotes (duration and size of files), (3) accept/reject job (4) output job url for monitoring and downloading
# inputs: UN, PWD, account (individual's information)
#         request: fromDate, toDate, jobTitle, rules (search keywords etc)
# output: jobTitle.txt with job url for monitoring progress and downloading upon completion
"""

import urllib.request
import base64
import json
import sys
import time

def request_url(url, jobString, base64string):
    base64string = base64.encodebytes(('%s:%s' % (UN, PWD)).encode()).decode().replace('\n', '')
    req = urllib.request.Request(url=url, data=jobString)
    req.add_header('Content-type', 'application/json')
    req.add_header("Authorization", "Basic %s" % base64string)
# automatizing the usl analysis.
    try:
        response = urllib.request.urlopen(req)
        the_page = response.read()
        return the_page
    except urllib.error.HTTPError as e:
        print (e.read())


if __name__ == "__main__":

    UN = 'chagag@gmail.com' # change to my email and my password
    PWD = 'fabrizy8'
    account = 'StanfordResearch'
    base64string = base64.encodebytes(('%s:%s' % (UN, PWD)).encode()).decode().replace('\n', '')

    # create job
    url = 'https://gnip-api.gnip.com/historical/powertrack/accounts/' + account + '/publishers/twitter/jobs.json'
    publisher = "twitter"
    streamType = "track_v2"
    dataFormat = "activity_streams" #raceriotsUSA
    fromDate = "201408112359" # This time is inclusive -- meaning the minute specified will be included in the data returned
    toDate =   "201408122359" # This time is exclusive -- meaning the data returned will not contain the minute specified, but will contain the minute immediately preceding it
    jobTitle = "test-job-python_amit5"
    rules = [{"value":"Amit Goldenberg"}]
    job = {"publisher":publisher,"streamType":streamType,"dataFormat":dataFormat,"fromDate":fromDate,"toDate":toDate,"title":jobTitle,"rules":rules}
    jobString = json.dumps(job).encode()
    print (jobString)
#the job string includes all the information you put above.
    print ('\n' + 'creating job: ' + jobTitle + '\n')
    job_page = request_url(url, jobString, base64string)
    parse_job_page = json.loads(job_page)
    job_url = parse_job_page['jobURL'] # This is the getting the job url from the page, whose' content is in a jason format.

    # wait for 30s first before checking - request taking time to complete and calculate
    time.sleep(60)  # 60s

    # monitor status
    print ('requesting a quote for the job ...')

    job_status = ''
    while job_status !='quoted':

        time.sleep(60)

        status_page = request_url(job_url, None, base64string)
        parse_status_page = json.loads(status_page)
        job_status = parse_status_page['status']

    print ('job quoted - ')
    print ('    estimated downloading time: ' + parse_status_page['quote']['estimatedDurationHours'] + ' (hr)')
    print ('    estimated file size:' + parse_status_page['quote']['estimatedFileSizeMb'] + ' Mb')
    print ('\n')

    # check for accepting job
    # check for quoted size
    quoted_hours = float(parse_status_page['quote']['estimatedDurationHours'])
    quoted_size = float(parse_status_page['quote']['estimatedFileSizeMb'])
    if quoted_hours > 15*24:   # the file will expire after 15 days
        choice = 'reject'
    else:
        choice = 'accept'

    print ('job ' + choice + 'ed' + '\n')

    payload = '{"status":"' + choice + '"}'

    job_url2 = parse_status_page['jobURL']

    #output to text file:
    file_name = jobTitle + '.txt'
    f = open(file_name,'w')
    f.write(job_url2)
    f.write('\n')
    f.close()
>>>>>>> 31fe29a42eb00bf3efb108b41c8a88579ddd3671
