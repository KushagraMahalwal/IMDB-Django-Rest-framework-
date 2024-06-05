<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IMDB API Clone - README</title>
</head>
<body>
    <h1>IMDB API Clone</h1>
    <p>This project is an IMDB-like movie rating application developed using the Django Rest Framework. The focus is solely on backend development, providing robust functionalities for user authentication, movie CRUD operations, and rating submissions.</p>
    
    <h2>Features</h2>
    <ul>
        <li><strong>User Authentication</strong>: Implemented using JWT, allowing secure registration, login, and logout processes.</li>
        <li><strong>Movie CRUD Operations</strong>: Create, read, update, and delete movie entries seamlessly.</li>
        <li><strong>Rating Submissions</strong>: Users can rate movies, and the average rating is dynamically updated.</li>
        <li><strong>Database Management</strong>: Designed and optimized database models using Django ORM for storing movie information, user profiles, and ratings.</li>
        <li><strong>Admin Interface</strong>: Utilized Django's built-in admin interface for easy management of movie data and user accounts.</li>
    </ul>
    
    <h2>Requirements</h2>
    <p>To run this project, you need to have the following installed:</p>
    <ul>
        <li>Python (version 3.8 or higher)</li>
        <li>Django (version 3.2 or higher)</li>
        <li>Django Rest Framework</li>
        <li>Other dependencies listed in <code>requirements.txt</code></li>
    </ul>
    
    <h2>Setup Instructions</h2>
    <ol>
        <li><strong>Clone the Repository</strong>
            <pre><code>git clone https://github.com/your-username/IMDB-Django-Rest-framework.git
cd IMDB-Django-Rest-framework</code></pre>
        </li>
        <li><strong>Create a Virtual Environment</strong>
            <pre><code>python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`</code></pre>
        </li>
        <li><strong>Install Dependencies</strong>
            <pre><code>pip install -r requirements.txt</code></pre>
        </li>
        <li><strong>Apply Migrations</strong>
            <pre><code>python manage.py migrate</code></pre>
        </li>
        <li><strong>Run the Development Server</strong>
            <pre><code>python manage.py runserver</code></pre>
        </li>
        <li><strong>Access the Application</strong>
            <p>Open your web browser and navigate to <a href="http://127.0.0.1:8000/">http://127.0.0.1:8000/</a>.</p>
        </li>
    </ol>
    
    <h2>Project Structure</h2>
    <p>The project follows a standard Django project structure:</p>
    <pre><code>IMDB-Django-Rest-framework/
├── drf_project/
│   ├── watchmate/
│   │   ├── watchlist_app/
│   │   ├── watchmate/
│   │   ├── manage.py
├── requirements.txt
└── README.md</code></pre>
    
    <h2>API Endpoints</h2>
    <ul>
        <li><strong>User Authentication</strong>:
            <ul>
                <li><code>/api/register/</code> - Register a new user</li>
                <li><code>/api/login/</code> - Login an existing user</li>
                <li><code>/api/logout/</code> - Logout the current user</li>
            </ul>
        </li>
        <li><strong>Movie Management</strong>:
            <ul>
                <li><code>/api/movies/</code> - List all movies or create a new movie</li>
                <li><code>/api/movies/&lt;id&gt;/</code> - Retrieve, update, or delete a movie</li>
            </ul>
        </li>
        <li><strong>Rating Management</strong>:
            <ul>
                <li><code>/api/ratings/</code> - Submit a new rating</li>
                <li><code>/api/ratings/&lt;id&gt;/</code> - Retrieve, update, or delete a rating</li>
            </ul>
        </li>
    </ul>
    
    <h2>Contributing</h2>
    <p>Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.</p>
    
    <h2>License</h2>
    <p>This project is licensed under the MIT License. See the <code>LICENSE</code> file for more details.</p>
</body>
</html>
