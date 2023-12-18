import sentry_sdk

sentry_sdk.init(
    dsn="https://ef07de3146c9d4b7248734c46fff5e11@o4506410812375040.ingest.sentry.io/4506410861461504",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)