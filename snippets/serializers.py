from rest_framework import serializers

from django.contrib.auth.models import User  #new

from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES




class SnippetSerializer(serializers.HyperlinkedModelSerializer):          #new new
	owner = serializers.ReadOnlyField(source="owner.username")     #new
	highlight = serializers.HyperlinkedIdentityField(view_name="snippet-highlight", format="html") #new new

	class Meta:
		model = Snippet
		fields = ("url", "id", "highlight", "title", "code", "linenos", "language", "style", "owner",)



class UserSerializer(serializers.HyperlinkedModelSerializer):
	snippets = serializers.HyperlinkedRelatedField(many=True, view_name="snippet-detail", read_only=True)

	class Meta:
		model = User
		fields = ("url", "id", "username", "snippets")