from god.common.enum import Enum

Clusterstate=Enum(["INITIALIZING",
                   "STARTING",
                   "INITIALIZING_FAILED",
                   "DELETING",
                   'DELETED',
                   "RUNNING",
                   "MAINTAIN",
                   "SCALING",
                   "STOPPING",
                   "STOPPED"])

Nodestate = Enum(["STAGING",
                  "FAILED",
                  "STARTING",
                  "RUNNING",
                  "STOPPING",
                  "STOPPED",
                  "MAINTAIN",
                  "DELETING",
                  "DELETED"])

