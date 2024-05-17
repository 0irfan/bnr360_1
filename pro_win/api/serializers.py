from rest_framework import serializers
from .models import (AddProject, ProjectUpdate, Files, ProjectManager)

#================= fetch information from job tracking ====.
class JobTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = 'JobTracking'
        fields = ['no_of_opening','reference_no','procurement_vehicle','job_mode','job_location','client_company','due_time','due_date','language_requirement','clearance_required']





# ======= Serializer for Add Project of Jv_collab ====. 
class AddProjectSerializer(serializers.ModelSerializer):
    detail_of_job = JobTrackingSerializer(many = True)
    class Meta:
        model = AddProject
        fields = '__all__'





# ======= Serializer for fetching fields of No Of Opening ======.
class FetchSerializer(serializers.ModelSerializer):
     class Meta:
        model = AddProject
        fields = ['project_id','position_title',]




# ======= Serialzer for project update ===========.
class UpdateInformationSerializer(serializers.ModelSerializer):
    position_heading = FetchSerializer(many= True) # fetchiing position_title and id..
    class Meta:
        model = ProjectUpdate
        fields = ['resource_name','hourly_bill_rate','hourly_pay_rate','security_clearance_level','security_clearance_expiry','security_clearance_verified','security_file_number','candidate_reference_verification','education_verification','candidate_employment','candidate_meets','candidate_rated_requirement','candidate_language_requirement']


class ProjectManagerSerializer(serializers.Serializer):
    project = AddProjectSerializer
    class Meta:
        model = ProjectManager
        fields = ['project','technical_readline','financial_readlines','security_readlines','language_verification','corporate_reference_readlines','education','technical_evaluation_check','financial_evaluation_check','security_evaluation_check','corporate_reference_check','candidate_reference_check','educational_evaluation_check','miscellaneous_check']



class DashboardSerializer(serializers.Serializer):
    dashboard = ProjectManagerSerializer(many = True)
    class Meta:
        model = ProjectUpdate
        fields = ['dashboard','applicant_name','hourly_bill_rate','hourly_pay_rate','security_clearance_verified','resource_met_requirement','resource_rated_requirement']


class FileSerializer(serializers.Serializer):
    class Meta:
        model = Files
        fields = '__all__'