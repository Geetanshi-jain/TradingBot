from loguru import logger
import re

def validate_symbol(symbol: str):
    """Simple validation for USDT-M symbols."""
    symbol = symbol.upper()
    if not re.match(r"^[A-Z0-9]{3,12}USDT$", symbol):
        logger.warning(f"Invalid symbol format: {symbol}")
        raise ValueError(f"Invalid symbol: {symbol}. Must be a valid USDT pair (e.g., BTCUSDT)")
    return symbol

def validate_side(side: str):
    side = side.upper()
    if side not in ["BUY", "SELL"]:
        logger.warning(f"Invalid side: {side}")
        raise ValueError("Side must be BUY or SELL")
    return side

def validate_order_type(order_type: str):
    order_type = order_type.upper()
    if order_type not in ["MARKET", "LIMIT", "STOP_MARKET"]:
        logger.warning(f"Invalid order type: {order_type}")
        raise ValueError("Order type must be MARKET, LIMIT, or STOP_MARKET")
    return order_type

def validate_quantity(quantity: float):
    if quantity <= 0:
        logger.warning(f"Invalid quantity: {quantity}")
        raise ValueError("Quantity must be greater than 0")
    return quantity

def validate_price(price: float, order_type: str):
    if order_type == "LIMIT" and (price is None or price <= 0):
        logger.warning(f"Invalid price for LIMIT order: {price}")
        raise ValueError("Price must be greater than 0 for LIMIT orders")
    return price
