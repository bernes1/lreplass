CREATE TABLE job_listings (
    id SERIAL PRIMARY KEY,
    company_name VARCHAR(255),
    position VARCHAR(255),
    application_deadline DATE,
    date_posted DATE,
    number_of_positions INT,
    job_ad_link VARCHAR(255)
)