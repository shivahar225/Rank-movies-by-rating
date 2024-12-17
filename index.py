<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>index</title>
</head>
<body>
{% extends 'base.html' %}
{% block title %}My Top 10 Movies{% endblock %}

{%block content %}
<div class="container">
  <h1 class="heading">My Top 10 Movies</h1>
  <p class="description">These are my all time favourite movies.</p>

  {% for movie in movies %}
  <div class="card">
    <div class="front" style="background-image: url('{{movie.img_url}}');">
      <p class="large">{{ movie.ranking }}</p>
    </div>
    <div class="back">
      <div>
        <div class="title">
          {{movie.title}} <span class="release_date">({{movie.year}})</span>
        </div>
        <div class="rating">
          <label>{{movie.rating}}</label>
          <i class="fas fa-star star"></i>
        </div>
        <p class="review">"{{movie.review}}"</p>
        <p class="overview">{{movie.description}}</p>

        <a href="#" class="button">Update</a>
        <a href="#" class="button delete-button">Delete</a>
        <a href="{{ url_for('delete_movie', id=movie.id) }}" class="button delete-button">Delete</a>

      </div>
    </div>
  </div>
  {% endfor %}
</div>
<div class="container text-center add">
  <a href="#" class="button">Add Movie</a>
</div>

{% endblock %}
</body>
</html>
