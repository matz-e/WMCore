"""
_GetParentId_

MySQL implementation of WorkQueueElement.GetParentId
"""

__all__ = []
__revision__ = "$Id: GetParentId.py,v 1.2 2009/11/12 16:43:31 swakef Exp $"
__version__ = "$Revision: 1.2 $"

from WMCore.Database.DBFormatter import DBFormatter
from WMCore.WorkQueue.Database import States

class GetParentId(DBFormatter):
    sql = """SELECT we.parent_queue_id
                FROM wq_element we
                WHERE we.subscription_id = :subscription
          """

    def execute(self, subs, conn = None, transaction = False):
        binds = [{'subscription' : x} for x in ids]
        result = self.dbi.processData(self.sql, binds, conn = conn,
                             transaction = transaction)
        return self.formatDict(result)
