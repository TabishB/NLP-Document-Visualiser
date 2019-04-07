from mongoengine import Document, EmbeddedDocument, ReferenceField, fields

# Model for the [ {word: freq} ]
class Word(EmbeddedDocument):
    word = fields.StringField(max_length=255)
    frequency = fields.FloatField()

#Model for Word Cloud
class Words(Document):
    document = fields.StringField(max_length=256)
    words = fields.EmbeddedDocumentListField(Word)


#Model for the [ { topic: { keywords } } ]
class Topic(EmbeddedDocument):
    topic = fields.IntField()
    keywords = fields.EmbeddedDocumentListField(Word)

# Topic Cloud model
class Topics(Document):
    document = fields.StringField(max_length=255)
    data = fields.EmbeddedDocumentListField(Topic)

#Model for the [ {name: {children: [{name: children[] }]} } ]
class Fishbone(EmbeddedDocument):
    name = fields.StringField(max_length=255)
    children = fields.EmbeddedDocumentListField('self', default = [])

class Fish(Document):
    name = fields.StringField(max_length=255)
    children = fields.EmbeddedDocumentListField(Fishbone, default = [])

#Structure of tweets according to twitter API
class Tweets(Document):
    '''
    "{'hashtags', 'screenName', 'urls', 'isRetweet', 'images', 'replyCount', 'userMentions',
     'favoriteCount', 'text', 'isPinned', 'time', 'retweetCount', 'isReplyTo', 'quote'}"
    '''
    hashtags = fields.DynamicField()
    screenName = fields.DynamicField()
    urls = fields.DynamicField()
    isRetweet = fields.DynamicField()
    images = fields.DynamicField()
    replyCount = fields.DynamicField()
    userMentions = fields.DynamicField()
    favoriteCount = fields.DynamicField()
    text = fields.DynamicField()
    isPinned = fields.DynamicField()
    time = fields.DynamicField()
    retweetCount = fields.DynamicField()
    isReplyTo = fields.DynamicField()
    quote = fields.DynamicField()

    meta = {'collection' : 'tweets_data'}
