#!/usr/bin/python3
"""
Consuming and processing data from an API using Python.
"""
import requests
import csv


def fetch_and_print_posts():
    """
    Fetches posts from JSONPlaceholder and prints the titles.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    # Firewall bypass header
    headers = {'cfclearance': 'true'}
    
    try:
        response = requests.get(url, headers=headers)
        print("Status Code: {}".format(response.status_code))
        
        if response.status_code == 200:
            posts = response.json()
            for post in posts:
                print(post.get('title'))
    except Exception:
        pass


def fetch_and_save_posts():
    """
    Fetches posts and saves them into a CSV file.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    headers = {'cfclearance': 'true'}
    
    try:
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            posts = response.json()
            # Structure the data
            structured_data = [
                {'id': p.get('id'), 'title': p.get('title'), 'body': p.get('body')}
                for p in posts
            ]
            
            # Write to CSV
            with open('posts.csv', 'w', encoding='utf-8', newline='') as f:
                fieldnames = ['id', 'title', 'body']
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(structured_data)
    except Exception:
        pass
