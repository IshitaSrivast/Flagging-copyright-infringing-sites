# Flagging-copyright-infringing-site


This is a decentralized application for detecting the copyright infringement on the OTT platforms/websites. It mainly comprises of two componenets:
# A) Ethereum-based reference records:
This consisted of the time-stamped records of the Broadcasters, OTT, etc., platforms with permission to broadcast the digital media as fed in by the producers.The CID
was then stored on the Ethereum along with the web address of the permitted broadcasters.The perceptual served as the tool to compare and find matches within media from 
different sources. Also, the copyright permissions are indexed and can be queried through the address. 
# B) Web Crawler: 
The web crawler visited all the sites that appeared on the browser results and scraped through them. Then the system extracted the image of the website
using the PUPPETEER. OCR was employed to detect the download instructions on the website and flag them. The seed URL were the top browsing results of searches like 
"Movie_name"+"download" or "Movie_name"+"D0wnl0ad" or "Movie_name"+"free stream" and so on. HTML parser was used to extract the redirect links and the crawler then
navigated through them to perform OCR after taking images of the website.

![image](https://user-images.githubusercontent.com/99870284/217743333-ceb8d996-dd67-4492-8e1a-b64c89800da7.png)

