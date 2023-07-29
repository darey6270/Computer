from django.db import models
from datetime import datetime


# from restserver.stockdata.models import stockdata

# Create your models here.

class stockdata(models.Model):
    stock = models.CharField(max_length=25,null=True, blank=True)
    source = models.CharField(max_length=255,null=True, blank=True)
    alpaca = models.CharField(max_length=255, null=True, blank=True)
    ig = models.CharField(max_length=255, null=True, blank=True)
    starttime = models.DateTimeField(default=datetime.now)
    endtime = models.DateTimeField(default=datetime.now)
    categoryId = models.IntegerField(default=1, null=True, blank=True)
    portfolioId = models.IntegerField(default=1, null=True, blank=True)
    length = models.FloatField(blank=True, null=True,default=5000)
    interval = models.FloatField(blank=True, null=True,default=5)
    qty = models.FloatField(blank=True, null=True,default=1)
    deviationfactor = models.FloatField(blank=True, null=True,default=0.7)
    telegram=models.CharField(max_length=255,default="999999999")
    whatsapp=models.CharField(max_length=255,default="999999999")
    email=models.CharField(max_length=255,default="abc@abc.com")

    
    class Meta:
        db_table = "stockdata"


class robotalpaca(models.Model):
    stock = models.CharField(max_length=25,null=True, blank=True)
    source = models.CharField(max_length=255,null=True, blank=True)
    alpaca = models.CharField(max_length=255, null=True, blank=True)
    starttime = models.DateTimeField(default=datetime.now)
    endtime = models.DateTimeField(default=datetime.now)
    categoryId = models.IntegerField(default=1, null=True, blank=True)
    portfolioId = models.IntegerField(default=1, null=True, blank=True)
    length = models.FloatField(blank=True, null=True,default=5000)
    interval = models.FloatField(blank=True, null=True,default=5)
    qty = models.FloatField(blank=True, null=True,default=1)
    deviationfactor = models.FloatField(blank=True, null=True,default=0.7)
    api_key=models.CharField(max_length=255)
    api_secret=models.CharField(max_length=255)
    api_endpoint=models.CharField(max_length=255)
    telegram=models.CharField(max_length=255,default="999999999")
    whatsapp=models.CharField(max_length=255,default="999999999")
    email=models.CharField(max_length=255,default="abc@abc.com")
    status = models.FloatField(blank=True, null=True,default=1)
    customerId = models.FloatField(blank=True, null=True,default=1)
    
    class Meta:
        db_table = "stockdata_robotalpaca"


class robotig(models.Model):
    stock = models.CharField(max_length=25,null=True, blank=True)
    source = models.CharField(max_length=255,null=True, blank=True)
    ig = models.CharField(max_length=255, null=True, blank=True)
    starttime = models.DateTimeField(default=datetime.now)
    endtime = models.DateTimeField(default=datetime.now)
    categoryId = models.IntegerField(default=1, null=True, blank=True)
    portfolioId = models.IntegerField(default=1, null=True, blank=True)
    length = models.FloatField(blank=True, null=True,default=5000)
    interval = models.FloatField(blank=True, null=True,default=5)
    qty = models.FloatField(blank=True, null=True,default=1)
    deviationfactor = models.FloatField(blank=True, null=True,default=0.7)
    username=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    api_key=models.CharField(max_length=255)
    acc_type=models.CharField(max_length=255)
    telegram=models.CharField(max_length=255,default="999999999")
    whatsapp=models.CharField(max_length=255,default="999999999")
    email=models.CharField(max_length=255,default="abc@abc.com")
    status = models.FloatField(blank=True, null=True,default=1)
    customerId = models.FloatField(blank=True, null=True,default=1)
    
    class Meta:
        db_table = "stockdata_robotig"


class robotaliceblue(models.Model):
    stock = models.CharField(max_length=25,null=True, blank=True)
    source = models.CharField(max_length=255,null=True, blank=True)
    aliceblue = models.CharField(max_length=255, null=True, blank=True)
    starttime = models.DateTimeField(default=datetime.now)
    endtime = models.DateTimeField(default=datetime.now)
    categoryId = models.IntegerField(default=1, null=True, blank=True)
    portfolioId = models.IntegerField(default=1, null=True, blank=True)
    length = models.FloatField(blank=True, null=True,default=5000)
    interval = models.FloatField(blank=True, null=True,default=5)
    qty = models.FloatField(blank=True, null=True,default=1)
    deviationfactor = models.FloatField(blank=True, null=True,default=0.7)
    username=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    api_key=models.CharField(max_length=255)
    secret_key=models.CharField(max_length=255)
    twofa=models.CharField(max_length=10)
    telegram=models.CharField(max_length=255,default="999999999")
    whatsapp=models.CharField(max_length=255,default="999999999")
    email=models.CharField(max_length=255,default="abc@abc.com")
    status = models.FloatField(blank=True, null=True,default=1)
    customerId = models.FloatField(blank=True, null=True,default=1)
    
    class Meta:
        db_table = "stockdata_robotaliceblue"



