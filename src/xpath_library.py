# possible cookie page after login
#Allow all Cookies, Accept All
#possible save info page for login
# not now


XPATHS = {}
#known locations
XPATHS["login-page"] = {
    "username-form" : "//input[@name='username']",
    "password-form" : "//input[@name='password']",
    "cookie-policy-text" : "//div[contains(text(),'We use cookies to help personalize content, ')]",
    "cookie-policy-link" : "//div/a[contains(@href,'/legal/cookies')]",
    "cookie-policy-accept" : "//button[contains(text(),'Accept')]",
    "html-class-login-page" : "//*[contains(@class, 'not-logged-in')]",
    "get-instagram-app" : "//*[contains(text(), 'Get Instagram App')]",
    "login-button" : "//*[contains(text(),'Log In')]",
    "save-login" : "//div[contains(text(), 'Save Your')]",
    "not-now" : "//div/*[contains(text(), 'Not Now')]"
}

XPATHS["feed-page"] = {
    "get-posts" : "//main/section//article",
    "post-link" : "//div/div/a/time/parent::a",
    "post-time" : "//div/div/a/time", 
    "post-owner" : "//header/div/a",   #href
    "post-images" : "//img[not(@data-testid='user-avatar')]" #href
}

XPATHS["comment-page"] = {
    "comment-form" : "//div/form/textarea",
    "back-btn" : "//div/a[@href = '/']" #might also select the home btn but it doesnt matter 
}