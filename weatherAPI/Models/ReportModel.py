from django.db import models

class ReportType(models.Model):
    report_type_id = models.AutoField(primary_key=True)
    report_type = models.TextField()

    class Meta:
        name = "report_type"

class Region(models.Model):
    region_id = models.AutoField(primary_key=True)
    region = models.TextField()

    class Meta:
        name = "region"

class Gender(models.Model):
    gender_id = models.AutoField(primary_key=True)
    gender_code = models.IntegerField()
    gender = models.CharField(max_length=20)

    class Meta:
        name = "gender"

class ReportDataMining(models.Model):
    data_mining_id = models.AutoField(primary_key=True)
    data_mining_year_num = models.IntegerField()
    data_mining_year = models.IntegerField()
    data_mining_quarter = models.CharField(max_length=20)
    data_mining_half_year = models.CharField(max_length=20)

    class Meta:
        name = "report_data_mining"

class InitialReport(models.Model):
    initial_report_id=models.AutoField(primary_key=True)
    initial_report_year_num = models.IntegerField()
    initial_report_year = models.IntegerField()
    initial_report_month = models.CharField(max_length=20)
    initial_report_quarter = models.CharField(max_length=20)
    initial_report_half_year = models.CharField(max_length=20)

    class Meta:
        name = "initial_report"

class AgeGroup(models.Model):
    age_group_id=models.AutoField(primary_key=True)
    age_group_code = models.IntegerField()
    age_group = models.CharField(max_length=20)
    age_group_9 = models.CharField(max_length=20)
    age_group_4 = models.CharField(max_length=20)
    age_group_3 = models.CharField(max_length=20)

    class Meta:
        name = "age_group"

class UserReport(models.Model):
    report_id = models.AutoField(primary_key=True)
    source_report_id = models.IntegerField(Required=True)
    data_enter_date = models.DateTimeField()
    first_dated_database = models.DateTimeField()
    report_type_id = models.ForeignKey(ReportType, on_delete="PROTECT")
    region = models.ForeignKey(Region, on_delete="PROTECT")
    data_mining_id = models.ForeignKey(ReportDataMining, on_delete="PROTECT")
    initial_report_id = models.ForeignKey(ReportDataMining, on_delete="PROTECT")
    gender_id = models.ForeignKey(Gender, on_delete="PROTECT")
    age_group_id = models.ForeignKey(AgeGroup, on_delete="PROTECT")
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
        name="user_report"
