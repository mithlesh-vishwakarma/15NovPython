# Django REST Framework External API Integration (Session-5)

This Django REST Framework project implements 4 external API integration endpoints and includes complete test suites and Postman setup for **Session-5**.

---

## 🚀 Endpoints Summary

### 1. Music Weather Info
- **URL**: `GET /api/music-weather/<city>/`
- **Example**: `http://127.0.0.1:8000/api/music-weather/London/`
- **Description**: Uses OpenWeatherMap API to return weather temperature (°C), weather description, and music festival tips for outdoor stages.
- **Sample Response**:
  ```json
  {
    "city": "London",
    "temperature": 18.5,
    "temperature_unit": "°C",
    "description": "light rain",
    "festival_tip": "Pack a raincoat and boots for muddy festival grounds!",
    "source": "Simulated Weather Data (Set OPENWEATHER_API_KEY in .env for live API)"
  }
  ```

---

### 2. Food Location Geocoding
- **URL**: `GET /api/food-location/?name=<restaurant_name>`
- **Example**: `http://127.0.0.1:8000/api/food-location/?name=Hard%20Rock%20Cafe`
- **Description**: Uses Google Maps Geocoding API via the `requests` library to return latitude and longitude coordinates. Handles missing parameters (400) and unlocated restaurants (404).
- **Sample Response**:
  ```json
  {
    "restaurant": "Hard Rock Cafe",
    "latitude": 40.7589,
    "longitude": -73.9851,
    "formatted_address": "1501 Broadway, New York, NY 10036, USA",
    "status": "SUCCESS"
  }
  ```

---

### 3. Country Quick Facts
- **URL**: `GET /api/country-info/<country_name>/`
- **Example**: `http://127.0.0.1:8000/api/country-info/Japan/`
- **Description**: Uses REST Countries API to fetch and return country capital, population, region, and flag emoji.
- **Sample Response**:
  ```json
  {
    "country": "Japan",
    "capital": ["Tokyo"],
    "population": 125120000,
    "region": "Asia",
    "flag": "🇯🇵"
  }
  ```

---

### 4. GitHub User Repositories
- **URL**: `GET /api/github-repos/<username>/`
- **Example**: `http://127.0.0.1:8000/api/github-repos/torvalds/`
- **Description**: Adapted GitHub REST API logic returning total repository count and an array of public repository names as JSON.
- **Sample Response**:
  ```json
  {
    "username": "torvalds",
    "total_repos": 3,
    "repositories": [
      "linux",
      "pesconvert",
      "subsurface-divelog"
    ]
  }
  ```

---

## 🛠️ How to Run the Server

1. **Navigate to Session-5 folder**:
   ```bash
   cd "Session-5"
   ```

2. **Run Django Development Server**:
   ```bash
   python manage.py runserver
   ```

3. **Run Unit Tests**:
   ```bash
   python manage.py test api
   ```

---

## 📮 Postman & Postman AI Instructions (Task 5)

1. Open **Postman**.
2. Click **Import** and select `postman_collection.json` located inside `Session-5`.
3. Select **`1. Music Weather Info`** request (`GET http://127.0.0.1:8000/api/music-weather/London/`).
4. Click on the **Tests** tab.
5. Enter or ask Postman AI to generate the following test script:
   ```javascript
   pm.test("Status code is 200", function () {
       pm.response.to.have.status(200);
   });

   pm.test("Response contains temperature and description keys", function () {
       const responseJson = pm.response.json();
       pm.expect(responseJson).to.have.property('temperature');
       pm.expect(responseJson).to.have.property('description');
   });
   ```
6. Click **Send** to run the request and verify that the tests **PASS**.
