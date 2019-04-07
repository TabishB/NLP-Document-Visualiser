########CLIENT SIDE TEST CASES###########
#To run this use python manage.py test visualiser --settings=ForumMind.testing_settings 
# from django.test import TestCase, Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

import mongoengine
import mongomock
import test_addons
import unittest
import test_addons

from api.models import *
from visualiser.models import *
from visualiser.forms import DocumentForm

class FileUplodingFormTest(test_addons.MongoTestCase):
    def setUp(self):
        # self.userClient = Client()
        self.client = mongomock.MongoClient()
        self.client.db.create_collection('visualiser_filedoc')
        self.client.db.create_collection('words')
        self.client.db.create_collection('topics')
        self.testfile = SimpleUploadedFile('testFiles/test.json', b'file_content', content_type='text/json')
        self.filedoc = FileDoc(topics=3, document='testFiles/test.json')
        # self.filedoc.save()
    
    #If it doesn't init properly this will raise an error. No need to define an exception.
    def test_init(self):
        DocumentForm()

    def test_valid_data(self):
        form = DocumentForm({
            'topics': 3,
            'document': self.filedoc
        })
        if not form.is_valid():
            print(form.errors)
        self.assertTrue(form.is_valid())
        uploaded_doc = form.save()
        self.assertEqual(uploaded_doc.topics, 3)
        self.assertEqual(uploaded_doc.document, 'testFiles/test.json')

    def test_blank_data(self):
        form = DocumentForm({})

        self.assertFalse(form.is_valid())
        self.assertEquals(form.errors, {
            'document' : ['This field is out of bounds.']
        })
 
    def test_lower_bound_topic(self):
        form = DocumentForm({'topics': 2, 'document': self.filedoc})

        self.assertFalse(form.is_valid())
        self.assertEquals(form.errors, {
            'topics' : ['This field is out of bounds.']
        })

    def test_upped_bound_topic(self):
        form = DocumentForm({'topics': 21, 'document': self.filedoc})

        self.assertFalse(form.is_valid())
        self.assertEquals(form.errors, {
            'topics' : ['This field is out of bounds.'],
        })

    def test_json_file(self):
        dform = DocumentForm(data={'topics': 3, 'document': self.filedoc})
        self.assertTrue(dform.is_valid())
        # res = self.client.post(reverse('home'), dform)
        # self.assertEqual(res.status_code, 200)

    def test_docx_file(self):
        testFile = FileDoc(topics=3, document='testFiles/test.docx')
        dform = DocumentForm(data={'topics': 3, 'document': testFile})
        
        self.assertTrue(dform.is_valid())

    #Need confirmation on whether we are still doing this.
    def test_text_file(self):
        testFile = FileDoc(topics=3, document='testFiles/test.txt')
        dform = DocumentForm(data={'topics': 3, 'document': testFile})
        
        self.assertTrue(dform.is_valid())

    def test_pdf_file(self):
        testFile = FileDoc(topics=3, document='testFiles/test.pdf')
        dform = DocumentForm(data={'topics': 3, 'document': testFile})
        
        self.assertTrue(dform.is_valid())

    def test_doc_file(self):
        testFile = FileDoc(topics=3, document='testFiles/test.doc')
        dform = DocumentForm(data={'topics': 3, 'document': testFile})
        
        self.assertTrue(dform.is_valid())

    # def test_corrupted_file(self):
    #     file = SimpleUploadedFile("testFiles/testCorrupted.txt", b"file_content")
    #     res = self.client.post(reverse('home', {'file': file, 'topics':3}))
        
    #     self.assertEqual(res.status_code, 200)

    def test_othertype_invalid_file(self):
        testFile = FileDoc(topics=3, document='testFiles/test.java')
        dform = DocumentForm(data={'topics': 3, 'document': testFile})
        
        self.assertFalse(dform.is_valid())
    
    def test_jpg_invalid_file(self):
        testFile = FileDoc(topics=3, document='testFiles/test.jpg')
        dform = DocumentForm(data={'topics': 3, 'document': testFile})
        
        self.assertFalse(dform.is_valid())

