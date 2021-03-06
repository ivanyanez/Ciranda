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
import jinja2
import os

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname("templates"))
)


class MainHandler(webapp2.RequestHandler):
    def get(self):
        main_template = env.get_template("templates/index.html")
        self.response.write(main_template.render())

class ProjetoHandler(webapp2.RequestHandler):
    def get(self):
        main_template = env.get_template("templates/projeto.html")
        self.response.write(main_template.render())



class AdoteHandler(webapp2.RequestHandler):
    def get(self):
        main_template = env.get_template("templates/faleconosco.html")
        self.response.write(main_template.render())


class FaleConoscoHandler(webapp2.RequestHandler):
    def get(self):
        main_template = env.get_template("templates/faleconosco.html")
        self.response.write(main_template.render())



app =  webapp2.WSGIApplication([
    ('/', AdoteHandler),
    ('/adote', AdoteHandler),
    ('/faleconosco', FaleConoscoHandler),
    ('/projeto', ProjetoHandler)

], debug=True)







