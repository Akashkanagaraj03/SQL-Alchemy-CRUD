# Task2
SQL Alchemy with Postgres

**Assignment:** Movie Streaming Platform Database Using SQL-Alchemy

**Objective:**
You are tasked with creating a database system for a Movie Streaming Platform using SQL-Alchemy ORM in Python. The system should manage Users, Movies, and User Reviews.


**Requirements:**
**1. Design the Following Database Models:**
   
**User Table**
* id – Primary Key
* name – String (Not Null)
* email – String (Unique)

**Movie Table**
· id – Primary Key
· title – String (Not Null)
· genre – String
· release_year – Integer

**Review Table**
· id – Primary Key
· user_id – Foreign Key (references User.id)
· movie_id – Foreign Key (references Movie.id)
· rating – Integer (1 to 5)
· review_text – String


**2. Relationships:**
· One User can submit many Reviews.
· One Movie can have many Reviews.
· Each Review is written by one User for one Movie.


**3. Functional Requirements (Tasks to Perform in Code):**
   1. **Create** the database tables using SQL-Alchemy ORM.
   2. **Insert** sample data into the User, Movie, and Review tables.
   3. **Query:**
      * Fetch all reviews for a specific movie.
      * Fetch all movies reviewed by a specific user.
   4. **Update:** Update the rating of a review.
   5. **Delete:** Delete a specific review.
   6. **Use Transaction Handling:** Wrap inserts or updates inside try-except blocks to handle errors and rollback if needed.
