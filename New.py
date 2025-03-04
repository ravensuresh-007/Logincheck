import configparser

Config = configparser.ConfigParser()
Config.read('config.ini')

# Get user configuration
source = Config.get('user', 'source')
client_name = Config.get(client_id, 'client_name')

# Extract API credentials
API_KEY_MarketData = Config.get(client_id, 'market_data_api_key')
API_SECRET_MarketData = Config.get(client_id, 'market_data_api_secret')
API_KEY_Interactive = Config.get(client_id, 'interactive_api_key')
API_SECRET_Interactive = Config.get(client_id, 'interactive_api_secret')
print(API_KEY_MarketData)
