#!/usr/local/bin/python
"""
__Defaults__

Contains defaults for TaskQueue modules use.
Any of these may be overriden in the configuration file
(object), but otherwise the values here are used.

Please do not change these values, rather override
them in the configuration file.
"""

# Default formatter for TQ listener (json)
# Do not change if the pilots are not aware!
listenerFormatter = "TQComp.DefaultFormatter"

# Default tasks-pilots matcher (selects a task for a pilot requesting one)
matcherPlugin = "TQComp.FlexPyMatchmaker"

# Max number of threads for the listener (including its handlers)
listenerMaxThreads = 10

# How often to check for heartbeat/TTL status of pilots (seconds)
heartbeatPollPeriod = 300

# After how long a no reporting pilot is considered dead (seconds)
heartbeatValidity = 1800