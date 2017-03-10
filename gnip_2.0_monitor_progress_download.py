<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
# date: Wed Sep 16 10:37:34 2015
# last update: Thurs Sep 19 2015
# author: danyang /modified by amit
# parts of the code is modified from: MonitorJobStatus.py
#                                     https://github.com/gnip/support/tree/master/Historical%20PowerTrack/Python
# older version: monitor_progress_download.py
# description: (1) to read the job url of a particular job, (2) check for job completion (percentComplete = 100)
#              and (3) to download the data upon completion to the respective job folder
# inputs: UN, PWD, account (individual's information)
#         jobTitle
# output: (1) completion status, (2) downloaded data files
# undecided add on: unzip and parse to json
"""

from __future__ import division
import urllib
#import urllib2
import base64
import json
import os
import gzip
#from __future__ import division

def request_url(url, jobString, base64string):
      req = urllib2.Request(url=url, data=jobString)
      req.add_header('Content-type', 'application/json')
      req.add_header("Authorization", "Basic %s" % base64string)

      try:
          response = urllib.request.urlopen(req)
          the_page = response.read()
          return the_page
      except urllib.error.HTTPError as e:
          print (e.read())


if __name__ == "__main__":

        UN = 'example@email.com'
        PWD = 'password'
        account = 'accountname'
        base64string = base64.encodebytes(('%s:%s' % (UN, PWD)).encode()).decode().replace('\n', '')

        jobTitle = "your_previous_job_title" # you have to specify the actual job title to reference to what was previously found.

        #url_file_name = jobTitle + '_json_job_url.txt'
        url_file_name = jobTitle + '.txt'
        furl = open(url_file_name, 'r')
        line_n = furl.readline()
        job_url = line_n.strip('\n')
        furl.close()

        print ('Updating job retrieving status')
        job_page = request_url(job_url, None, base64string)
        parse_job_page = json.loads(job_page)
        job_status = parse_job_page['status']

        # check for completion
        if parse_job_page['percentComplete'] ==100:
            print ('\n' + 'start to download data files...')
# once the job is complete we need to be able to loop for all the JSON files in order to be able to get the jobs and analyze whatever we want to see.

            # create directory for the current job for file downloading
            data_dir = jobTitle + '/'       #???? backslash?
            if not os.path.exists(data_dir):
                os.makedirs(data_dir)

            data_url = parse_job_page['results']['dataURL']
            data_page = request_url(data_url,None, base64string)
            parse_data_page = json.loads(data_page)
            num_url = len(parse_data_page['urlList']) # this just checks the number of generated JSON

            #download files
            #for i in range(2): # this range is just because danyang chose to do this. We can take as much as we want.
            for i in range(num_url):
                url_i = parse_data_page['urlList'][i]  #use for downloading - usrllist is a dictionary and we are taking i which the number in the range.
                name_temp1 = url_i.split('?') # everything that comes after the question mark means nothing and we want jus tthe link,
                name_temp2 = name_temp1[0].split('/')
                file_name = name_temp2[-5]+name_temp2[-4]+name_temp2[-3]+name_temp2[-2]+name_temp2[-1]
                outfile_name = data_dir + file_name
                #old - outfile_name = data_dir + name_temp2[-1] # this is to get the name of the file. We are cutting it until the last /
                outfile = urllib.URLopener()
                outfile.retrieve(url_i, outfile_name) # these two lines are made to rertrive the lines from the linst and save it .
                #unzip the files

            print ('downloading complete...')

        else:
            completion_progress = str(parse_job_page['percentComplete'])

            estimated_duration = float(parse_job_page['quote']['estimatedDurationHours'])
            estimated_remaining_time = estimated_duration-estimated_duration*parse_job_page['percentComplete']/100

            print (completion_progress + '%  completed'  + '\n' + 'Please try again later for downloading...')
            print ('estimated time remaining: ' + str(estimated_remaining_time) + ' (hr)' + '\n')
=======
# -*- coding: utf-8 -*-
"""
# date: Wed Sep 16 10:37:34 2015
# last update: Thurs Sep 19 2015
# author: danyang /modified by amit
# parts of the code is modified from: MonitorJobStatus.py
#                                     https://github.com/gnip/support/tree/master/Historical%20PowerTrack/Python
# older version: monitor_progress_download.py
# description: (1) to read the job url of a particular job, (2) check for job completion (percentComplete = 100)
#              and (3) to download the data upon completion to the respective job folder
# inputs: UN, PWD, account (individual's information)
#         jobTitle
# output: (1) completion status, (2) downloaded data files
# undecided add on: unzip and parse to json
"""

from __future__ import division
import urllib
#import urllib2
import base64
import json
import os
import gzip
#from __future__ import division

def request_url(url, jobString, base64string):
      req = urllib2.Request(url=url, data=jobString)
      req.add_header('Content-type', 'application/json')
      req.add_header("Authorization", "Basic %s" % base64string)

      try:
          response = urllib.request.urlopen(req)
          the_page = response.read()
          return the_page
      except urllib.error.HTTPError as e:
          print (e.read())


if __name__ == "__main__":

        UN = 'chagag@gmail.com'
        PWD = 'fabrizy8'
        account = 'StanfordResearch'
        base64string = base64.encodebytes(('%s:%s' % (UN, PWD)).encode()).decode().replace('\n', '')

        jobTitle = "test-job-python_amit5" # you have to specify the actual job title to reference to what was previously found.

        #url_file_name = jobTitle + '_json_job_url.txt'
        url_file_name = jobTitle + '.txt'
        furl = open(url_file_name, 'r')
        line_n = furl.readline()
        job_url = line_n.strip('\n')
        furl.close()

        print ('Updating job retrieving status')
        job_page = request_url(job_url, None, base64string)
        parse_job_page = json.loads(job_page)
        job_status = parse_job_page['status']

        # check for completion
        if parse_job_page['percentComplete'] ==100:
            print ('\n' + 'start to download data files...')
# once the job is complete we need to be able to loop for all the JSON files in order to be able to get the jobs and analyze whatever we want to see.

            # create directory for the current job for file downloading
            data_dir = jobTitle + '/'       #???? backslash?
            if not os.path.exists(data_dir):
                os.makedirs(data_dir)

            data_url = parse_job_page['results']['dataURL']
            data_page = request_url(data_url,None, base64string)
            parse_data_page = json.loads(data_page)
            num_url = len(parse_data_page['urlList']) # this just checks the number of generated JSON

            #download files
            #for i in range(2): # this range is just because danyang chose to do this. We can take as much as we want.
            for i in range(num_url):
                url_i = parse_data_page['urlList'][i]  #use for downloading - usrllist is a dictionary and we are taking i which the number in the range.
                name_temp1 = url_i.split('?') # everything that comes after the question mark means nothing and we want jus tthe link,
                name_temp2 = name_temp1[0].split('/')
                file_name = name_temp2[-5]+name_temp2[-4]+name_temp2[-3]+name_temp2[-2]+name_temp2[-1]
                outfile_name = data_dir + file_name
                #old - outfile_name = data_dir + name_temp2[-1] # this is to get the name of the file. We are cutting it until the last /
                outfile = urllib.URLopener()
                outfile.retrieve(url_i, outfile_name) # these two lines are made to rertrive the lines from the linst and save it .
                #unzip the files

            print ('downloading complete...')

        else:
            completion_progress = str(parse_job_page['percentComplete'])

            estimated_duration = float(parse_job_page['quote']['estimatedDurationHours'])
            estimated_remaining_time = estimated_duration-estimated_duration*parse_job_page['percentComplete']/100

            print (completion_progress + '%  completed'  + '\n' + 'Please try again later for downloading...')
            print ('estimated time remaining: ' + str(estimated_remaining_time) + ' (hr)' + '\n')
>>>>>>> 443ce15d9cd84ac9590647263bf95f7f4b8b135a
