CREATE TABLE visits (
    id INT AUTO_INCREMENT PRIMARY KEY,
    visitor_name VARCHAR(25) NOT NULL,
    visit_datetime DATETIME DEFAULT NOW() NOT NULL
) 