# infrastructure-testapp
Test application for p6 pipservice installer

This app should install by adding the following to any node yaml:

~~~yaml
pipservice:
  testapp:
    tag: 'master'
~~~

It should then install the pips, enable the service as laid out in the testapp.service systemd script and run it, producing a "test app still works" every minute in syslog.
