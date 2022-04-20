from django.db import models

class ReportType(models.Model):
    report_type_id = models.AutoField(primary_key=True)
    report_type = models.TextField()

    class Meta:
        db_table = "report_type"

class Region(models.Model):
    region_id = models.AutoField(primary_key=True)
    region = models.TextField()

    class Meta:
        db_table = "region"

class Gender(models.Model):
    gender_id = models.AutoField(primary_key=True)
    gender_code = models.IntegerField()
    gender = models.CharField(max_length=20)
    
    class Meta:
        db_table = "gender"

class ReportDataMining(models.Model):
    data_mining_id = models.AutoField(primary_key=True)
    data_mining_year_num = models.IntegerField()
    data_mining_year = models.IntegerField()
    data_mining_quarter = models.CharField(max_length=20)
    data_mining_half_year = models.CharField(max_length=20)

    class Meta:
        db_table = "report_data_minining"

class InitialReport(models.Model):
    initial_report_id=models.AutoField(primary_key=True)
    initial_report_year_num = models.IntegerField()
    initial_report_year = models.IntegerField()
    initial_report_month = models.CharField(max_length=20)
    initial_report_quarter = models.CharField(max_length=20)
    initial_report_half_year = models.CharField(max_length=20)

    class Meta:
        db_table = "initial_report"

class AgeGroup(models.Model):
    age_group_id=models.AutoField(primary_key=True)
    age_group_code = models.IntegerField()
    age_group = models.CharField(max_length=20)
    age_group_9 = models.CharField(max_length=20)
    age_group_4 = models.CharField(max_length=20)
    age_group_3 = models.CharField(max_length=20)

    class Meta:
        db_table = "age_group"

class UserReport(models.Model):
    report_id = models.AutoField(primary_key=True)
    source_report_id = models.IntegerField()
    data_enter_date = models.DateTimeField()
    first_dated_database = models.DateTimeField()
    report_type_id = models.ForeignKey(ReportType, on_delete=models.PROTECT)
    region = models.ForeignKey(Region, on_delete=models.PROTECT)
    data_mining_id = models.ForeignKey(ReportDataMining, on_delete=models.PROTECT)
    initial_report_id = models.ForeignKey(InitialReport, on_delete=models.PROTECT)
    gender_id = models.ForeignKey(Gender, on_delete=models.PROTECT)
    age_group_id = models.ForeignKey(AgeGroup, on_delete=models.PROTECT)
    standard_strata = models.CharField(max_length=20)
    num_total_drug = models.IntegerField()
    num_con_drug = models.IntegerField()
    num_total_pt = models.IntegerField()
    data_load_quarter = models.CharField(max_length=20)
    flag_dup = models.BooleanField()
    report_id_for_dupgroup = models.IntegerField()
    num_rpts_in_dupgroup = models.IntegerField()
    fda_case_id = models.IntegerField()

    class Meta:
        db_table = "user_report"


