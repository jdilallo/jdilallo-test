#The googleads Python client library


This client library simplifies accessing Google's SOAP Ads APIs - AdWords,
DoubleClick Ad Exchange SOAP, DoubleClick for Advertisers, and DoubleClick for
Publishers. The library provides easy ways to store your authentication and
create SOAP web service clients. It also contains example code to help you get
started integrating with our APIs.


##How do I get started?
Install or update the library from PyPI. If you're using pip, this is as easy
as:

`$ pip install [--upgrade] googleads`

If you don't want to install directly from PyPI, you can download the library
as a tarball and then install it manually. The download can be found here:
https://pypi.python.org/pypi/googleads
Navigate to the directory that contains your downloaded unzipped client
library and run the "setup.py" script to install the "googleads"
module.

`$ python setup.py build install`

You can find code examples in the git repo and in the library's releases within
the examples folder.

##Where do I submit bug reports and/or feature requests?

Use the issue tracker at:
  INSERT_URL_HERE

Make sure to subscribe to our Google Plus page for API change announcements and
other news:

  https://plus.google.com/+GoogleAdsDevelopers

##How do I log SOAP interactions?
The library uses Python's built in logging framework. If you wish to log your
SOAP interactions to stdout, you can do the following:
```python
logging.basicConfig(level=logging.INFO)
logging.getLogger('suds.transport').setLevel(logging.DEBUG)
```
If you wish to log to a file, you'll need to attach a log handler to this source
which is configured to write the output to a file.

##I'm familiar with suds. Can I use suds features with this library?
Yes, you can. The services returned by the `client.GetService()` functions all
have a reference to the underlying suds client stored in the `suds_client` 
attribute. You can retrieve the client and use it in familiar ways:
```python
client = AdWordsClient.LoadFromStorage()
campaign_service = client.GetService('CampaignService')
suds_client = campaign_service.suds_client

campaign = suds_client.factory.create('Campaign')
campaign.name = 'My Campaign'
campaign.status = 'PAUSED'
# Set any attributes on the campaign that you need.
suds_client.factory.create('CampaignOperation')
operation.operator = 'ADD'
operation.operand = campaign

# If you set the SOAP headers yourself, you can use the suds_client.service
# directly. Using the service object returned from the client.GetService() call
# will set the SOAP headers for you.
campaign_service.mutate([operation])
```


##External Dependencies:


    - oauthlib             -- http://pypi.python.org/pypi/oauthlib/
    - suds-jurko           -- http://pypi.python.org/pypi/suds-jurko/
    - pyYAML               -- http://pypi.python.org/pypi/pyYAML/
    - mock                 -- http://pypi.python.org/pypi/mock
                              (only needed to run unit tests)


##Authors:
    jdilallo@google.com (Joseph DiLallo)
