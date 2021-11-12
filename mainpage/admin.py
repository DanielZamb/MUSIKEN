from django.contrib import admin
from .models import (User,
                     Publication,
                     Review,
                     Rating,
                     ContentImage,
                     ProfileImage,
                     Content,
                     TextMeasure,
                     ScaleMeasure,
                     PercentageMeasure)
admin.site.register(User)
admin.site.register(Publication)
admin.site.register(Review)
admin.site.register(Rating)
admin.site.register(Content)
admin.site.register(ContentImage)
admin.site.register(ProfileImage)
admin.site.register(TextMeasure)
admin.site.register(ScaleMeasure)
admin.site.register(PercentageMeasure)
# Register your models here.
