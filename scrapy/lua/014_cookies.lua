function main(splash)
    splash:add_cookie{"sessionid", "237465ghgfsd", "/", domain="http://example.com"}
    splash:go("http://example.com/")
    return splash:get_cookies()
end

--Splash Response: Array[1]
--0: Object
--domain: "http://example.com"
--httpOnly: false
--name: "sessionid"
--path: "/"
--secure: false
--value: "237465ghgfsd"