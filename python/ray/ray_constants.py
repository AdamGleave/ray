from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

"""Ray constants used in the Python code."""


# Abort autoscaling if more than this number of errors are encountered. This
# is a safety feature to prevent e.g. runaway node launches.
AUTOSCALER_MAX_NUM_FAILURES = 5

# The maximum number of nodes to launch in a single request.
# Multiple requests may be made for this batch size, up to
# the limit of AUTOSCALER_MAX_CONCURRENT_LAUNCHES.
AUTOSCALER_MAX_LAUNCH_BATCH = 5

# Max number of nodes to launch at a time.
AUTOSCALER_MAX_CONCURRENT_LAUNCHES = 10

# Interval at which to perform autoscaling updates.
AUTOSCALER_UPDATE_INTERVAL_S = 5

# The autoscaler will attempt to restart Ray on nodes it hasn't heard from
# in more than this interval.
AUTOSCALER_HEARTBEAT_TIMEOUT_S = 30

# Max number of retries to AWS (default is 5, time increases exponentially)
BOTO_MAX_RETRIES = 12
