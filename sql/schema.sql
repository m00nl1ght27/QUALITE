CREATE TABLE clients (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nom VARCHAR(100) NOT NULL,
  prenom VARCHAR(100) NOT NULL,
  date_naissance DATE NOT NULL,
  adresse VARCHAR(255) NOT NULL,
  cp VARCHAR(10) NOT NULL,
  ville VARCHAR(100) NOT NULL
);
