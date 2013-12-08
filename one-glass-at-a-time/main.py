#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import json
import logging

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
from apiclient.discovery import build



class MainHandler(webapp2.RequestHandler):
	def get(self):
		self.response.write('<b>Derpy Glass!</b>')
		CLIENTSECRETS_LOCATION = 'client_secrets.json'
		REDIRECT_URI = 'http://one-glass-at-a-time.appspot.com/oauth2callback'
		SCOPES = [
    	'https://www.googleapis.com/auth/glass.timeline',
    	'https://www.googleapis.com/auth/userinfo.profile',
    	# Add other requested scopes.
		]
		flow = flow_from_clientsecrets('client_secrets.json',
                               scope=SCOPES,
                               redirect_uri=REDIRECT_URI)
		auth_uri = flow.step1_get_authorize_url()
		#Redirect the user to auth_uri on your platform.
		self.response.write('<br><a href="'+auth_uri+'">'+auth_uri+'</a>')
class NotificationHandler(webapp2.RequestHandler):
	def parse_notification(request_body):
		"""Parse a request body into a notification dict.

		Params:
		request_body: The notification payload sent by the Mirror API as a string.
		Returns:
		Dict representing the notification payload.
		"""
		return json.load(request_body)

class ImageHandler(webapp2.RequestHandler):
	def get(self, image_id):
		self.response.write('This is the ImageHandler. '
			'The image id is %s' % image_id)

app = webapp2.WSGIApplication([
	(r'/', MainHandler),
	(r'/notification', NotificationHandler),
	(r'/images/(\d+)', ImageHandler),
], debug=True)