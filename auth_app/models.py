from django.db import models
from shopify_auth.models import AbstractShopUser

class AuthAppShopUser(AbstractShopUser):
    pass




countries = (
    ('Palestine','Palestine'),
    ('Japan','Japan'),
    ('Iceland','Iceland'),
    ('Singapore','Singapore'),
    
)

# Create your models here.
class Settings(models.Model):
    user=models.ForeignKey(AuthAppShopUser,related_name='usersetting',on_delete=models.CASCADE,null=True)
    vpnconfig=models.BooleanField(default=False)
    rdpcofig=models.BooleanField(default=False)
    proxyconfig=models.BooleanField(default=False)
    blockedmsgtitle=models.CharField(max_length=200)
    blockedmsgbody=models.TextField(max_length=200)
    allowedcountries=models.CharField(max_length=15 , choices=countries)
    blockedcountries=models.CharField(max_length=15 , choices=countries)

class AllVisites(models.Model):
    user=models.ForeignKey(AuthAppShopUser,related_name='uservisites',on_delete=models.CASCADE,null=True)
    IPadress=models.CharField(max_length=39)
    county=models.CharField(max_length=15)
    time=models.CharField(max_length=20)
    browser=models.CharField(max_length=20)
    device=models.CharField(max_length=20)
    bot=models.BooleanField(default=False)
    hosting=models.CharField(max_length=20)
    providertype=models.CharField(max_length=20)
    isblocked=models.BooleanField(default=False)
    os=models.CharField(max_length=20)


class Iplist (models.Model):
    IPadress=models.CharField(max_length=39)
    county=models.CharField(max_length=15)
    countycode=models.CharField(max_length=15)
    city=models.CharField(max_length=15)
    providertype=models.CharField(max_length=30)
    ishosting=models.CharField(max_length=30)
    isisp=models.CharField(max_length=30)
    isvpn=models.CharField(max_length=30)
    isproxy=models.CharField(max_length=30)
    vpndomain=models.CharField(max_length=30)


