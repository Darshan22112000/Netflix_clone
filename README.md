# Netflix Clone

## Project Overview

This project is a **Netflix Clone** application that mimics the core functionalities of the Netflix platform. The app provides movie and TV show recommendations based on content similarity. The frontend is built using **Angular**, while the backend is powered by **FastAPI** in Python and **PostgreSQL** for the database.

## Features

- **User Interface**: Developed using Angular for a responsive and user-friendly experience.
- **Backend API**: FastAPI for handling requests and managing data flow.
- **Database**: PostgreSQL is used to store and manage movie and TV show data.
- **Recommendation Engine**: Machine learning model based on **TF-IDF** and **cosine similarity** to provide personalized recommendations.

## Tech Stack

### Frontend
- **Angular**: Handles UI and client-side logic.
  
### Backend
- **FastAPI**: Manages API endpoints for data retrieval and interaction.
- **PostgreSQL**: Stores movie and TV show information.

### Machine Learning
- **Python**: Used to develop the recommendation engine.
- **Sklearn**: Utilized for TF-IDF and cosine similarity.
- **Pandas & Numpy**: Data manipulation and transformation.
- **NLTK**: For text preprocessing (lemmatization, stopword removal).
- **Joblib**: Model persistence for saving and loading machine learning models.

## How the Recommendation System Works

1. **Data Collection**: TV shows and movies are fetched from the database (could be extended to external sources like TMDB).
2. **Text Preprocessing**: Movie and TV show overviews are processed by:
   - Lowercasing
   - Removing non-alphanumeric characters
   - Lemmatization
   - Stopword removal using **NLTK**.
3. **Keywords**: Movie keywords are fetched asynchronously from the TMDB API to enhance the content description.
4. **Feature Extraction**: TF-IDF vectorization is used to convert textual content (overview + keywords) into numerical features.
5. **Cosine Similarity**: A cosine similarity matrix is computed to determine the similarity between different pieces of content.
6. **Model Saving**: The vectorizer and cosine similarity matrix are saved using **Joblib** for quick reloading in future API calls.

## Setup and Installation

### Prerequisites
- **Angular CLI**: To run the frontend.
- **Python 3.8+**: For the backend.
- **PostgreSQL**: For the database.
- **FastAPI**: For creating the backend API.
  
### Installation Steps

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Darshan22112000/Netflix_clone.git
    ```

2. **Frontend Setup (Angular)**:
    - Navigate to the `frontend` folder and install dependencies:
      ```bash
      cd frontend
      npm install
      ```
    - Run the Angular development server:
      ```bash
      ng serve
      ```

3. **Backend Setup (FastAPI)**:
    - Navigate to the `backend` folder and create a virtual environment:
      ```bash
      cd backend
      python -m venv venv
      source venv/bin/activate  # For Linux/MacOS
      venv\Scripts\activate  # For Windows
      ```
    - Install required Python packages:
      ```bash
      pip install -r requirements.txt
      ```
    - Start the FastAPI server:
      ```bash
      uvicorn main:app --reload
      ```

4. **Database Setup (PostgreSQL)**:
    - Create a PostgreSQL database and configure the connection settings in `backend/config.py`.

5. **Run the Application**:
    - Access the frontend at `http://localhost:4200/`.
    - Access the backend at `http://localhost:8000/`.

## Machine Learning Model

The recommendation system is based on a **content-based filtering** approach, using the movie's and TV show's metadata.

### Key Components:

1. **Text Preprocessing**:
   - Movie and TV show overviews are preprocessed to remove unwanted characters and extract meaningful tokens using NLTK.
   
2. **TF-IDF**:
   - The **TfidfVectorizer** from Scikit-learn is used to convert text into numerical vectors.
   
3. **Cosine Similarity**:
   - The **cosine similarity** between content vectors is calculated to find the most similar content.

4. **Asynchronous Keyword Fetching**:
   - The `aiohttp` library is used to asynchronously fetch keywords from the **TMDB API** to improve the content description.

### Model Training

The machine learning code for training the recommendation model is located in `backend/ml_models.py`. Here’s an outline:

- **Preprocessing**: The `preprocess_text` function cleans and prepares movie descriptions.
- **TF-IDF**: The text is transformed into TF-IDF features.
- **Cosine Similarity**: Calculates the similarity between different content based on the text features.
- **Model Persistence**: The trained models (TF-IDF vectorizer, cosine similarity matrix) are saved for reuse using **Joblib**.

To retrain the models:
```bash
python backend/app/train.py
```

## Contributing

Feel free to fork the project and submit pull requests for enhancements or bug fixes.

## License

This project is licensed under the MIT License.

---

Feel free to contact me for any questions or collaboration requests.
