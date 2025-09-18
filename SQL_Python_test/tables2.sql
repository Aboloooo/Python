CREATE TABLE IF NOT EXISTS AccessLevel (
  AccessLevelID INT PRIMARY KEY,
  level VARCHAR(50)
);

INSERT INTO AccessLevel (AccessLevelID, level) VALUES (1, "Admin");
INSERT INTO AccessLevel (AccessLevelID, level) VALUES (2, "SecurityGuard");
INSERT INTO AccessLevel (AccessLevelID, level) VALUES (3, "Residence");

CREATE TABLE IF NOT EXISTS users (
    UserID INT PRIMARY KEY,
    First_name VARCHAR(255),
    Last_name VARCHAR(255),
    social_security_number BIGINT NOT NULL,
    Username VARCHAR(255) NOT NULL,
    Password VARCHAR(255) NOT NULL,
    Email VARCHAR(255) NOT NULL,
    AccessLevelID INT NOT NULL,
    status BOOLEAN,
    user_must_change_password BOOLEAN,
    FOREIGN KEY (AccessLevelID) REFERENCES AccessLevel(AccessLevelID)
);

CREATE TABLE IF NOT EXISTS Sites (
    SiteId INT PRIMARY KEY,
    SiteName VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS reservation (
    ReservationID INT PRIMARY KEY,
    Reserved_by_userID INT,
    StartMoment DATETIME,
    SiteId INT NOT NULL,
    FOREIGN KEY (Reserved_by_userID) REFERENCES users(UserID) ON DELETE CASCADE,
    FOREIGN KEY (SiteId) REFERENCES Sites(SiteId)
);

INSERT INTO Sites(SiteName) VALUES ("LilyUnden");
INSERT INTO Sites(SiteName) VALUES ("DonBosco");
