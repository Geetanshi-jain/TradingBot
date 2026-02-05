from loguru import logger
from binance.exceptions import BinanceAPIException
from .client import BinanceClientWrapper

class OrderManager:
    def __init__(self, client_wrapper: BinanceClientWrapper):
        self.client = client_wrapper.get_client()

    def place_order(self, symbol, side, order_type, quantity, price=None, stop_price=None):
        try:
            params = {
                "symbol": symbol,
                "side": side,
                "type": order_type,
                "quantity": quantity,
            }

            if order_type == "LIMIT":
                params["price"] = price
                params["timeInForce"] = "GTC"  # Good Till Cancelled
            
            if order_type == "STOP_MARKET":
                params["stopPrice"] = stop_price

            logger.info(f"Sending {order_type} request: {params}")
            
            # Use futures_create_order for USDT-M Futures
            response = self.client.futures_create_order(**params)
            
            logger.info(f"Order success: {response.get('orderId')}")
            return response

        except BinanceAPIException as e:
            logger.error(f"Binance API Error: {e.status_code} - {e.message}")
            return {"error": e.message, "status_code": e.status_code}
        except Exception as e:
            logger.error(f"Unexpected error placing order: {str(e)}")
            return {"error": str(e)}

    def format_order_summary(self, response):
        if "error" in response:
            return f"[bold red]FAILED[/bold red]: {response['error']}"
        
        order_id = response.get("orderId")
        status = response.get("status")
        executed_qty = response.get("executedQty")
        avg_price = response.get("avgPrice", "N/A")
        
        summary = (
            f"[bold green]SUCCESS[/bold green]\n"
            f"Order ID: {order_id}\n"
            f"Status: {status}\n"
            f"Executed Qty: {executed_qty}\n"
            f"Avg Price: {avg_price}"
        )
        return summary
