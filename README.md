# image-scrap-from-amazon
This is about scrapping watch images from amazon search result page with their tags. The URL used here to scrap the images is https://www.amazon.in/s/ref=sr_in_-2_p_89_14?fst=as%3Aoff&rh=k%3Awatches%2Cn%3A1350387031%2Cp_89%3AFossil&bbn=1350387031&keywords=watches&ie=UTF8&qid=1517909003&rnid=3837712031


## Python Requirements
Use pip install for the installtion.
* selenium
* pandas
* BeautifulSoup
* urlretrieve
* csv


#### How to Run
* Download the Selenium webdriver from https://www.seleniumhq.org/projects/webdriver/ for a particular web browser, here Chrome is been used.
* Give the path of the driver in the "driver" section.
* Create a folder to download the images and give the path for same in image download section.
* Run the fossil_watches.py file
* The images will be downloaded into the specified path.


#### Notes
This also creates a CSV File containing the URLs of the images with their tags, fossil_with_tags.csv is the sample CSV File.
