from django.db import models
from utils.reference_utils.model_choices import (SECTION_CHOICES,SECTION_CHOICES_1, SECTION_CHOICES_2, CHOICE_CLEARANCE_VERIFIED, CANDIDATE_EMPLOYMENT_CHOICE)
# from django.core.validators import RegexValidator

class AddProject(models.Model):

    #===================== Project section ============.
    
    project_name = models.CharField(max_length=75, null= False)
    project_description = models.CharField(max_length= 500, null= False)

    #===================== Job Information section ======.

    Job = models.ForeignKey('job', on_delete= models.CASCADE,null=False)


    #===================== No Of Opening===================.

    project_id = models.UUIDField(null= False)
    position_title = models.CharField(max_length= 255, null= False)
    security_requirement = models.CharField(max_length= 255)
    education = models.CharField(max_length= 255)
    language_requirement = models.CharField(max_length= 255)
    recruiter = models.ForeignKey('Model', on_delete= models.CASCADE)
    proposal_writer = models.ForeignKey('Model', on_delete= models.CASCADE)
    partner_specialist = models.ForeignKey('Model', on_delete= models.CASCADE)


    #================== Additional information section =========.


    potential_resources = models.IntegerField(null= False)
    project_requirement_status = models.CharField(null= False)
    technical_evaluation_resume = models.CharField(max_length= 50,choices= SECTION_CHOICES, default= 'N/A')
    project_financial = models.CharField(max_length= 50,
     choices= SECTION_CHOICES, default= 'N/A' )
    project_security = models.CharField(max_length= 50, choices= SECTION_CHOICES, default= 'N/A')
    education = models.CharField(max_length= 50, choices= SECTION_CHOICES_1, default= 'N/A')
    corporate_reference = models.CharField(max_length= 50, choices= SECTION_CHOICES_1, default= 'N/A')
    candidate_reference = models.CharField(max_length= 50, choices= SECTION_CHOICES_2, default= 'N/A')

    #=================  Validator For miscellanous   ================.

    # alpha_numeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    miscellanouse = models.CharField(max_length= 255, choices= SECTION_CHOICES, default='N/A')

    
    
    class Meta:
        db_table = 'add_project'
        verbose_name = 'add project'
        verbose_name_plural = 'add projects'

class ProjectUpdate(models.Model):

    #========================= Information Section ==================.
    
    resource_name = models.CharField(max_length= 255, null= False)
    hourly_bill_rate = models.DecimalField(decimal_places= 2, null= False)
    hourly_pay_rate =  models.DecimalField(decimal_places= 2, null= False)
    security_clearance_level = models.CharField(max_length= 255)
    security_clearance_expiry = models.DateField()
    security_clearance_verified = models.CharField(max_length= 50, choices=CHOICE_CLEARANCE_VERIFIED, null= False)
    security_file_number = models.CharField(max_length= 50)
    date_of_birth = models.DateField()
    candidate_reference_verification = models.CharField(max_length= 50, choices= CHOICE_CLEARANCE_VERIFIED, null= False)
    education_verification = models.CharField(max_length= 50, choices= CHOICE_CLEARANCE_VERIFIED, null= False)
    candidate_employment =  models.CharField(max_length= 50, choices= CANDIDATE_EMPLOYMENT_CHOICE, null= False)
    candidate_meets = models.CharField(max_length= 50, choices= CHOICE_CLEARANCE_VERIFIED, null= False)
    #========= How this field work? ============.
    candidate_rated_requirement = models.IntegerField(null= False)
    candidate_language_requirement = models.CharField(max_length= 50, null= False)

    #======================== File sections ==============.
    
    # Prepared Resume fields?
    # Exclusively agreement fields?
    # NDA fields?
    # Education fields?
    # Candidate reference fields?
    class Meta:
        db_table = 'project_update'
        verbose_name = 'project update'
        verbose_name_plural = 'project updates'

# ================== Project Dashboard ===============.
class ProjectDashboard(models.Model):
    
    #===================== Top Section =================.
    
    project_id = models.UUIDField(null= False) # is we need to extract id from addproject class.
    project_name = models.CharField(max_length= 255, null= False)
    
    #==================== Lower Top =====================.

    technical_readliness = models.CharField(max_length= 255)
    financial_readliness = models.CharField(max_length= 255)
    security_readliness = models.CharField(max_length= 255)
    language_verification = models.CharField(max_length= 255)
    corporate_reference_readliness = models.CharField(max_length= 255)
    education = models.CharField(max_length= 255)

    #==================== Center Right ====================.

    technical_evaluation_check = models.CharField(max_length= 255)
    financial_evaluation_check = models.CharField(max_length= 255)
    security_evaluation_check = models.CharField(max_length= 255)
    education_evaluation_check = models.CharField(max_length= 255)
    corporate_evaluation_check = models.CharField(max_length= 255)
    candidate_evaluation_check = models.CharField(max_length= 255)
    miscelaneous_check = models.CharField(max_length= 255)

    #==================== Center Bottom ====================.

    # this section will fetch information from project information update






