from calendar import monthrange
from reliablemetrics import ReliableMetrics

sre = ReliableMetrics()

var_1 = sre.uptime(2040,2)
print(var_1)

var_2 = sre.downtime(10)
print(var_2)

var_3 = sre.sla()
print(var_3)

var_4 = sre.slo()
print(var_4)

var_5 = sre.sli()
print(var_5)

var_6 = sre.availability(var_1,var_2)
print(var_6)

var_7 = sre.get_all_metrics()
print(var_7)

var_8 = sre.set_all_metrics(year=202,month=12,downtime=1,sla=99.99,slo=99.99,sli=0,mtbf=10,mttr=60)
print(var_8)

var_9 = sre.error_budget(99.99)
print(var_9)