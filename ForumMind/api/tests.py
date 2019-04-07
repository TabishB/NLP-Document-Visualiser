# Collection of tests designed to test the creation of documents in the database is created
# With the right formatting as well as persisting. It uses a mockmongo database which is created
# and destroyed after each testsuite.
# Make sure the test_ is the name of each function or it won't run
# To run this use python manage.py test visualiser --settings=ForumMind.testing_settings

from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from django.test import Client
from django.core.validators import ValidationError

import test_addons
import mongomock
from api.models import *

import copy
class WordsModelTests(test_addons.MongoTestCase):

    def setUp(self):
        #create a mock client.
        self.client = mongomock.MongoClient()
        self.words_collection = self.client.db.create_collection('words')
    
    #Test that this creates a document and stored the result as the first entry
    def test_one_word_add(self):
        Words(document='test', words=[Word(word='alpha', frequency=10)]).save()
        
        self.assertEqual(len(Words.objects.filter(document='test')), 1)
        self.assertEqual(Words.objects.get(document='test').document, 'test')
        self.assertEqual(Words.objects.get(document='test').words[0].word, 'alpha')
        self.assertEqual(Words.objects.get(document='test').words[0].frequency, 10)

    ###############DATABASE TESTS#####################
    #Test to check what happens if document name already exists
    def test_same_document_name(self):
        Words(document='test2', words=[Word(word='alpha', frequency=10)]).save()
        Words(document='test2', words=[Word(word='beta', frequency=9)]).save()

        self.assertEqual(len(Words.objects.filter(document='test2')),1)

    #This test checks that multiple word objects will enter the document.
    def test_multiple_word_add(self):
        wordOne = {'word':'one', 'frequency':10}
        wordTwo = {'word':'two', 'frequency':10}
        wordThree = {'word':'three', 'frequency':10}
        Words(document='test3', words=[
                                    Word(**wordOne),
                                    Word(**wordTwo),
                                    Word(**wordThree),
                                    ]).save()

        self.assertEqual(len(Words.objects.get(document='test3').words),3)
        self.assertEqual(Words.objects.get(document='test3').words[0].word, wordOne['word'])
        self.assertEqual(Words.objects.get(document='test3').words[1].word, wordTwo['word'])
        self.assertEqual(Words.objects.get(document='test3').words[2].word, wordThree['word'])

    #This tests that sequential entries will be entered into separate documents.
    def test_sequential_entry(self):
        wo = Words(document='test4.1', words=[Word(word='alpha', frequency=10)])
        wo.save()
        woTwo = Words(document='test4.2', words=[Word(word='beta', frequency=9)])
        woTwo.save()
        self.assertEqual(Words.objects.get(document='test4.1'), wo)
        self.assertEqual(Words.objects.get(document='test4.2'), woTwo)

    #Test to append an existing document
    def test_update_document(self):
        wo = Words(document='test5', words=[Word(word='alpha', frequency=10)])
        wo.save()
        self.assertEqual(Words.objects.get(document='test5'), wo)
        Words.objects.get(document='test5').update(document='test5.1')
        result = Words.objects.filter(document='test5')
        self.assertEqual(result.count(), 0)
        self.assertEqual(Words.objects.get(document='test5.1').words[0].word, 'alpha')
        self.assertEqual(Words.objects.get(document='test5.1').words[0].frequency, 10)

    #tests max size of document name
    ##########WILL COME BACK TO THIS TESTCASE
    # def test_document_name_invalid_size(self):
    #     docName = ''
    #     for i in range(0,300):
    #         docName += 'a'
    #     self.assertEqual(len(docName), 300)
    #     with self.assertRaises(ValidationError):
    #         wo = Words(document=docName, words=[Word(word='alpha', frequency=10)])
    #         wo.clean()
    #         wo.save()

    #tests empty document name
    def test_document_name_empty(self):
        with self.assertRaises(ValidationError):
            wo = Words(document='', words=[Word(word='alpha', frequency=10)]).save()
            wo.clean()
            wo.save()

    #test empty words list
    def test_empty_words_list(self):
        with self.assertRaises(ValidationError):
            wo = Words(document='test8', words=[]).save()


