import logging
from notifiers import notify


class Notifier:
    """
    Library for using different notification services.

    All keywords take keyword arguments (**kwargs) to allow giving
    additional arguments for the notifications.
    """

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def notify_pushover(
        self, message: str = None, user: str = None, token: str = None, **kwargs: dict
    ) -> bool:
        """Notify using Pushover service

        Arguments:
            message: notification message
            user: target user for the notification
            token: service token
            kwargs: other arguments to pass to notify method

        Returns:
            True is notification was success, False if not
        """
        response = notify("pushover", message=message, user=user, token=token, **kwargs)
        return self._handle_response(response)

    def notify_slack(
        self,
        message: str = None,
        channel: str = None,
        webhook_url: str = None,
        **kwargs: dict,
    ) -> bool:
        """Notify using Slack service

        Arguments:
            message: notification message
            channel: target channel for the notification
            webhook_url: Slack webhook url
            kwargs: other arguments to pass to notify method

        Returns:
            True is notification was success, False if not
        """
        response = notify(
            "slack",
            message=message,
            webhook_url=webhook_url,
            channel=channel,
            **kwargs,
        )
        return self._handle_response(response)

    def notify_telegram(
        self,
        message: str = None,
        chat_id: str = None,
        token: str = None,
        **kwargs: dict,
    ) -> bool:
        """Notify using Telegram service

        Arguments:
            message: notification message
            chat_id: target chat id for the notification
            token: service token
            kwargs: other arguments to pass to notify method

        Returns:
            True is notification was success, False if not
        """
        response = notify(
            "telegram", message=message, chat_id=chat_id, token=token, **kwargs
        )
        return self._handle_response(response)

    def notify_gmail(
        self,
        message: str = None,
        to: str = None,
        username: str = None,
        password: str = None,
        **kwargs: dict,
    ) -> bool:
        """Notify using Gmail service

        Arguments:
            message: notification message
            to: target of email message
            username: GMail service username
            password: GMail service password
            kwargs: other arguments to pass to notify method

        Returns:
            True is notification was success, False if not
        """
        response = notify(
            "gmail",
            message=message,
            to=to,
            username=username,
            password=password,
            **kwargs,
        )
        return self._handle_response(response)

    def notify_email(
        self,
        message: str = None,
        to: str = None,
        username: str = None,
        password: str = None,
        **kwargs: dict,
    ) -> bool:
        """Notify using email service

        Arguments:
            message: notification message
            to: target of email message
            username: email service username
            password: email service password
            kwargs: other arguments to pass to notify method

        Returns:
            True is notification was success, False if not
        """
        response = notify(
            "email",
            message=message,
            to=to,
            username=username,
            password=password,
            **kwargs,
        )
        return self._handle_response(response)

    def notify_twilio(
        self,
        message: str = None,
        number_from: str = None,
        number_to: str = None,
        account_sid: str = None,
        token: str = None,
        **kwargs: dict,
    ) -> bool:
        """Notify using Twilio service

        Arguments:
            message: notification message
            number_from: number where the message comes from
            number_to: number where the messages goes to
            account_sid: Twilio account SID
            token: Twilio account token
            kwargs: other arguments to pass to notify method

        Returns:
            True is notification was success, False if not
        """
        response = notify(
            "twilio",
            message=message,
            from_=number_from,
            to=number_to,
            account_sid=account_sid,
            auth_token=token,
            **kwargs,
        )
        return self._handle_response(response)

    def _handle_response(self, response):
        if response.status == "Success":
            self.logger.info("Notify %s resulted in Success", response.provider)
            return True
        else:
            self.logger.error("Notify errors: %s", response.errors)
            return False