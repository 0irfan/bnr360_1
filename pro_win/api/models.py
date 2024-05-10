from django.db import models
from utils.reference_utils.model_choices import (SECTION_CHOICES,SECTION_CHOICES_1, SECTION_CHOICES_2)
from django.core.validators import RegexValidator

class JvCollab(models.Model):

    #===================== No Of Opening===================.

    id = models.UUIDField(null= False)
    job_title = models.CharField(max_length= 255, null= False)
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

    alpha_numeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    miscellanouse = models.CharField(max_length= 255, choices= SECTION_CHOICES, default='N/A',validators=[alpha_numeric])

    
    



    class Meta:
        db_table = 'jv_collab_edit'













