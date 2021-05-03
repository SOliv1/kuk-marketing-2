from django.test import TestCase

# Create your tests here.
{% load embed_video_tags %}

<!-- The video tag: -->
{% video item.video as my_video %}
  URL: {{ video .url }}
  Thumbnail: {{ video.thumbnail }}
  Backend: {{ video.backend }}

  {% video my_video "large" %}
{% endvideo %}

<!-- Or embed shortcut: -->
{% video my_video '800x600' %}


