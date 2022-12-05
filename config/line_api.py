import config

__config = config.Config('line_api')

CHANNEL_SECRET=__config.get('channel_secret')

CHANNEL_ACCESS_TOKEN=__config.get('channel_access_token')

BASIC_ID=__config.get('basic_id')