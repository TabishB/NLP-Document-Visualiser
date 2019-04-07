# Forum Mind

ForumMind’s project primarily encapsulates the analysis of any given text body (JSON, PDF and so on), performing the categorisation, summation and relation of such in terms of topic analysis and prevalence in easy to view graphical formats.  

Through heavy utilisation of NLTK/NLP text mining, database and front end web development the team has been able to analyse, store and graphically display large amounts of text to provide accurate and easily interpreted overviews. This enables users to determine context and relevance quickly, saving time on researching necessary resources or determining the relevance of any given text and providing a new level of understanding.  

## Getting Started

* [Installation Instructions](Installation Instructions)
* [User Walkthrough](User Walkthrough)
* [Demo Video](https://bitbucket.org/forummind/forummind/src/master/ForumMind%20Final%20Demo%20Video.mp4)
* [Final Deployment Set up Manual](Final Deployment Set up Manual)  
* [Database Implementation](Database implementation)

## Built With

### **Tools used** ###

| Tool                               | Description                          | Version |
|------------------------------------|--------------------------------------|---------|
| **Project Management Tools**       |                                      |         |
| Bitbucket                          | Version Control System               | N/A     |
| Trello                             | Task allocation and                  | N/A     |
| Google Drive                       | Documentation Storage                | N/A     |
|------------------------------------|--------------------------------------|---------|
| **Django Web App Tools**           |                                      |         |
| Django                             | Web Framework                        | 2.1.1   |
| Bootstrap 4                        | CSS Framework                        | 4.1     |
| D3.JS                              | Data visualization framework.        |         |
| Django-cripsy-forms                | Bootstrap style css for Django Forms | 1.7.2   |
| Python 3                           |                                      | 2018.5  |
|------------------------------------|--------------------------------------|---------|
| **Django Database Tools**          |                                      |         |
| Mlab                               | MongoDB cloud hosting service        | N/A     |
| Django-rest-framework- mongoengine |                                      | 3.3.1   |
| Djongo                             |                                      | 1.2.30  |
|------------------------------------|--------------------------------------|---------|
| **LDA Tools**                      |                                      |         |
| Nltk                               |                                      | 3.3     |
| Genism                             |                                      | 3.6.0   |
| Numpy                              |                                      | 1.15.2  |
| Pandas                             |                                      | 0.23.4  |
| Spacy                              |                                      | 2.0.12  |
| Mallet                             |                                      | 2.0.8   |
| Python 3                           |                                      | 2018.5  |

**Languages:** • python

**Frameworks:** • Django • Bootstrap • D3.js

**Libraries:** • NLTK • pandas • scikit-learn • matplotlib • pyLDAvis • Gensim • spacy

**Development Environments:** • Jupyter • Atom • Visual Studio Code

**Version Control:** • Bitbucket • GitKraken • SourceTree

**Databases:** • MongoDB


## Documentation

**ER digram:**
![Untitled Diagram.png](https://bitbucket.org/repo/gkMeG6A/images/4115154197-Untitled%20Diagram.png)

**Sequence diagram:**
![Sequence Diagram.png](https://bitbucket.org/repo/gkMeG6A/images/2165513940-Sequence%20Diagram.png)

**Database diagram:**  
![erd forummind.png](https://bitbucket.org/repo/gkMeG6A/images/3743896194-erd%20forummind.png)  

**LDA model diagram:**
![LDA model diagram.png](https://bitbucket.org/repo/gkMeG6A/images/1512815332-LDA%20model%20diagram.png) 

**A7:Team Meetings**

* [Week 1](Week 1 Meeting a: Initial Formation)
* [Week 2](Week 2 Meeting a: Next Steps)
* [Week 3](Week 3 Meeting: )
* [Week 4](Week 4 Meeting: Prototype Sprint)
* [Week 5](Week 5 Meeting: Report and new task delegation sprint)
* [Week 6](Week 6 Meeting: New sprint task allocations)
* [Week 7](Week 7 Meeting: DB Concerns and sprint check up)
* [Week 8](Week 8 Meeting: Midsem break task sprint)
* [Week 9](Week 9 Meeting: Final integration sprint)
* [Week 10](Week 10 Meeting: More graphs!)
* [Week 11](Week 11 Meeting: Next Sprint)
* [Week 12](Week 12: Final steps)
* [Week 13](Week 13: Presentation, demo, deployment and reports)

**Requirements:** 

1.  User must be able to upload either a pdf, .txt, or JSON file for processing
2.  The uploaded corpus must be stored (with a downloadable link) so that the user can view it afterwards 
    without having to wait.
3.  User must be notified when the file has been processed for visualisations.
4.  User must be able to click on the file to view options for visualisations.
5.  User must receive an estimation for the upload of the file.
6.  User must be able to view a word cloud of the uploaded file  
7.  User must be able to view a topical cloud of the uploaded file  
8.  User must be able to view a fishbone diagram of the uploaded file  
9.  User must be able to view a bar chart of the uploaded file  
10. User must be able to view a bubble graph of the uploaded file



### **Details of Tests** ###

| ﻿Number | Type  | User Story                                                                                                                                                     | Acceptance Test  | Nature                                                                                                                                                                                                    |   |   |   |   |   |
|--------|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|---|---|---|---|
| 1      | Epic  | As a user, I can upload a corpus so that it can be stored, processed and retrieved at a later date.                                                            |                                   |Normal                                                                                                                                                                                   |   |   |   |   |   |
| 2      | Story | As a user, I can upload a corpus in txt, pdf or word document formats so that the system can process and store it                                              | Upload multiple corpus in ALL text, pdf, json  and txt. Contents can be arbitrary however at least 1 corpus must have manually counted each word to cross reference with the result so smaller might be better. |Normal|   |   |   |   |   |
| 3      | Story | As a user, I can retrieve my uploaded corpus at a later date so that I don't have to reupload the same documents costing me time and bandwidth                 | Test that the link to each document works.   |Normal                                                                                                                                                                        |   |   |   |   |   |
| 4      | Story | As a user, I can download my uploaded corpus in the same format it was uploaded so I can retrieve the exact document that was uploaded                         | downnload each document and compare it to the original document.                |Normal                                                                                                                                     |   |   |   |   |   |
| 5      | Story | As a user wanting to view the corpus in a visual format, I will receive a notification when the analysis has been completed                                    | Test that the document is in home once it has been uploaded (wait 20-25 minutes).           |Normal                                                                                                                         |   |   |   |   |   |
| 6      | Epic  | As a user with an uploaded corpus, I want to be able to visualise the text in a summarised form                                                                |                                              |Normal                                                                                                                                                                        |   |   |   |   |   |
| 7      | Story | As a user with an uploaded corpus, I can click on the corpus to select it once it has been analysed so that I can select specific visualisations               | Using an uploaded corpus, confirm that the graphs visually describe the corpus                 |Normal                                                                                                                      |   |   |   |   |   |
| 8      | Story | As a user with multiple corpus',I can see which corpus' are ready to be viewed as visualisations from my homepage so that I can select them and visualise them | After uploading a valid corpus, click through to the graph dashboard                             |Normal                                                                                                                    |   |   |   |   |   |
| 9     | Epic  | As a user with an analysed corpus, I can view each visualisation from a dashboard by clicking the visualisation type                                           |                 |Normal                                                                                                                                                                                                     |   |   |   |   |   |
| 10     | Story | As a user with an analysed corpus, I can select from word cloud, topical cloud and fishbone diagram to better understand the context of the corpus             | After uploading a valid corpus and clicking through to the graph dashboard, click on each button to assess that the graph represents the data.       |Normal                                                                |   |   |   |   |   |
| 11     | Story | As a user with an analysed corpus, I can select from concept cloud, layout tree and bubble chart to better understand the context of the corpus                | After uploading a valid corpus and clicking through to the graph dashboard, click on each button to assess that the graph represents the data.     |Normal                                                                  |   |   |   |   |   |
| 12     | Epic  | As a user, I can navigate the application from a side-bar so that I can quickly move between corpus'                                                           |               |Normal                                                                                                                                                                                                       |   |   |   |   |   |


## Authors

* Sam Higgs
* Emma Muscat
* Shenin Faizah
* Thad Shattuck
* Roy Gu
* Tabish Bidiwale

	