class TopicsModelTests(test_addons.MongoTestCase):
    @classmethod
    def setUp(self):
        #create a mock client.
        self.client = mongomock.MongoClient()
        self.topic_collection = self.client.db.create_collection('topics')
        self.topics_data = {
            'document': 'example_document',
            'data' : [
                {
                    'topic' : 1,
                    'keywords' : [
                        {'word' : 'alpha', 'frequency' : 10},
                        {'word' : 'bravo', 'frequency' : 9},
                        {'word' : 'charlie', 'frequency' : 8},
                    ]
                }
            ]
        }
        self.topics_data2 = {
            'document': 'example_document2',
            'data' : [
                {
                    'topic' : 1,
                    'keywords' : [
                        {'word' : 'alpha', 'frequency' : 10},
                        {'word' : 'bravo', 'frequency' : 9},
                        {'word' : 'charlie', 'frequency' : 8},
                    ]
                }
            ]
        }
        self.topics_data3 = {
            'document': 'example_document3',
            'data' : []
        }
        self.topics_data4 = {
            'document': 'example_document4',
            'data' : [
                {
                    'topic' : 1,
                    'keywords' : [
                        {'word' : 'alpha', 'frequency' : 10},
                        {'word' : 'bravo', 'frequency' : 9},
                        {'word' : 'charlie', 'frequency' : 8},
                    ]
                }
            ]
        }
        self.topics_data5 = {
            'document': 'example_document5',
            'data' : [
                {
                    'topic' : 1,
                    'keywords' : [
                        {'word' : 'alpha', 'frequency' : 10},
                        {'word' : 'bravo', 'frequency' : 9},
                        {'word' : 'charlie', 'frequency' : 8},
                    ]
                }
            ]
        }
    #Test that this creates a document and stored the result as the first entry
    def test_one_topic_add(self):
        topic_obj = Topics(**self.topics_data)
        topic_obj.save()
        self.assertEqual(Topics.objects.get(document='example_document'), topic_obj)

    ###############DATABASE TESTS#####################
    #Test to check what happens if document name already exists
    def test_same_topic_name(self):
        topics = copy.deepcopy(self.topics_data)
        topics['document']='test2'
        Topics(**topics).save()

        self.assertEqual(len(Topics.objects.filter(document='test2')),1)

    #This test checks that multiple topics will enter the document.
    def test_multiple_topics_add(self):
        Topics(**self.topics_data4).save()
        Topics(**self.topics_data5).save()

        self.assertEqual(Topics.objects.filter(document='example_document4').to_json(), self.topics_data4)
        self.assertEqual(Topics.objects.filter(document='example_document5').to_json() , self.topics_data5)

    #This tests that sequential entries will be entered into separate documents.
    def test_sequential_entry(self):
        topic_obj = Topics(**self.topics_data)
        topic_obj['document']='test3'
        topic_obj.save()
        topic_obj2 = Topics(**self.topics_data2)
        topic_obj2['document']='test4'
        topic_obj2.save()

        self.assertEqual(Topics.objects.get(document='test3'), topic_obj)
        self.assertEqual(Topics.objects.get(document='test4'), topic_obj)

    #Test to append an existing document
    def test_update_document(self):
        topic_obj = Topics(**self.topics_data)
        topic_obj['document']='test5'
        topic_obj.save()
        self.assertEqual(Topics.objects.get(document='test5'), topic_obj)
        Topics.objects.get(document='test5').update(document='test6')
        result = Topics.objects.filter(document='test6')
        self.assertEqual(result.count(), 0)
        self.assertEqual(Topics.objects.get(document='test6').data[0].topic, 1)
        
    #tests max size of document name
    ##########WILL COME BACK TO THIS TESTCASE
    # def test_document_name_invalid_size(self):
    #     docName = ''
    #     for i in range(0,300):
    #         docName += 'a'
    #     self.assertEqual(len(docName), 300)
    #     with self.assertRaises(ValidationError):
    #         wo = Words(document=docName, words=[Word(word='alpha', frequency=10)])
    #         wo.clean()
    #         wo.save()

    #tests empty document name
    def test_document_name_empty(self):
        with self.assertRaises(ValidationError):
            topic_obj = Topics(**self.topics_data)
            topic_obj['document']='test7'
            topic_obj.save()
            topic_obj.clean()
            topic_obj.save()

    #test empty topics list
    def test_empty_topics_list(self):
        with self.assertRaises(ValidationError):
            topic_obj = Topics(**self.topics_data3)
            topic_obj.save()
