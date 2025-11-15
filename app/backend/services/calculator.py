def calculate_sip(monthly_sip: float, duration_months: int, expected_return_rate: float):
    """
    Calculate the SIP investment details.

    :param monthly_sip: The amount invested monthly.
    :param duration_months: The total duration of the investment in months.
    :param expected_return_rate: The expected annual return rate (in percentage).
    :return: A tuple containing total investment, total profit, total value, and CAGR.
    """
    monthly_rate_return = expected_return_rate / 12

    #SIP Future Value Formula
    final_value = monthly_sip * (((1 +monthly_rate_return / 100) ** duration_months - 1) / monthly_rate_return) * (1 + monthly_rate_return)

    total_investment = monthly_sip * duration_months
    total_profit = final_value - total_investment

    #CAGR Calculation
    years = duration_months / 12
    cagr = ((final_value / total_investment) ** (1 / years) - 1) if total_investment != 0 and duration_months != 0 else 0

    return total_investment, final_value, total_profit, cagr 