class URLTest(test_addons.MongoTestCase):
    @classmethod
    def setUp(self):

        # self.client = mongomock.MongoClient()
        # self.client.db.create_collection('visualiser_filedoc')
        # self.client.db.create_collection('words')
        # self.client.db.create_collection('topics')
        self.testfile = SimpleUploadedFile('testFiles/test.json', b'file_content', content_type='text/json')
        self.filedoc = FileDoc(topics=3, document='tweets.json')
        # self.filedoc.save()
        testDocument = {
        "document": "testDocument",
            "data": [{
                'topic': 1,
                'keywords':
                [
                    {
                        "word": "Calf",
                        "frequency": 2
                    },
                    {
                        "word": "Guava",
                        "frequency": 3
                    },
                    {
                        "word": "Avocado",
                        "frequency": 8
                    },
                    {
                        "word": "Pear",
                        "frequency": 12
                    },
                    {
                        "word": "Sugar",
                        "frequency": 18
                    },
                    {
                        "word": "Grape",
                        "frequency": 20
                    },
                    {
                        "word": "Banana",
                        "frequency": 23
                    },
                    {
                        "word": "Cinnamon",
                        "frequency": 33
                    },
                    {
                        "word": "Tomato",
                        "frequency": 39
                    },
                    {
                        "word": "Brownie",
                        "frequency": 41
                    },
                    {
                        "word": "Mango",
                        "frequency": 56
                    },
                    {
                        "word": "Orange",
                        "frequency": 80
                    },
                    {
                        "word": "Coffee",
                        "frequency": 81
                    },
                    {
                        "word": "Apple",
                        "frequency": 100
                    }
                ]
            }]
        }
        words_list = []
        for w in testDocument['data'][0]['keywords']:
            words_list.append(Word(**w))
        #Ensure that the test documents are 
        if Words.objects.filter(document='testDocument').count() == 0:
            print('testDocument not found in "words" collection, creating new testDocument')
            wordObj = Words(document=testDocument['document'], words=words_list)
            wordObj.save()
        if Topics.objects.filter(document='testDocument').count() == 0:
            print('testDocument not found in "topics" collection, creating new testDocument')
            topicObj = Topics(**testDocument)
            topicObj.save()
        self.dName = 'testDocument'
        
    def test_visualiser_home_page(self):
        res = self.client.get(reverse('home', kwargs={}))

        self.assertEqual(res.status_code, 200)
    
    def test_graphs_page(self):
        res = self.client.get(reverse('graphs', kwargs={'slug':self.dName}))
        
        self.assertEqual(res.status_code, 200)
    
    def test_wordcloud_page(self):
        res = self.client.get(reverse('wordcloud', kwargs={'slug':self.dName}))
        
        self.assertEqual(res.status_code, 200)
    
    def test_topicalcloud_page(self):
        res = self.client.get(reverse('topicalcloud', kwargs={'slug':self.dName}))
        
        self.assertEqual(res.status_code, 200)
    
    def test_fishbone_page(self):
        res = self.client.get(reverse('fishbone', kwargs={'slug':self.dName}))
        
        self.assertEqual(res.status_code, 200)
    
    def test_bubblegraph_page(self):
        res = self.client.get(reverse('bubblegraph', kwargs={'slug':self.dName}))
        
        self.assertEqual(res.status_code, 200)
    
    def test_barchart_page(self):
        res = self.client.get(reverse('barchart', kwargs={'slug':self.dName}))
        self.assertEqual(res.status_code, 200)

    


##### I dont think these are useful at all...
    # def get_homepage_test(self):
    #     # Issue a GET request.
    #     response = self.client.get('/visualiser/')

    #     # Check that the response is 200 OK.
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(len(response.context['documents']), 0)

    # def test_get2(self):
    #     # Issue a GET request.
    #     response = self.client.get('/visualiser/')

    #     # Check that the response is 200 OK.
    #     self.assertEqual(response.status_code, 200)
    #     self.assertNotEqual(len(response.context['widget']), 0)

    # def test_post(self):
    #     # Issue a Post request.
    #     response = self.client.post('/visualiser/', {'username': 'john', 'password': 'smith'})

    #     # Check that the response is 200 OK.
    #     self.assertEqual(response.status_code, 200)

    # def test_post2(self):
    #     # Issue a Post request.
    #     response = self.client.post('/visualiser/home/', {'username': 'john', 'password': 'smith'})

    #     # Check that the response is 200 OK.
    #     self.assertNotEqual(response.status_code, 200)

    
    

