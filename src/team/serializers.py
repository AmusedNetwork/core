from rest_framework import serializers

from backend.mixins import IncorrectSolvesMixin
from challenge.serializers import SolveSerializer
from member.serializers import MinimalMemberSerializer
from backend.signals import team_create
from team.models import Team


class SelfTeamSerializer(IncorrectSolvesMixin, serializers.ModelSerializer):
    members = MinimalMemberSerializer(many=True, read_only=True)
    solves = SolveSerializer(many=True, read_only=True)
    incorrect_solves = serializers.SerializerMethodField()

    class Meta:
        model = Team
        fields = [
            "id",
            "is_visible",
            "name",
            "password",
            "owner",
            "description",
            "members",
            "solves",
            "incorrect_solves",
        ]
        read_only_fields = ["id", "is_visible", "incorrect_solves"]


class TeamSerializer(IncorrectSolvesMixin, serializers.ModelSerializer):
    members = MinimalMemberSerializer(many=True, read_only=True)
    solves = SolveSerializer(many=True, read_only=True)
    incorrect_solves = serializers.SerializerMethodField()

    class Meta:
        model = Team
        fields = [
            "id",
            "is_visible",
            "name",
            "owner",
            "description",
            "members",
            "solves",
            "incorrect_solves",
        ]

    def get_incorrect_solves(self, instance):
        return instance.solves.filter(correct=False).count()


class ListTeamSerializer(serializers.ModelSerializer):
    members = serializers.SerializerMethodField()

    class Meta:
        model = Team
        fields = ["id", "name", "members"]

    def get_members(self, instance):
        return instance.members.count()


class AdminTeamSerializer(IncorrectSolvesMixin, serializers.ModelSerializer):
    members = MinimalMemberSerializer(many=True, read_only=True)
    solves = SolveSerializer(many=True, read_only=True)
    incorrect_solves = serializers.SerializerMethodField()

    class Meta:
        model = Team
        fields = [
            "id",
            "is_visible",
            "name",
            "password",
            "owner",
            "description",
            "members",
            "solves",
            "incorrect_solves",
            "size_limit_exempt",
        ]


class MinimalTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ["id", "is_visible", "name", "owner", "description"]


class CreateTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ["id", "is_visible", "name", "owner", "password"]
        read_only_fields = ["id", "is_visible", "owner"]

    def create(self, validated_data):
        name = validated_data["name"]
        password = validated_data["password"]
        team = Team.objects.create(
            name=name, password=password, owner=self.context["request"].user
        )
        self.context["request"].user.team = team
        self.context["request"].user.save()
        team_create.send(sender=self.__class__, team=team)
        return team
