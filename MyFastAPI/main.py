
from pydantic import BaseModel

## Schema validation
class CustomerChurn(BaseModel):
               tenure: int
               age: int 
               address: int 
               income: float 
               employ: int 
               retire: int 
               reside: int
               tollfree: int 
               equip: int
               callcard: int
               wireless: int
               multline: int
               voice: int
               pager: int
               internet: int
               callid: int
               callwait: int
               forward: int
               confer: int
               ebill: int
               loglong: float
               Ininc: float
               total_monthly_bill: float
               total_bill: float 
               region_zone_1: int
               region_zone_2: int
               region_zone_3: int
               marital_married: int
               marital_unmarried: int
               ed_college_degree: int
               ed_did_not_complete_high_school:int
               ed_high_school_degree:int
               ed_post_undergraduate_degree:int
               ed_some_college:int
               gender_female:int
               gender_male:int
               custcat_basic_service:int
               custcat_e_service:int
               custcat_plus_service:int
               custcat_total_service:int
                       