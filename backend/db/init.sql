-- Create the table
CREATE TABLE job_listings (
    id SERIAL PRIMARY KEY,
    company_name VARCHAR(255),
    position VARCHAR(255),
    application_deadline DATE,
    date_posted DATE,
    number_of_positions INT,
    job_ad_link VARCHAR(255),
    location VARCHAR(100)
);

-- Insert data into the table
INSERT INTO job_listings (company_name, position, application_deadline, date_posted, number_of_positions, job_ad_link, location) VALUES
    ('Intility AS', 'IT-Utvikling', '2024-07-01', '2024-06-01', 3, 'https://techcorp.example.com/jobs/software-engineer', 'Oslo'),
    ('NRK AS', 'IT-Drift', '2024-07-15', '2024-06-05', 2, 'https://healthplus.example.com/careers/data-scientist', 'Oslo'),
    ('UDI', 'IT-Utvikling', '2024-06-30', '2024-05-20', 1, 'https://eduworld.example.com/jobs/curriculum-developer', 'Oslo'),
    ('FinanceWorks', 'IT-Drift', '2024-07-10', '2024-06-02', 1, 'https://financeworks.example.com/job/financial-analyst', 'Oslo'),
    ('Intility AS', 'IT-Utvikling', '2024-07-05', '2024-06-03', 4, 'https://retailpro.example.com/careers/store-manager', 'Oslo'),
    ('BioLife', 'IT-Drift', '2024-07-20', '2024-06-07', 2, 'https://biolife.example.com/jobs/lab-technician', 'Oslo'),
    ('GreenEnergy', 'IT-Utvikling', '2024-07-18', '2024-06-04', 1, 'https://greenenergy.example.com/jobs/project-manager', 'Oslo'),
    ('AutoTech', 'IT-Drift', '2024-07-25', '2024-06-06', 3, 'https://autotech.example.com/jobs/mechanical-engineer', 'Oslo'),
    ('Foodies', 'IT-Utvikling', '2024-07-22', '2024-06-08', 1, 'https://foodies.example.com/careers/head-chef', 'Oslo'),
    ('TravelCo', 'IT-Drift', '2024-07-12', '2024-06-05', 2, 'https://travelco.example.com/jobs/travel-consultant', 'Oslo');
