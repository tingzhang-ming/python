function main(splash, args)
  splash:autoload([[
    function get_document_title(){
      return document.title;
    }
  ]])
  splash:go("https://www.baidu.com")
  return splash:evaljs("get_document_title()")
end

--Splash Response: "百度一下，你就知道"