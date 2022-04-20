from datetime import date
from rest_framework import serializers
from .models import UserReport, Region

class RegionSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = "__all__"

class UserReportSerialzier(serializers.ModelSerializer):
    region=RegionSerialzier(read_only=True,many=True)
    class Meta:
        model = UserReport
        fields = "__all__"

# class UserReportSerializer(serializers.Serializer):
#     source_report_id = serializers.IntegerField()
#     age_group_code = serializers.IntegerField()
#     age_group = serializers.CharField(max_length=20)
#     gender_code = serializers.IntegerField()
#     data_enter_date = serializers.DateTimeField()
#     first_dated_database = serializers.DateTimeField()
#     report_type = serializers.TextField()
#     region = serializers.CharField(max_length=20)
#     gender = serializers.CharField(max_length=20)
#     age_group_9 = serializers.CharField(max_length=20)
#     age_group_4 = serializers.CharField(max_length=20)
#     data_mining_year_num = serializers.IntegerField()
#     data_mining_year = serializers.IntegerField()
#     data_mining_quarter = serializers.CharField(max_length=20)
#     data_mining_half_year = serializers.CharField(max_length=20)
#     initial_report_year_num = serializers.IntegerField()
#     initial_report_year = serializers.IntegerField()
#     initial_report_month = serializers.CharField(max_length=20)
#     initial_report_quarter = serializers.CharField(max_length=20)
#     initial_report_half_year = serializers.CharField(max_length=20)
#     standard_strata = serializers.CharField(max_length=20)
#     num_total_drug = serializers.IntegerField()
#     num_con_drug = serializers.IntegerField()
#     num_total_pt = serializers.IntegerField()
#     data_load_quarter = serializers.CharField(max_length=20)
#     flag_dup = serializers.BooleanField()
#     report_id_for_dupgroup = serializers.IntegerField()
#     num_rpts_in_dupgroup = serializers.IntegerField()
#     fda_case_id = serializers.IntegerField()