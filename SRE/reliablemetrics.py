from datetime import datetime
from calendar import monthrange

class ReliableMetrics:
    """
    This class will have all the metrics related to SRE
    uptime =>  will calculate uptime for a month if no value passed it will take the current month by default
    downtime => Default = 0
    SLI => Default = 0
    SLA => Default = 99.99
    SLO => Default = 99.99
    """    
    def uptime(self,year=int(datetime.today().year),month=int(datetime.today().month)):
        """ Calculate uptime in minutes"""
        
        list_month = []
        self.year = year
        self.month = month 
        
        month_in_days = list(monthrange(year,month))
        
        for m in month_in_days:
            list_month.append(int(m))
        
        up_time = list_month[1] * 24 * 60
        
        return up_time

    def downtime(self,down_time=0):
        """ Calculate downtime in minutes """
        
        self.down_time = down_time
        
        return down_time
    
    def sla(self,customer_sla=99.99):
        """ Calculate service level agreement """
        
        self.customer_sla = customer_sla
        
        return customer_sla
    
    def slo(self,objective=99.99):
        """ Calculate service level objectives """
        
        self.objective = objective
        
        return objective
    
    def sli(self,indicator=0):
        """ Calculate service level indicator """
        
        self.indicator = indicator
        
        return indicator
    
    def availability(self,up_time=100,down_time=0,dec_point=3):
        """ Calculate availability in %  
        input: uptime , downtime, results with number of decimal points
        """
        
        self.up_time = up_time
        self.down_time = down_time
        self.dec_point = dec_point
        
        avail_percentage = round(float((up_time/(up_time+down_time))*100),dec_point)
        
        return avail_percentage
    
    def mtbf(self,mt_bf=0):
        """ Calculate mean time between failures """
        
        self.mt_bf = mt_bf
        
        return mt_bf
    
    def mttr(self,mt_tr=0):
        """ Calculate mean time to repair """
        
        self.mt_tr = mt_tr
        
        return mt_tr

    def get_all_metrics(self):
        """
        Get all the metrics related to sre
        """
        up_time = self.uptime()
        down_time = self.downtime()
        customer_sla = self.sla()
        objective = self.slo()
        indicator = self.sli()
        avail_percentage = self.availability()
        mt_bf = self.mtbf()
        mt_tr = self.mttr()
        
        list_results = [up_time,down_time,customer_sla,objective,indicator,avail_percentage,mt_bf,mt_tr]
        
        return list_results

    def set_all_metrics(self,**kwargs):
        if kwargs is not None:
            try:
                year = kwargs['year']
                month = kwargs['month']
                d_time = kwargs['downtime']
                u_time = self.uptime(year=year,month=month)
                self.sla(kwargs['sla'])
                self.slo(kwargs['slo'])
                self.sli(kwargs['sli'])
                self.availability(up_time=u_time,down_time=d_time)
                self.mtbf(kwargs['mtbf'])
                self.mttr(kwargs['mttr'])
                return 'OK'
            except:
                raise Exception("ValidationError: Check the input arguments")
        else:
            return 'FAILED'           