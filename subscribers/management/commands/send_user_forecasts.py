from django.conf import settings
from django.core.mail import send_mail
from django.core.management.base import BaseCommand

from core.models import Location
from subscribers.models import Subscriber
from subscribers.weather import fetch_forecast

dark_sky_msg = "<a href='https://darksky.net/poweredby/'>Powered by Dark Sky</a>"


def construct_email(forecast_dict):
    """
    Constructs dictionary to be passed off to send_email
    :param forecast_dict:
    :return: dict containing the subject and weekly summary to be send to the user based on their location
    and weather forecast
    """
    daily_forecast = forecast_dict['daily']
    summary = daily_forecast['daily']['summary']
    curr_forecast, tmrw_forecast = daily_forecast['data'][0], daily_forecast['data'][1]
    subject = determine_email_subject(curr_forecast, tmrw_forecast)

    return {
        'subject': subject,
        'daily_summary': summary
    }


def send_forecast_emails(subscribers, forecast_dict):
    email_dict = construct_email(forecast_dict)
    send_mail(
        subject=email_dict['subject'],
        message=f"{email_dict['daily_summary']}\nHope you're keeping it awesome!\n{dark_sky_msg}",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[sub['email'] for sub in subscribers]
    )


def determine_email_subject(curr_forecast, tmrw_forecast):
    """
    Determines if it's 'nice outside' depending on how today's weather forecast
    compares to what's predicted for tomorrow
    """
    temp_diff = tmrw_forecast['temperatureHigh'] - curr_forecast['temperatureHigh']
    # Is nice today
    if temp_diff < -5 or tmrw_forecast['precipProbability'] > 0.05:
        return "It's nice out! Enjoy a discount on us."
    # Nice today
    elif temp_diff > 5 or curr_forecast['precipProbability'] > 0.05:
        return "Not so nice out? That's okay, enjoy a discount on us"
    # Neutral
    else:
        return "Enjoy a discount on us"


class Command(BaseCommand):
    help = 'Sends weather to subscribers'

    def handle(self, *args, **options):
        # Get list of locations IDs for our subscribers
        user_location_ids = Subscriber.objects.values('location')
        for location in user_location_ids:
            loc_id = location['location']
            location = Location.objects.get(id=loc_id)
            subscribers = Subscriber.objects.filter(location_id=loc_id).values('email')
            loc_forecast_dict = fetch_forecast(location.latitude, location.longitude)
            send_forecast_emails(subscribers, loc_forecast_dict)
