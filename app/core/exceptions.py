"""Custom application exceptions."""


class AppError(Exception):
    """Base class for all application-level errors."""


class NotFoundError(AppError):
    pass


class PermissionDeniedError(AppError):
    pass


class SubscriptionRequiredError(AppError):
    pass


class BillingError(AppError):
    pass
