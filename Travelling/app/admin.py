from django.contrib import admin
from .models import Contact,about,Route,BusDetails, Destination, Customer,Ticket_history,Payment,NewUser,Passenger

# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','subject','message','bus_name','origin','destination','bus_No','driver_phono']


@admin.register(about)
class PostAdmin(admin.ModelAdmin):
 list_display = ['bus_name','travels']

@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
     list_display = ['id', 'origin', 'destination_two', 'date']

@admin.register(BusDetails)
class BusDetailsAdmin(admin.ModelAdmin):
     list_display = ['id', 'source', 'destination_one', 'bus_name', 'vehicle_num', 'driver_no', 'arrival_time','start_time', 'price','nos','rem','bus_type']

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
     list_display = ['id', 'destination']

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
     list_display = ['id','name', 'age', 'gender', 'bus_name','no_tkt','price','source','destination','mobile_number','seatno']

@admin.register(Ticket_history)
class Ticket_historyAdmin(admin.ModelAdmin):
     list_display = ['name', 'bus_name',  'origin', 'destination','date', 'user']


@admin.register(NewUser)
class NewUserAdmin(admin.ModelAdmin):
     list_display=['user_id','username','first_name','last_name','mobile_number','email','is_staff','start_date']


admin.site.register(Payment)

@admin.register(Passenger)
class PassengerAdmin(admin.ModelAdmin):
     list_display=['Ticket_id','User_id','seatno','Date_of_journey','Bus_id','name','age','gender','Booking_id','Phone_number','source','destination','price','no_tkt','bus_name']