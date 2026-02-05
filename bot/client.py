import os
from binance.client import Client
from loguru import logger
from dotenv import load_dotenv

load_dotenv()

class BinanceClientWrapper:
    def __init__(self):
        self.api_key = os.getenv("BINANCE_API_KEY")
        self.api_secret = os.getenv("BINANCE_API_SECRET")
        self.testnet = os.getenv("BINANCE_TESTNET", "true").lower() == "true"
        
        if not self.api_key or not self.api_secret:
            logger.error("BINANCE_API_KEY or BINANCE_API_SECRET not found in environment variables.")
            raise ValueError("API Credentials missing.")

        # We initialize without the 'testnet' flag to prevent the library from 
        # reaching out to 'testnet.binance.vision' (Spot Testnet) by default.
        # Instead, we manually set the Futures Testnet endpoint.
        requests_params = {'timeout': 30}
        self.client = Client(
            self.api_key, 
            self.api_secret, 
            requests_params=requests_params
        )
        
        if self.testnet:
            # Manually point to Futures Testnet
            self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'
            logger.info("Configured for Binance Futures TESTNET (Manual Override)")
        else:
            logger.info("Connected to Binance Futures MAINNET")

    def get_client(self):
        return self.client

    def ping(self):
        try:
            self.client.futures_ping()
            logger.info("Successfully pinged Binance Futures API")
            return True
        except Exception as e:
            logger.error(f"Failed to ping Binance Futures API: {e}")
            return False
