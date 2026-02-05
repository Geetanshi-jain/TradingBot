import typer
from rich.console import Console
from rich.table import Table
from loguru import logger
from .client import BinanceClientWrapper
from .orders import OrderManager
from .validators import (
    validate_symbol, validate_side, validate_order_type, 
    validate_quantity, validate_price
)
from .logging_config import setup_logging

app = typer.Typer(help="Binance Futures Trading Bot CLI")
console = Console()

def init_components():
    setup_logging()
    try:
        client_wrapper = BinanceClientWrapper()
        order_manager = OrderManager(client_wrapper)
        return client_wrapper, order_manager
    except Exception as e:
        console.print(f"[bold red]Initialization Error:[/bold red] {e}")
        raise typer.Exit(code=1)

@app.command()
def market(
    symbol: str = typer.Argument(..., help="Symbol (e.g., BTCUSDT)", callback=validate_symbol),
    side: str = typer.Argument(..., help="BUY or SELL", callback=validate_side),
    quantity: float = typer.Argument(..., help="Quantity to trade", callback=validate_quantity),
):
    """Place a MARKET order on Binance Futures Testnet."""
    client_wrapper, order_manager = init_components()
    
    console.print(f"Placing [bold cyan]MARKET[/bold cyan] {side} order for {quantity} {symbol}...")
    
    response = order_manager.place_order(
        symbol=symbol,
        side=side,
        order_type="MARKET",
        quantity=quantity
    )
    
    console.print(order_manager.format_order_summary(response))

@app.command()
def limit(
    symbol: str = typer.Argument(..., help="Symbol (e.g., BTCUSDT)", callback=validate_symbol),
    side: str = typer.Argument(..., help="BUY or SELL", callback=validate_side),
    quantity: float = typer.Argument(..., help="Quantity to trade", callback=validate_quantity),
    price: float = typer.Argument(..., help="Limit price", callback=lambda v: validate_price(v, "LIMIT")),
):
    """Place a LIMIT order on Binance Futures Testnet."""
    client_wrapper, order_manager = init_components()
    
    console.print(f"Placing [bold cyan]LIMIT[/bold cyan] {side} order for {quantity} {symbol} at price {price}...")
    
    response = order_manager.place_order(
        symbol=symbol,
        side=side,
        order_type="LIMIT",
        quantity=quantity,
        price=price
    )
    
    console.print(order_manager.format_order_summary(response))

@app.command()
def stop_market(
    symbol: str = typer.Argument(..., help="Symbol (e.g., BTCUSDT)", callback=validate_symbol),
    side: str = typer.Argument(..., help="BUY or SELL", callback=validate_side),
    quantity: float = typer.Argument(..., help="Quantity to trade", callback=validate_quantity),
    stop_price: float = typer.Argument(..., help="Stop price for the order"),
):
    """Place a STOP_MARKET order (Bonus Feature)."""
    client_wrapper, order_manager = init_components()
    
    console.print(f"Placing [bold magenta]STOP_MARKET[/bold magenta] {side} order for {quantity} {symbol} at stop price {stop_price}...")
    
    response = order_manager.place_order(
        symbol=symbol,
        side=side,
        order_type="STOP_MARKET",
        quantity=quantity,
        stop_price=stop_price
    )
    
    console.print(order_manager.format_order_summary(response))

@app.command()
def status():
    """Check connectivity to Binance Futures Testnet."""
    client_wrapper, _ = init_components()
    if client_wrapper.ping():
        console.print("[bold green]Online:[/bold green] Connected to Binance Futures Testnet.")
    else:
        console.print("[bold red]Offline:[/bold red] Could not connect to Binance Futures.")

if __name__ == "__main__":
    app()
