# WEB-SCRAPER

*COMPANY*: HEX SOFTWARES

NAME*: TANVI NILESH DHULE

*DOMAIN*: PYTHON PROGRAMMING

*DURATION*: 4 WEEKS

*MENTOR*: KAPTAN

*DESCRIPTION*: 
Project Title: Web Scraper for Quotes using Python

This project involves the development of a *web scraper using Python* to extract quotes and author names from a practice website: [http://quotes.toscrape.com](http://quotes.toscrape.com). The purpose of the project is to demonstrate how web scraping techniques can be used to collect structured data from websites and store it in a usable format such as CSV. The scraper uses popular Python libraries like requests and BeautifulSoup to handle the task.
Web scraping is a technique used to automate the process of collecting data from websites. In this project(http://quotes.toscrape.com), the scraper targets the main page of the Quotes to Scrape website, which displays multiple famous quotes along with their respective authors. This website is specifically designed for practicing and learning web scraping, making it a safe and appropriate choice for educational purposes.

The process starts by sending an HTTP GET request to the URL http://quotes.toscrape.com. Once the response is received, the HTML content of the page is parsed using BeautifulSoup, a library that makes it easy to navigate, search, and extract data from HTML documents. The scraper identifies all the HTML elements that contain quotes and author names using class selectors.
Each quote is contained within a <div> element with the class "quote". Inside each of these containers, the actual quote text is found in a <span> with class "text", and the author name is in a <small> tag with the class "author". The program loops through all these elements, extracts the required information, and writes it into a CSV file.
To ensure compatibility with programs like Microsoft Excel, the CSV file is saved using the utf-8-sig encoding. This prevents common character encoding issues such as the appearance of strange symbols in place of quotation marks or accented characters. The output file, quotes.csv, contains two columns: one for the quote and another for the author.

Here is an example of how the output is structured:

| Quote                                                             | Author          |
| ----------------------------------------------------------------- | --------------- |
| “The world as we have created it is a process of our thinking...” | Albert Einstein |

This project demonstrates a real-world application of web scraping and basic file handling. It also shows the importance of understanding HTML structure, using the correct encodings for data storage, and presenting data in a clean, readable format. The script also includes basic error handling using HTTP response status codes to verify that the page was successfully retrieved before proceeding.

Potential future improvements to the project include scraping multiple pages using pagination, extracting tags associated with each quote, and exporting the data into other formats such as JSON or PDF. A graphical interface (GUI) could also be added using libraries like Tkinter for a more user-friendly experience.
Overall, this project successfully illustrates how Python can be used to automate data collection from websites and is a strong example of applying programming skills to a practical task

EXAMPLE
*OUTPUT*
![Image](https://github.com/user-attachments/assets/d777c83d-1e3e-4641-be4f-8e9b95ecce99)
