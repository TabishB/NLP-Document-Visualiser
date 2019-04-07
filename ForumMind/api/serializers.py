from rest_framework_mongoengine import serializers
from api.models import *

class WordSerializer(serializers.EmbeddedDocumentSerializer):
    class Meta:
        model = Word
        fields = '__all__'

    def create(self, validated_data):
        word = validated_data.pop('word')
        created_instance = Word.objects.create(**validated_data).append(word)
        created_instance.save()
        return created_instance

class WordsSerializer(serializers.DocumentSerializer):
    words = WordSerializer(many=True)

    class Meta:
        model = Words
        fields = '__all__'
        depth = 2

    def create(self, validated_data):
        words = validated_data.pop('words')
        created_instance = Words.objects.create(**validated_data)
        created_instance.words = []
        for word in words:
            created_instance.words.append(Word(**word))
        created_instance.save()
        return created_instance

    def update(self, instance, validated_data):
        words = validated_data.pop('words')
        updated_instance = super(WordsSerializer, self).update(instance, validated_data)

        for word in words:
            updated_instance.words.append(Word(**word))

        updated_instance.save()
        return updated_instance

class TopicSerializer(serializers.EmbeddedDocumentSerializer):
    keywords = WordSerializer(many=True)

    class Meta:
        model = Topic
        fields = '__all__'
        depth = 2

    def create(self, validated_data):
        keywords = validated_data.pop('keywords')
        # keywords = validated_data.pop('keywords')
        created_instance = Topic.objects.create(**validated_data)
        created_instance.keywords = []
        for word in keywords:
            created_instance.keywords.append(Word(**word))
        created_instance.save()
        return created_instance

class TopicsSerializer(serializers.DocumentSerializer):
    data = TopicSerializer(many=True)

    class Meta:
        model = Topics
        fields = '__all__'
        depth = 2


    def create(self, validated_data):
        data = validated_data.pop('data')
        # keywords = validated_data.pop('keywords')
        created_instance = Topics.objects.create(**validated_data)
        created_instance.data = []
        for topic in data:
            created_instance.data.append(Topic(**topic))
        created_instance.save()
        return created_instance

class RecursiveField(serializers.EmbeddedDocumentSerializer):
    class Meta:
        model = Fishbone
        fields = '__all__'

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data

class FishboneSerializer(serializers.EmbeddedDocumentSerializer):
    children = RecursiveField(many=True, required=False)

    class Meta:
        model = Fishbone
        depth = 5
        fields = '__all__'

    def create(self, validated_data):
        children = None
        if 'children' in validated_data:
            children = validated_data.pop('children')

        created_instance = super(FishboneSerializer, self).create(validated_data)
        created_instance.children = None
        created_instance.save()

        child_lst = []
        if children:
            created_instance.children = []
            for child in children:
                childObj = Fishbone(**child)
                child_lst.append(childObj)


        if len(child_lst)>0:
            for child in child_lst:
                created_instance.children.append(child)
            created_instance.save()

        return created_instance

class FishSerializer(serializers.DocumentSerializer):
    children = FishboneSerializer(many=True, required=False)

    class Meta:
        model = Fish
        depth = 6
        fields = '__all__'

    def create(self, validated_data):
        children = None
        if 'children' in validated_data:
            children = validated_data.pop('children')

        created_instance = super(FishSerializer, self).create(validated_data)
        created_instance.children = []
        created_instance.save()

        child_lst = []
        if children:
            for child in children:
                childObj = Fishbone(**child)
                child_lst.append(childObj)


        if len(child_lst)>0:
            for child in child_lst:
                created_instance.children.append(child)
            created_instance.save()

        return created_instance


    # def recursive_create(self, validated_data):
    #     children = validated_data.pop('children')
    #     created_instance = super(FishboneSerializer, self).create(validated_data)
    #     created_instance.children = []
    #     for child in children:
    #         created_instance.children.append(Fishbone(**child))
    #     created_instance.cascade_save()
    #     return created_instance

# class ConceptsSerializer(serializers.DocumentSerializer):
#     class Meta:
#         model = Concepts
#         fields = '__all__'

class TweetsSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Tweets
        fields = '__all__'
