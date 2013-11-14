#!/usr/bin/python
#
# Copyright 2012 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This code example gets an order by its id. To determine which orders exist,
run get_all_orders.py."""

__author__ = 'api.shamjeff@gmail.com (Jeff Sham)'

# Locate the client library. If module was installed via "setup.py" script, then
# the following two lines are not needed.
import os
import sys
sys.path.insert(0, os.path.join('..', '..', '..', '..'))

# Import appropriate classes from the client library.
from adspygoogle import DfpClient


# Initialize client object.
client = DfpClient(path=os.path.join('..', '..', '..', '..'))

# Initialize appropriate service.
order_service = client.GetService('OrderService', version='v201204')

# Set the id of the order to get.
order_id = 'INSERT_ORDER_ID_HERE'

# Get order.
order = order_service.GetOrder(order_id)[0]

# Display results.
print ('Order with id \'%s\', name \'%s\', and advertiser id \'%s\' was '
       'found.' % (order['id'], order['name'], order['advertiserId']))
