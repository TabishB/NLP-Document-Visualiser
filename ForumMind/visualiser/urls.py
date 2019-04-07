from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

	path('wordcloud/<slug:slug>/', views.wordcloud, name='wordcloud'),
    path('wordcloud/', views.wordcloud, name='wordcloud'),

    path('topicalcloud/<slug:slug>/', views.topicalcloud, name='topicalcloud'),
    path('topicalcloud/', views.topicalcloud, name='topicalcloud'),

	path('fishbone/<slug:slug>/', views.fishbone, name='fishbone'),
	path('fishbone/api/<slug:slug>/', views.fishbone_api, name='fishbone_api'),
	path('fishbone/api/', views.fishbone_api, name='fishbone_api'),
    path('fishbone/', views.fishbone, name='fishbone'),

	path('bubblegraph/<slug:slug>/', views.bubblegraph, name='bubblegraph'),
    path('bubblegraph/', views.bubblegraph, name='bubblegraph'),

	path('barchart/<slug:slug>/', views.barchart, name='barchart'),
    path('barchart/', views.barchart, name='barchart'),

	path('graphs/<slug:slug>/', views.graphs, name='graphs'),
	path('graphs/', views.graphs, name='graphs'),

    path('embed_fishbone/<slug:slug>/', views.embed_fishbone, name='embed_fishbone'),
	path('embed_fishbone/', views.embed_fishbone, name='embed_fishbone'),
]
