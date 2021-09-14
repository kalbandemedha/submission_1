Answers for the Part II in the task - 
1.	For this selenium + python test case, we need to use an ‘appium python client’ which is compatible with selenium v3 and v4 web-driver. The reason we could do this is because the appium communicates with the web-driver with the same protocols as selenium. In this appium python client, we need to configure the platform name (ex. Android, iOS), platform version and the app path. This is the link to the application running to be installed and tested on the targeted phone. 
In our current browser based test case we are using the selenium web-driver which will be replaced by appium based web-driver and we will be connecting to the appium server and perform the test cases with lines similar to current implementation. 

2.	In order to run appium on the targeted mobile, the mobile should be in developer mode. The appium server should be installed on the laptop running the test cases. Before starting any tests, appium server should be started and the displayed server address and the server port number should be verified with the one in the test. 

3.	The adaptions in the layouts should be considered. The xpaths changes would need to be considered as well, as it would be the hybrid android app.

4.	Unfortunately, I don’t know answer to this.
