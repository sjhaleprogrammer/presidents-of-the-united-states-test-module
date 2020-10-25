import pytest
import requests

r = requests.get("http://api.duckduckgo.com/?q=presidents of the united states&format=json")

list = ["George Washington","John Adams",
"Thomas Jefferson","James Madison","James Monroe","John Quincy Adams","Andrew Jackson","Martin Van Buren",
"Martin Van Buren", "William Henry Harrison","John Tyler","James K. Polk","Zachary Taylor","Millard Fillmore",
"Millard Fillmore", "Franklin Pierce","James Buchanan","Abraham Lincoln","Andrew Johnson","Ulysses S. Grant",
"Rutherford B. Hayes","James Garfield","Chester A. Arthur","Grover Cleveland","Benjamin Harrison","Grover Cleveland",
"William McKinley","Theodore Roosevelt","William Howard Taft","Woodrow Wilson","Warren G. Harding","Calvin Coolidge",
"Herbert Hoover","Franklin D. Roosevelt","Harry S. Truman","Dwight D. Eisenhower","John F. Kennedy","Lyndon B. Johnson",
"Richard M. Nixon", "Gerald R. Ford", "James Carter","Ronald Reagan","George H. W. Bush","William J. Clinton","George W. Bush",
"Barack Obama","Donald J. Trump"]


def test_presidents():
    assert (list in r.text) == True
        
    
    