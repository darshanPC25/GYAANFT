from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['zingguru']  # Using the database name from the original setup

# Sample data for collections
sample_data = {
    'User': [
        {'username': 'john_doe', 'email': 'john@example.com', 'role': 'student'},
        {'username': 'jane_smith', 'email': 'jane@example.com', 'role': 'teacher'}
    ],
    'Playlist': [
        {'title': 'Python Basics', 'description': 'Introduction to Python programming'},
        {'title': 'Web Development', 'description': 'HTML, CSS, and JavaScript fundamentals'}
    ],
    'Book': [
        {'title': 'Learning Python', 'author': 'Mark Lutz'},
        {'title': 'Clean Code', 'author': 'Robert C. Martin'}
    ],
    'CareerPath': [
        {
            'title': 'Full Stack Developer',
            'description': 'Path to become a full stack developer',
            'skills': ['HTML', 'CSS', 'JavaScript', 'Python', 'Database'],
            'category': 'Web Development'
        },
        {
            'title': 'Data Scientist',
            'description': 'Path to become a data scientist',
            'skills': ['Python', 'Statistics', 'Machine Learning', 'Data Analysis'],
            'category': 'Data Science'
        },
        {
            'title': 'Blockchain Developer',
            'description': 'Path to become a blockchain developer',
            'skills': ['Solidity', 'JavaScript', 'Blockchain', 'Smart Contracts'],
            'category': 'Blockchain'
        }
    ],
    'CareerAssessment': [
        {
            'question_number': 1,
            'question': 'What are your key interests?',
            'options': [
                {'text': 'Blockchain', 'category': 'Blockchain'},
                {'text': 'Web Development', 'category': 'Web Development'},
                {'text': 'Data Analysis', 'category': 'Data Science'},
                {'text': 'Mobile Development', 'category': 'Mobile Development'}
            ]
        },
        {
            'question_number': 2,
            'question': 'What type of work environment do you prefer?',
            'options': [
                {'text': 'Startup', 'category': 'Startup'},
                {'text': 'Corporate', 'category': 'Corporate'},
                {'text': 'Freelance', 'category': 'Freelance'},
                {'text': 'Research', 'category': 'Research'}
            ]
        }
    ],
    'Question': [
        {'question': 'What is Python?', 'answer': 'Python is a high-level programming language.'},
        {'question': 'What is HTML?', 'answer': 'HTML is a markup language for creating web pages.'}
    ],
    'Other': [
        {'type': 'article', 'title': 'Getting Started with MongoDB'},
        {'type': 'resource', 'title': 'Python Documentation'}
    ]
}

def setup_collections():
    try:
        # Drop existing collections
        for collection_name in db.list_collection_names():
            db[collection_name].drop()
        
        # Create collections and insert sample data
        for collection_name, data in sample_data.items():
            collection = db[collection_name]
            if data:  # Only insert if there's data
                collection.insert_many(data)
            
            # Verify the collection was created and data was inserted
            print(f"Created collection '{collection_name}' with {collection.count_documents({})} documents")
            
    except Exception as e:
        print(f"Error setting up MongoDB collections: {str(e)}")

if __name__ == "__main__":
    setup_collections() 