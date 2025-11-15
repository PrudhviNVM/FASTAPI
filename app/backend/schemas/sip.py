from pydantic import BaseModel 

class SIPRequest(BaseModel):
    fund_name: str
    monthly_sip: float
    duration_months: int
    expected_return_rate: float


class SIPResponse(BaseModel):
    fund_name: str
    total_investment: float
    total_profit: float
    total_value: float
    cagt: float

#How to stop auto sugegstions in vscode
