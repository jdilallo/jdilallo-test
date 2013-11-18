===========================================
The Google Ads APIs Python Client Libraries
===========================================

The Google Ads APIs Python Client Libraries support the following products:

* {{ adwords }}
* {{ dfa }}
* {{ dfp }}

You can find more information about the Google Ads Python Client Libraries
`here <https://code.google.com/p/google-api-ads-python/>`_.

Installation
============

You have two options for installing the Ads Python Client Libraries:

* Install with a tool such as pip::

  $ sudo pip install adspygoogle

* Install manually after downloading and extracting the tarball::

  $ sudo python setup.py install

Examples and Configuration Scripts
==================================

This package only provides the core components necessary to use the client
libraries. If you would like to obtain example code for any of the included
client libraries, you can find it on our
`downloads page <https://code.google.com/p/google-api-ads-python/downloads/list>`_.

Known Issues
============

* The installation of PyXML and cElementTree will fail on Ubuntu 13.04, which
  is why these are now optional. If you are trying to install adspygoogle
  on Ubuntu 13.04, you should avoid installing these dependencies. If you need
  to use either of these dependencies, there is currently a work-around that can
  be found in
  `this bug <https://bugs.launchpad.net/ubuntu/+source/python2.7/+bug/1238244/>`_.

Contact Us
==========

Do you have an issue using the Ads Python Client Libraries? Or perhaps some
feedback for how we can improve them? Feel free to let us know on our
`issue tracker <https://code.google.com/p/google-api-ads-python/issues/list>`_.