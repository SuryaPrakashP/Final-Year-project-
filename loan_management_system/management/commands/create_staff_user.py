{% extends 'base.html' %}
{% load static %}

{% block css_block %}
<style>
    /* Ensure the image covers the entire screen */
    .background-image {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100vh; /* Set the height to 100vh for full viewport height */
        object-fit: cover; /* Ensure the image covers the entire container */
        z-index: -1; /* Send the image behind other content */
        opacity: 0.6; /* Adjust the opacity for a slight fade effect */
    }

    /* Center align and style the buttons */
    .button-container {
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        text-align: center;
    }

    .button-container a {
        text-decoration: none;
    }

    .btn {
        padding: 10px 20px;
        font-size: 18px;
        margin: 0 10px;
        background-color: #000000; /* Change background color to black */
        color: #ffffff; /* Set text color to white */
        border: none; /* Remove border */
        border-radius: 5px; /* Add border radius */
        cursor: pointer;
    }

    /* Footer */
    footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #343a40; /* Dark background color */
        color: #ffffff; /* White text color */
        text-align: center;
    }
</style>
{% endblock %}

{% block body_block %}
{% include 'navbar.html' %}

<!-- Full-page background image -->
<img src="{% static 'images/img.jpg' %}" class="background-image" alt="Background Image">

<!-- Button container -->
<!-- Button container -->
<div class="button-container">
    <a href="/loan/loan-request/">
        <button type="button" class="btn btn-info btn-rounded m-2" style="color: black; padding: 10px 20px; font-size: 17px;">Apply Loan</button>
    </a>
    <span>or</span>
    <a href="/account/signup-customer/">
        <button type="button" class="btn btn-info btn-rounded m-2" style="color: black; padding: 10px 20px; font-size: 17px;">Register</button>
    </a>
</div>


{% include "footer.html" %}
{% endblock %}
