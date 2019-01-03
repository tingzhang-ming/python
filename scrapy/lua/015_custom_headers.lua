function main(splash)
  splash:set_custom_headers({
     ["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36",
     ["Site"] = "httpbin.org",
  })
  splash:go("http://httpbin.org/get")
  return splash:html()
end