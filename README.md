# Binance Futures Trading Bot (Testnet)

A simplified Python trading bot for placing orders on Binance Futures Testnet (USDT-M).

## Features
- **Place Market Orders**: Quick execution at best available price.
- **Place Limit Orders**: Execute at a specific price or better.
- **Connectivity Check**: Verify API connection to the testnet.
- **Structured Logging**: Logs all API requests and responses to `logs/trading_bot.log`.
- **Validation**: Robust input validation for symbols, quantities, and sides.

## Bonus Features Added
- **Stop-Market Order**: Support for `STOP_MARKET` order type in addition to `MARKET` and `LIMIT`.
- **Enhanced CLI UX**: Implemented professional terminal output using `Rich` for colorful status messages, tables, and better readability.


## Setup

1. **Clone the repository**:
   ```bash
   git clone <repo-url>
   cd TradingBot
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**:
   Create a `.env` file in the root directory (use `.env.example` as a template):
   ```env
   BINANCE_API_KEY=your_testnet_api_key
   BINANCE_API_SECRET=your_testnet_api_secret
   BINANCE_TESTNET=true
   ```

## Usage Examples

### 1. Check Connectivity
```bash
python main.py status
```

### 2. Place a Market BUY Order
```bash
python main.py market BTCUSDT BUY 0.001
```

### 3. Place a Limit SELL Order
```bash
python main.py limit BTCUSDT SELL 0.01 75000
```

### 4. Place a Stop-Market Order (Bonus)
```bash
python main.py stop-market BTCUSDT SELL 0.01 60000
```

## Screenshots

### 1. Market BUY Order
![Market BUY Order](screenshots/buy_order.png)

### 2. Limit SELL Order
![Limit SELL Order](screenshots/sell_order.png)

## Project Structure
- `bot/`: Core package containing logic.
  - `client.py`: Binance API client wrapper.
  - `orders.py`: Order placement logic.
  - `validators.py`: Input validation utilities.
  - `logging_config.py`: Logger setup.
  - `cli.py`: Typer-based CLI implementation.
- `main.py`: Entry point for the application.
- `logs/`: Directory for log files.

## Assumptions
- The bot is designed for **USDT-M Futures** only.
- Symbols must end with "USDT".
## Logs
All API requests, responses, and errors are automatically logged to the `logs/trading_bot.log` file. This file provides a detailed audit trail of all trading activities and is essential for troubleshooting and verification.

---
**Developed by geetasnhi jain | 05 Feb 2026**
