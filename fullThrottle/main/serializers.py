from rest_framework import serializers 
from rest_framework.serializers import ModelSerializer
from .models import Activity_Period, Member, Membership

class Activity_Period_Serializer(ModelSerializer):
    start_time = serializers.DateTimeField(format="%b %d %Y %I:%M%p")
    end_time = serializers.DateTimeField(format="%b %d %Y %I:%M%p") 
    class Meta:
        model = Activity_Period
        fields = [
            "start_time",
            "end_time"
            ]

class MemberListSerializer(ModelSerializer):
    activity_periods = Activity_Period_Serializer(many=True)
    id = serializers.SerializerMethodField('get_alternate_name')
    class Meta:
        model = Member
        fields = [
            "id",
            "real_name",
            "tz",
            "activity_periods"
            ]
        
    def get_alternate_name(self, obj):
        return obj.member_id
    
class MembershipListSerializer(ModelSerializer):
    members = MemberListSerializer(many=True)
    class Meta:
        model = Membership
        fields = [
            "ok",
            "members"
            ]