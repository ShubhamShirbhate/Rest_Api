from rest_framework import serializers
from .models import Paradigm, Proggrammer, Languages



class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model   = Languages
        fields  = ('id','url', 'name', 'paradigm')

 

class ParadigmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model   = Paradigm
        fields  = ('id','url', 'name')


class ProggrammerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model   = Proggrammer
        fields  = ('id','url', 'name', 'language')

