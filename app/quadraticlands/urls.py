# -*- coding: utf-8 -*-
"""Handle grant URLs.

Copyright (C) 2020 Gitcoin Core

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.

"""
from django.urls import path, re_path

from quadraticlands.helpers import claim, set_mission_status
from quadraticlands.views import (
    base, index, mission_answer, mission_base, mission_index, mission_question, mission_state,
)

app_name = 'quadraticlands'

# TODO Zak - quadraticlands VS quadraticlands/ 
# possible solution - https://stackoverflow.com/questions/1596552/django-urls-without-a-trailing-slash-do-not-redirect


# this is better for now but the these should probably be updated to use regex for supported missions and kick 404 for everything else
urlpatterns = [
    path('', index, name='quadraticlands'),
    path('mission', mission_index, name='mission'),
    path('claim', claim, name='claim_json'),
    path('set_mission_status', set_mission_status, name='set_mission_status'),  
    path('<str:base>', base, name='quadraticlands'),
    path('mission/<str:mission_name>', mission_base, name='mission'),
    path('mission/<str:mission_name>/<str:mission_state>', mission_state, name='mission_state'),
    path('mission/<str:mission_name>/<str:mission_state>/<int:question_num>', mission_question, name='mission_questions'),
    path('mission/<str:mission_name>/<str:mission_state>/<int:question_num>/<str:answer>', mission_answer, name='mission_answer'),
    ]
