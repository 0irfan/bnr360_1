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
    class Meta:
        model = AddProject
        fields = [
            'project_id',
            'project_name',
            'project_description',
            'Job',
            'no_of_opening',
            'position_title',
            'security_requirement',
            'education',
            'language_requirement',
            'recruiter',
            'proposal_writer',
            'partner_specialist',
            'potential_resources',
            'project_requirement_status',
            'technical_evaluation_resume',
            'project_financial',
            'project_security',
            'education',
            'corporate_reference',
            'candidate_reference',
            'miscellanouse',
        ]

    def validate(self, data):
        required_fields = [
            'technical_evaluation_resume',
            'project_financial',
            'project_security',
            'education',
            'corporate_reference',
            'candidate_reference',
            'miscellanouse'
        ]
        
        status = ['ready to submit', 'submitted', 'N/A']
        
        for field in required_fields:
            if data.get(field) not in status:
                raise serializers.ValidationError(f"{field} must be one of {status}")
        
        return data


class ProjectDashboardSerializer(serializers.ModelSerializer):
    overall_project_status = serializers.SerializerMethodField()
    submission_checklist_status = serializers.SerializerMethodField()

    class Meta:
        model = AddProject
        fields = [
            'project_id',
            'project_name',
            'project_description',
            'technical_evaluation_resume',
            'project_financial',
            'project_security',
            'education',
            'corporate_reference',
            'candidate_reference',
            'miscellanouse',
            'overall_project_status',
            'submission_checklist_status',
        ]

    def get_overall_project_status(self, obj):
        statuses = [
            obj.technical_evaluation_resume,
            obj.project_financial,
            obj.project_security,
            obj.education,
            obj.corporate_reference,
            obj.candidate_reference,
            obj.miscellanouse
        ]

        if all(status == 'Not Started' for status in statuses):
            return 'Red'
        elif all(status in ['ready to submit', 'submitted'] for status in statuses):
            return 'Green'
        elif all(status == 'N/A' for status in statuses):
            return 'Grey'
        elif any(status == 'In Progress' for status in statuses):
            return 'Yellow'
        elif any(status in ['ready to submit', 'submitted'] for status in statuses) and all(status in ['N/A', 'ready to submit', 'submitted'] for status in statuses):
            return 'Green'
        return 'Grey'

    def get_submission_checklist_status(self, obj):
        checklist_fields = [
            'technical_evaluation_resume',
            'project_financial',
            'project_security',
            'education',
            'corporate_reference',
            'candidate_reference',
            'miscellanouse'
        ]

        status_dict = {}
        for field in checklist_fields:
            value = getattr(obj, field)
            if value in ['ready to submit', 'submitted']:
                status_dict[field] = 'checked'
            elif value == 'N/A':
                status_dict[field] = 'N/A'
            else:
                status_dict[field] = 'cross'

        if all(value in ['checked', 'N/A'] for value in status_dict.values()):
            status_dict['overall_status'] = 'Passed'
        else:
            status_dict['overall_status'] = 'Failed'

        return status_dict

    def validate(self, data):
        required_fields = [
            'technical_evaluation_resume',
            'project_financial',
            'project_security',
            'education',
            'corporate_reference',
            'candidate_reference',
            'miscellanouse'
        ]
        
        status = ['ready to submit', 'submitted', 'N/A', 'Not Started', 'In Progress']
        
        for field in required_fields:
            if data.get(field) not in status:
                raise serializers.ValidationError(f"{field} must be one of {status}")
        
        return data



class FileSerializer(serializers.Serializer):
    class Meta:
        model = Files
        fields = '__all__'