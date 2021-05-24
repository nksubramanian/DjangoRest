from rest_framework import serializers
#from rest_framework import employees


class employeesSerializer(serializers.ModelSerializer):

    class Meta:
        model = employeesSerializer
        #fields = ("firstname","lastname")
    fields = "__all__"