import GenrateAnalytics

AccessToken=""
GroupId = ""

# this graph api may change
request_url = "https://graph.facebook.com/"+GroupId+"/feed?&access_token="+AccessToken

GenrateAnalytics.installProxy('','','202.141.80.19','3128')
users = GenrateAnalytics.populateData(request_url,"time_logs",AccessToken)
GenrateAnalytics.dumpData("",users)
