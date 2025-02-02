from past_date2word import past_date2word
from datetime import datetime, timedelta


def test_second():
    time = datetime.now() - timedelta(seconds=1)
    assert past_date2word(time) == "1 second ago"
    time = datetime.now() - timedelta(seconds=23)
    assert past_date2word(time) == "23 seconds ago"


def test_minute():
    time = datetime.now() - timedelta(minutes=1)
    assert past_date2word(time) == "1 minute ago"
    time = datetime.now() - timedelta(minutes=1, seconds=1)
    assert past_date2word(time) == "1 minute and 1 second ago"
    time = datetime.now() - timedelta(minutes=13)
    assert past_date2word(time) == "13 minutes ago"
    time = datetime.now() - timedelta(minutes=9, seconds=34)
    assert past_date2word(time) == "9 minutes and 34 seconds ago"


def test_hour():
    time = datetime.now() - timedelta(hours=1)
    assert past_date2word(time) == "1 hour ago"
    time = datetime.now() - timedelta(hours=1, minutes=1)
    assert past_date2word(time) == "1 hour and 1 minute ago"
    time = datetime.now() - timedelta(hours=22)
    assert past_date2word(time) == "22 hours ago"
    time = datetime.now() - timedelta(hours=12, minutes=44)
    assert past_date2word(time) == "12 hours and 44 minutes ago"


def test_day():
    time = datetime.now() - timedelta(days=1)
    assert past_date2word(time) == "1 day ago"
    time = datetime.now() - timedelta(days=1, hours=1)
    assert past_date2word(time) == "1 day and 1 hour ago"
    time = datetime.now() - timedelta(days=6)
    assert past_date2word(time) == "6 days ago"
    time = datetime.now() - timedelta(days=5, hours=15)
    assert past_date2word(time) == "5 days and 15 hours ago"


def test_week():
    time = datetime.now() - timedelta(weeks=1)
    assert past_date2word(time) == "1 week ago"
    time = datetime.now() - timedelta(weeks=1, days=1)
    assert past_date2word(time) == "1 week and 1 day ago"
    time = datetime.now() - timedelta(weeks=3)
    assert past_date2word(time) == "3 weeks ago"
    time = datetime.now() - timedelta(weeks=2, days=4)
    assert past_date2word(time) == "2 weeks and 4 days ago"


def test_month():
    # 4 weeks == 1 month
    one_month_to_week = 4 * 1

    time = datetime.now() - timedelta(weeks=one_month_to_week)
    assert past_date2word(time) == "1 month ago"
    time = datetime.now() - timedelta(weeks=one_month_to_week + 1)
    assert past_date2word(time) == "1 month and 1 week ago"
    time = datetime.now() - timedelta(weeks=one_month_to_week * 2)
    assert past_date2word(time) == "2 months ago"
    time = datetime.now() - timedelta(weeks=(one_month_to_week * 3) + 2)
    assert past_date2word(time) == "3 months and 2 weeks ago"


def test_hour():
    # 12 month == 1 year
    # 4 weeks == 1 month
    one_month_to_week = 4 * 1
    one_year_to_week = one_month_to_week * 12

    time = datetime.now() - timedelta(weeks=one_year_to_week)
    assert past_date2word(time) == "1 year ago"
    time = datetime.now() - timedelta(weeks=one_year_to_week + one_month_to_week)
    assert past_date2word(time) == "1 year and 1 month ago"
    time = datetime.now() - timedelta(weeks=one_year_to_week * 4)
    assert past_date2word(time) == "4 years ago"
    time = datetime.now() - timedelta(
        weeks=(one_year_to_week * 12) + (one_month_to_week * 5)
    )
    assert past_date2word(time) == "12 years and 5 months ago"
