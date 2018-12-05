# Installation

`pip install git+https://github.com/aymericderbois/py-mattermost-webhooks-log-handler.git@master`

# Configuration

## Django

### For WARNING message
If you want to log on mattermost, you have to add an handler.
For example, to send warning message

```python
LOGGING = {
    'version': 1,
    'formatters': {
        'simple': {
            'format': '[%(asctime)s][%(levelname)s] %(message)s'
        },
    },
    'handlers': {
        'mattermost': {
            'level': 'WARTNING',
            'class': 'mattermost_handler.MattermostIncomeWebhookHandler',
            'formatter': 'simple',
            'url': 'https://mattermost.example.com/hooks/4m5sdub8sfg5s488uyt1Q97ei39fa'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['mattermost'],
            'propagate': True,
            'level': 'INFO'
        }
    }
}
```


### For specific message

You also can create a specific logger for mattermost
```python
LOGGING = {
    'version': 1,
    'formatters': {
        'simple': {
            'format': '[%(asctime)s][%(levelname)s] %(message)s'
        },
    },
    'handlers': {
        'mattermost': {
            'level': 'INFO',
            'class': 'mattermost_handler.MattermostIncomeWebhookHandler',
            'formatter': 'simple',
            'url': 'https://mattermost.example.com/hooks/4m5sdub8sfg5s488uyt1Q97ei39fa'
        }
    },
    'loggers': {
        'mattermost': {
            'handlers': ['mattermost'],
            'propagate': True,
            'level': 'INFO'
        }
    }
}
```

And in your code

```
logger = logging.getLogger('mattermost')

logger.info('this message will be sent to mattermost')
```

