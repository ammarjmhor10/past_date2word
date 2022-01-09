from past_date2word import past_date2word
from datetime import datetime, timedelta


def test_second_en():
    time = datetime.now() - timedelta(seconds=1)
    assert past_date2word(time) == "1 second ago"
    time = datetime.now() - timedelta(seconds=23)
    assert past_date2word(time) == "23 seconds ago"


def test_minute_en():
    time = datetime.now() - timedelta(minutes=1)
    assert past_date2word(time) == "1 minute ago"
    time = datetime.now() - timedelta(minutes=1, seconds=1)
    assert past_date2word(time) == "1 minute and 1 second ago"
    time = datetime.now() - timedelta(minutes=13)
    assert past_date2word(time) == "13 minutes ago"
    time = datetime.now() - timedelta(minutes=9, seconds=34)
    assert past_date2word(time) == "9 minutes and 34 seconds ago"


def test_hour_en():
    time = datetime.now() - timedelta(hours=1)
    assert past_date2word(time) == "1 hour ago"
    time = datetime.now() - timedelta(hours=1, minutes=1)
    assert past_date2word(time) == "1 hour and 1 minute ago"
    time = datetime.now() - timedelta(hours=22)
    assert past_date2word(time) == "22 hours ago"
    time = datetime.now() - timedelta(hours=12, minutes=44)
    assert past_date2word(time) == "12 hours and 44 minutes ago"


def test_day_en():
    time = datetime.now() - timedelta(days=1)
    assert past_date2word(time) == "1 day ago"
    time = datetime.now() - timedelta(days=1, hours=1)
    assert past_date2word(time) == "1 day and 1 hour ago"
    time = datetime.now() - timedelta(days=6)
    assert past_date2word(time) == "6 days ago"
    time = datetime.now() - timedelta(days=5, hours=15)
    assert past_date2word(time) == "5 days and 15 hours ago"


def test_week_en():
    time = datetime.now() - timedelta(weeks=1)
    assert past_date2word(time) == "1 week ago"
    time = datetime.now() - timedelta(weeks=1, days=1)
    assert past_date2word(time) == "1 week and 1 day ago"
    time = datetime.now() - timedelta(weeks=3)
    assert past_date2word(time) == "3 weeks ago"
    time = datetime.now() - timedelta(weeks=2, days=4)
    assert past_date2word(time) == "2 weeks and 4 days ago"


def test_month_en():
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


def test_year_en():
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

def test_second_ar():
    time = datetime.now() - timedelta(seconds=1)
    assert past_date2word(time) == "منذ ثانية"
    time = datetime.now() - timedelta(seconds=2)
    assert past_date2word(time) == "منذ ثانيتين"
    time = datetime.now() - timedelta(seconds=5)
    assert past_date2word(time) == "منذ 5 ثواني"
    time = datetime.now() - timedelta(seconds=13)
    assert past_date2word(time) == "منذ 13 ثانية"


def test_minute_ar():
    time = datetime.now() - timedelta(minutes=1)
    assert past_date2word(time) == "منذ دقيقة"
    time = datetime.now() - timedelta(minutes=1, seconds=1)
    assert past_date2word(time) == "منذ دقيقة و ثانية"
    time = datetime.now() - timedelta(minutes=2, seconds=2)
    assert past_date2word(time) == "منذ دقيقتين و ثانيتين"
    time = datetime.now() - timedelta(minutes=5, seconds=5)
    assert past_date2word(time) == "منذ 5 دقائق و 5 ثواني"
    time = datetime.now() - timedelta(minutes=13, seconds=13)
    assert past_date2word(time) == "منذ 13 دقيقة و 13 ثانية"


def test_hour_ar():
    
    time = datetime.now() - timedelta(hours=1)
    assert past_date2word(time) == "منذ ساعة"
    time = datetime.now() - timedelta(hours=1, minutes=1)
    assert past_date2word(time) == "منذ ساعة و دقيقة"
    time = datetime.now() - timedelta(hours=2,minutes=2)
    assert past_date2word(time) == "منذ ساعتين و دقيقتين"
    time = datetime.now() - timedelta(hours=5, minutes=5)
    assert past_date2word(time) == "منذ خمس ساعات و 5 دقائق"
    time = datetime.now() - timedelta(hours=13, minutes=13)
    assert past_date2word(time) == "منذ 13 ساعة و 13 دقيقة"

def test_day_ar():
    time = datetime.now() - timedelta(days=1)
    assert past_date2word(time) == "منذ يوم"
    time = datetime.now() - timedelta(days=1, hours=1)
    assert past_date2word(time) == "منذ يوم وساعة"
    time = datetime.now() - timedelta(days=2,hours=2)
    assert past_date2word(time) == "منذ يومين و ساعتين"
    time = datetime.now() - timedelta(days=5, hours=5)
    assert past_date2word(time) == "منذ5 ايام   و 5 ساعات "
    time = datetime.now() - timedelta(days=15, hours=15)
    assert past_date2word(time) == "منذ 15 يوم  و 15 ساعة"


def test_week_ar():
    
    time = datetime.now() - timedelta(weeks=1)
    assert past_date2word(time) == "منذ اسبوع"
    time = datetime.now() - timedelta(weeks=1, days=1)
    assert past_date2word(time) == "منذ اسبوع و يوم"
    time = datetime.now() - timedelta(weeks=2,days=2)
    assert past_date2word(time) == "منذ اسبوعين و يومين"
    time = datetime.now() - timedelta(weeks=4, days=4)
    assert past_date2word(time) == "منذ 4 اسابيع و 4 ايام"
    time = datetime.now() - timedelta(weeks=15 ,days=15)
    assert past_date2word(time) == "منذ 15 اسبوع و 15 يوم"

def test_month_ar():
    one_month_to_week = 4 * 1

    time = datetime.now() - timedelta(weeks=one_month_to_week)
    assert past_date2word(time) == "منذ شهر"
    time = datetime.now() - timedelta(weeks=one_month_to_week + 1)
    assert past_date2word(time) == "منذ شهر و اسبوع"
    time = datetime.now() - timedelta(weeks=one_month_to_week * 2)
    assert past_date2word(time) == "منذ شهرين"
    time = datetime.now() - timedelta(weeks=(one_month_to_week * 3) + 2)
    assert past_date2word(time) == "منذ 3 اشهر و اسبوعين"
    time = datetime.now() - timedelta(weeks=(one_month_to_week * 15) + 15)
    assert past_date2word(time) == "منذ 15 شهر و 15 اسبوع"

def test_year_ar():
    # 12 month == 1 year
    # 4 weeks == 1 month
    one_month_to_week = 4 * 1
    one_year_to_week = one_month_to_week * 12

    time = datetime.now() - timedelta(weeks=one_year_to_week)
    assert past_date2word(time) == "منذ سنة"
    time = datetime.now() - timedelta(weeks=(one_year_to_week) +(one_month_to_week * 1))
    assert past_date2word(time) == "منذ سنة و شهر"
    time = datetime.now() - timedelta(weeks=(one_year_to_week * 2) +(one_month_to_week * 2))
    assert past_date2word(time) == " منذ سنتين و شهرين"
    time = datetime.now() - timedelta(weeks=(one_year_to_week * 5)+(one_month_to_week * 5))
    assert past_date2word(time) == "منذ 5 سنوات و خمس شهور"
    time = datetime.now() - timedelta(
        weeks=(one_year_to_week * 12) + (one_month_to_week * 5)
    )
    assert past_date2word(time) == "منذ 12 سنة و5 شهور"