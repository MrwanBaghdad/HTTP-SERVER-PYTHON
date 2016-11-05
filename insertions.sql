INSERT INTO `publisher`(`Pub_ID`,`Name`, `Address`) VALUES (1,'Michael Jean','600 North Charles St.');
INSERT INTO `publisher`(`Pub_ID`,`Name`, `Address`) VALUES (2,'Jacob Fairbairn','799 E DRAGRAM SUITE 5A.');
INSERT INTO `publisher`(`Pub_ID`,`Name`, `Address`) VALUES (3,'John Allen','200 E MAIN ST.');
INSERT INTO `publisher`(`Pub_ID`,`Name`, `Address`) VALUES (4,'Michael Jean','300 BOYLSTON AVE E.');
INSERT INTO `publisher`(`Pub_ID`,`Name`, `Address`) VALUES (5,'Thomas Hardy','4150 Sydney Place.');

INSERT INTO `category`(`Category_ID`, `Name`) VALUES (1,'Computer Science');
INSERT INTO `category`(`Category_ID`, `Name`) VALUES (2,'Maths');
INSERT INTO `category`(`Category_ID`, `Name`) VALUES (3,'Biographies');
INSERT INTO `category`(`Category_ID`, `Name`) VALUES (4,'History');

INSERT INTO `book`(`Book_ID`, `Title`, `Price`, `Pub_ID`, `Category_ID`) VALUES (1,'Database',54,5,1);
INSERT INTO `book`(`Book_ID`, `Title`, `Price`, `Pub_ID`, `Category_ID`) VALUES (2,'Maths 3',25,1,2);
INSERT INTO `book`(`Book_ID`, `Title`, `Price`, `Pub_ID`, `Category_ID`) VALUES (3,'Networks',57,5,1);
INSERT INTO `book`(`Book_ID`, `Title`, `Price`, `Pub_ID`, `Category_ID`) VALUES (4,'Probabilities',46,5,2);
INSERT INTO `book`(`Book_ID`, `Title`, `Price`, `Pub_ID`, `Category_ID`) VALUES (5,'History of United Kingdom',46,3,4);
INSERT INTO `book`(`Book_ID`, `Title`, `Price`, `Pub_ID`, `Category_ID`) VALUES (6,'Steve Jobs Biography',34,4,3);
INSERT INTO `book`(`Book_ID`, `Title`, `Price`, `Pub_ID`, `Category_ID`) VALUES (7,'History of United States',18,3,4);
INSERT INTO `book`(`Book_ID`, `Title`, `Price`, `Pub_ID`, `Category_ID`) VALUES (8,'Programming',87,3,1);

INSERT INTO `member`(`Member_ID`, `Name`, `Address`, `Join_Date`) VALUES (1,'Jason','225 Elhorya st.','2014-12-02');
INSERT INTO `member`(`Member_ID`, `Name`, `Address`, `Join_Date`) VALUES (2,'Chris','110 Portsaid st.','2014-10-02');
INSERT INTO `member`(`Member_ID`, `Name`, `Address`, `Join_Date`) VALUES (3,'Jack','25 fawzy moaz st.','2014-2-22');
INSERT INTO `member`(`Member_ID`, `Name`, `Address`, `Join_Date`) VALUES (4,'Steve','15 Ahmed Kamha st.','2014-9-02');
INSERT INTO `member`(`Member_ID`, `Name`, `Address`, `Join_Date`) VALUES (5,'Robben','27 Moustafa kamel st.','2014-8-31');
INSERT INTO `member`(`Member_ID`, `Name`, `Address`, `Join_Date`) VALUES (6,'Kevin','5 Teba st.','2013-12-02');
INSERT INTO `member`(`Member_ID`, `Name`, `Address`, `Join_Date`) VALUES (7,'Adam','12 Alexander Ebrahim st.','2013-7-9');


INSERT INTO `borrowingbooks`(`Member_ID`, `Book_ID`, `Due_Date`, `Return_Date`) VALUES (1,1,'2014-12-02','2014-12-02');
INSERT INTO `borrowingbooks`(`Member_ID`, `Book_ID`, `Due_Date`, `Return_Date`) VALUES (2,1,'2014-10-02','2014-10-05');
INSERT INTO `borrowingbooks`(`Member_ID`, `Book_ID`, `Due_Date`, `Return_Date`) VALUES (4,2,'2014-11-02','2014-11-03');
INSERT INTO `borrowingbooks`(`Member_ID`, `Book_ID`, `Due_Date`, `Return_Date`) VALUES (3,1,'2014-10-26','2014-10-27');
INSERT INTO `borrowingbooks`(`Member_ID`, `Book_ID`, `Due_Date`, `Return_Date`) VALUES (7,3,'2014-10-7','2014-10-8');
INSERT INTO `borrowingbooks`(`Member_ID`, `Book_ID`, `Due_Date`, `Return_Date`) VALUES (5,1,'2014-10-26','2014-10-27');
INSERT INTO `borrowingbooks`(`Member_ID`, `Book_ID`, `Due_Date`, `Return_Date`) VALUES (6,5,'2014-10-7','2014-10-7');
INSERT INTO `borrowingbooks`(`Member_ID`, `Book_ID`, `Due_Date`, `Return_Date`) VALUES (7,1,'2014-09-7','2014-09-8');