class alpacatrans(models.Model):
    customer_id=models.CharField(max_length=255)
    transaction_id=models.CharField(max_length=255)
    account_number=models.CharField(max_length=255)
    status=models.CharField(max_length=255)
    crypto_status=models.CharField(max_length=255)
    currency=models.CharField(max_length=255)
    buying_power=models.CharField(max_length=255)
    regt_buying_power=models.CharField(max_length=255)
    daytrading_buying_power= models.CharField(max_length=255)
    non_marginable_buying_power=models.CharField(max_length=255)
    cash=models.CharField(max_length=255)
    accrued_fees=models.CharField(max_length=255)
    pending_transfer_out=models.CharField(max_length=255)
    pending_transfer_in= models.CharField(max_length=255)
    portfolio_value=models.CharField(max_length=255)
    pattern_day_trader=models.CharField(max_length=255)
    trading_blocked=models.CharField(max_length=255)
    transfers_blocked=models.CharField(max_length=255)
    account_blocked=models.CharField(max_length=255)
    created_at= models.CharField(max_length=255)
    trade_suspended_by_user=models.CharField(max_length=255)
    multiplier=models.CharField(max_length=255)
    shorting_enabled=models.CharField(max_length=255)
    equity=models.CharField(max_length=255)
    last_equity=models.CharField(max_length=255)
    long_market_value=models.CharField(max_length=255)
    short_market_value= models.CharField(max_length=255)
    initial_margin=models.CharField(max_length=255)
    maintenance_margin= models.CharField(max_length=255)
    last_maintenance_margin= models.CharField(max_length=255)
    sma=models.CharField(max_length=255)
    daytrade_count=models.CharField(max_length=255)
    
    class Meta:
        db_table = "stockdata_alpacatransaction"



class robotdemo(models.Model):
    stock = models.CharField(max_length=25,null=True, blank=True)
    source = models.CharField(max_length=255,null=True, blank=True)
    alpaca = models.CharField(max_length=255, null=True, blank=True)
    starttime = models.DateTimeField(default=datetime.now)
    endtime = models.DateTimeField(default=datetime.now)
    categoryId = models.IntegerField(default=1, null=True, blank=True)
    portfolioId = models.IntegerField(default=1, null=True, blank=True)
    length = models.FloatField(blank=True, null=True,default=5000)
    interval = models.FloatField(blank=True, null=True,default=5)
    qty = models.FloatField(blank=True, null=True,default=1)
    deviationfactor = models.FloatField(blank=True, null=True,default=0.7)
    api_key=models.CharField(max_length=255)
    api_secret=models.CharField(max_length=255)
    api_endpoint=models.CharField(max_length=255)
    telegram=models.CharField(max_length=255,default="999999999")
    whatsapp=models.CharField(max_length=255,default="999999999")
    email=models.CharField(max_length=255,default="abc@abc.com")
    status = models.FloatField(blank=True, null=True,default=1)
    customerId = models.FloatField(blank=True, null=True,default=1)
    
    class Meta:
        db_table = "stockdata_robotdemo"




class signalsrobot(models.Model):
    stock = models.CharField(max_length=25,null=True, blank=True)
    source = models.CharField(max_length=255,null=True, blank=True)
    alpaca = models.CharField(max_length=255, null=True, blank=True)
    starttime = models.DateTimeField(default=datetime.now)
    endtime = models.DateTimeField(default=datetime.now)
    categoryId = models.IntegerField(default=1, null=True, blank=True)
    portfolioId = models.IntegerField(default=1, null=True, blank=True)
    length = models.FloatField(blank=True, null=True,default=5000)
    interval = models.FloatField(blank=True, null=True,default=5)
    qty = models.FloatField(blank=True, null=True,default=1)
    deviationfactor = models.FloatField(blank=True, null=True,default=0.7)
    telegram=models.CharField(max_length=255,default="999999999")
    whatsapp=models.CharField(max_length=255,default="999999999")
    email=models.CharField(max_length=255,default="abc@abc.com")
    status = models.FloatField(blank=True, null=True,default=1)
    customerId = models.FloatField(blank=True, null=True,default=1)
    
    class Meta:
        db_table = "stockdata_signalsrobot"



