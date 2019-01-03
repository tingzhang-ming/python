function main(splash)
  splash:go("https://www.baidu.com/")
  input = splash:select("#kw")
  input:send_text('Splash')
  splash:wait(3)
  return {
    html = splash:html(),
    png = splash:png(),
    har = splash:har(),
  }
end