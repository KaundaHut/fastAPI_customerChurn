
from pydantic import BaseModel

## Schema validation
class CustomerChurn(BaseModel):
              region:str
              tenure:int
              age:int
              marital:str
              address:int
              income:float
              ed:str
              employ:int
              retire:str
              gender:str
              reside:int
              tollfree:str
              equip:str
              callcard:str
              wireless:str
              multline:str
              voice:str
              pager:str
              internet:str
              callid:str
              callwait:str
              forward:str
              confer:str
              ebill:str
              loglong:float
              lninc:float
              custcat:str
              total_monthly_bill:float
              total_bill:float
             