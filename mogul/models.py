from django.db import models

# Create your models here.

"""
User

+   email
    fname
    mname
    lname
    age 
    gender
    mobile
    city
    seq-qus
    seq-ans
"""
class User(models.Model):
    email_id  = models.EmailField(primary_key=True)
    fname = models.CharField(max_length=64)
    mname = models.CharField(max_length=64)
    lname = models.CharField(max_length=64)
    gender = models.CharField(max_length=64)
    mobile  = models.CharField(max_length=10)
    seq_qus = models.CharField(max_length=64)
    seq_ans = models.CharField(max_length=64)
    age = models.IntegerField()
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=64)

    def __str__(self):
        return " Inserted User with email "+ self.email_id 

    class Meta:
        db_table = "user"

"""
Train
+   train_id
    train_name
    train_type
    sc1 sc2 sc3 
    fc1 fc2 fc3
    avail_days
    source_id
    dest_id

"""
class Train(models.Model):
    train_id = models.IntegerField(primary_key=True)
    train_name = models.CharField(max_length=64)
    train_type = models.CharField(max_length=64)
    sc1 = models.IntegerField()
    sc2 = models.IntegerField()
    sc3 = models.IntegerField()
    fc1 = models.IntegerField()
    fc2 = models.IntegerField()
    fc3 = models.IntegerField()
    avail_days = models.IntegerField()
    source_id  = models.IntegerField()
    dest_id = models.IntegerField()

    def __str__(self):
        return str(self.train_id) + " | " 

    class Meta:
        db_table = "train"
"""
Route:
+	train_id
+   stop_numbers
    source_dist
	arrival_time
	depart_time
"""
class Route(models.Model):
    train= models.ForeignKey(Train,on_delete=models.CASCADE)
    stop_numbers_id = models.IntegerField(primary_key=True)
    source_dist = models.IntegerField()
    arrival_time = models.DateTimeField()
    depart_time = models.DateTimeField()

    def __str__(self):
        return str(self.train_id) + " | " 

    class Meta:
        db_table = "route"


"""
Station
+   station_id
    station_name
"""

class Station(models.Model):
    station_id = models.IntegerField(primary_key=True)
    station_name = models.CharField(max_length=64)

    def __str__(self):
        return "Station Inserted Succesfully "

    class Meta:
        db_table = "station"



"""
consist_of
+   station_id
+   train_id
+   stop_number
"""

class consist_of(models.Model):
    station = models.ForeignKey(Station,on_delete=models.CASCADE)
    train= models.ForeignKey(Route,on_delete=models.CASCADE,related_name='tid')
    stop_numbers = models.ForeignKey(Route,on_delete=models.CASCADE,related_name='sno')

    def __str__(self):
        return " Inserted Data. "

    class Meta:
        db_table = "consist_of"


"""
 Train_Status
 +  train_id
 +  avail_date
    bs1 bs2 bs3
    ws1 ws2 ws3
    as1 as2 as3
"""
class Train_Status(models.Model):
    train= models.ForeignKey(Train,on_delete=models.CASCADE)
    avail_date_id = models.DateTimeField()
    bs1 = models.IntegerField()
    bs2 = models.IntegerField()
    bs3 = models.IntegerField()
    as1 = models.IntegerField()
    as2 = models.IntegerField()
    as3 = models.IntegerField()
    ws1 = models.IntegerField()
    ws2 = models.IntegerField()
    ws3 = models.IntegerField()
    

    def __str__(self):
        return "Inserted"

    class Meta:
        unique_together = (("train", "avail_date_id"),)
        db_table = "train_status"





"""
Passenger
+   pnr
    name
    gender
    age
    seat_no
    class
    fare
    source_id
    dest_id
"""

class Passenger(models.Model):
    PNR_id = models.CharField(primary_key=True,max_length=64,default='1')
    name  = models.CharField(max_length=64)
    gender  = models.CharField(max_length=64)
    age = models.IntegerField()
    seat_no = models.IntegerField()
    Class_type = models.CharField(max_length=64,default='AC-FIRST')
    fare = models.IntegerField()
    source= models.ForeignKey(Train,on_delete=models.CASCADE,related_name='source')
    dest = models.ForeignKey(Train,on_delete=models.CASCADE,related_name='dest') 


    def __str__(self):
        return self.name

    class Meta:
        db_table = "passenger"


"""
Reservation
+   email_id
+   train_id
+   pnr
+   avail_date
    status
    date
"""

class Reservation(models.Model):
    email = models.ForeignKey(User,on_delete=models.CASCADE)
    train= models.ForeignKey(Train,on_delete=models.CASCADE)
    PNR = models.ForeignKey(Passenger,on_delete=models.CASCADE)
    avail_date = models.ForeignKey(Train_Status,on_delete=models.CASCADE)
    status = models.CharField(max_length=64)
    date = models.DateField()


    def __str__(self):
        i=1
        return  "Reserved to PNR no: "+str(self.PNR)

    class Meta:
        db_table = "reservation"

