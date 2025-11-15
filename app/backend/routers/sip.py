from fastapi import APIRouter
from app.backend.schemas.sip import SIPRequest, SIPResponse
from app.backend.services.calculator import calculate_sip


router = APIRouter(prefix="/sip", tags=["SIP Calculator"])

@router.post("/calculate", response_model=SIPResponse)
async def calculate_sip_endpoint(sip_request: SIPRequest):
    total_investment, total_value, total_profit, cagr = calculate_sip(
        monthly_sip=sip_request.monthly_sip,
        duration_months=sip_request.duration_months,
        expected_return_rate=sip_request.expected_return_rate
    )

    return SIPResponse(
        fund_name=sip_request.fund_name,
        total_investment=total_investment,
        total_profit=total_profit,
        total_value=total_value,
        cagt=cagr
    )