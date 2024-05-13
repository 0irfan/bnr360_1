from rest_framework import serializers
from .models import (AddProject, ProjectUpdate)

# ======= Serializer for Add Project of Jv_collab ====. 

class AddProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddProject
        fields = '__all__'



# ======= Serializer for fetching fields of No Of Opening ======.

class FetchSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddProject
        fields = ['id','position_title']

# ======= Serialzer for project update ===========.
class UpdateSerializer(serializers.ModelSerializer):
    fetch_fields = FetchSerializer(many= True)
    class Meta:
        model = ProjectUpdate
        fields = '__all__'