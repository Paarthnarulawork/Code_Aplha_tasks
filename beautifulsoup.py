from bs4 import BeautifulSoup
   
with open("file2.html","r") as f:
    html = f.read()
    
    soup = BeautifulSoup(html,'html.parser')
    
    # print(soup.pretify())
    # print(soup.title)
    # # print(soup.title.name)
    # print(soup.title.text)
    #print(soup.find_all('a'))
    print(soup.get_text())
    #sample_output
"""
#All products | Books to Scrape - Sandbox
# Books to Scrape We love being scraped!
Home
All products
 Books
Travel
Mystery
Historical Fiction
Sequential Art
Classics
Philosophy
                                Romance
                                Womens Fiction
                    Fiction
                    Childrens
                                                Religion
                            Nonfiction
                            Music
                
                                Default
                                Science Fiction
                                Sports and Games

                                Add a comment

                                Fantasy
 
                                New Adult

                                Young Adult
  
                                Science

                                Poetry

                                Paranormal

                                Art

                                Psychology
                                Autobiography
                                Parenting
                                Adult Fiction
                                Humor
                                Horro
                                History
                                Food and Drink
                                Christian Fiction
                                Business
                                Biography
                                Thriller
                                Contemporary
                                                            Spirituality
                                Academic
                                Self Help
                                Historical            
                            Christian
                                        Suspense
                            Short Stories
                        Novels
                            Health
                                Politics
                                Cultural
                                    Erotica
                                Crime
                        All products
1000 results - showing 1 to 20.
                Warning! This is a demo website for web scraping purposes. Prices and ratings here were randomly assigned and have no real meaning.
A Light in the ...
£51.77
    In stock
    Add to basket
Tipping the Velvet
£53.74
    In stock
    Add to basket
Soumission
£50.10
    In stock
    Add to basket
Sharp Objects
£47.82
    In stock
    Add to basket
Sapiens: A Brief History ...
£54.23
    In stock
    Add to basket
The Requiem Red
£22.65
In stock
    Add to basket
The Dirty Little Secrets ...
£33.34
    In stock
    Add to basket
The Coming Woman: A ...
£17.93
    In stock
    Add to basket
The Boys in the ...
£22.60
    In stock
    Add to basket
The Black Maria
£52.15
    In stock
    Add to basket
Starving Hearts (Triangular Trade ...
£13.99
        In stock
Add to basket
Shakespeare's Sonnets
£20.66
    In stock
    Add to basket
Set Me Free
£17.46
In stock
Add to basket
Scott Pilgrim's Precious Little ...
£52.29
    In stock
    Add to basket
Rip it Up and ...
£35.02
    In stock
    Add to basket
Our Band Could Be ...
£57.25
    In stock
    Add to basket
Olio
£23.88
    In stock
    Add to basket
Mesaerion: The Best Science ...
£37.59
    In stock
    Add to basket
Libertarianism for Beginners
£51.33
In stockAdd to basket
It's Only the Himalayas
£45.17
In stock
    Add to basket
Page 1 of 50
                next"""























