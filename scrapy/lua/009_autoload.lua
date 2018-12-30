function main(splash, args)
  assert(splash:autoload("https://code.jquery.com/jquery-2.1.3.min.js"))
  assert(splash:go("https://www.taobao.com"))
  local version = splash:evaljs("$.fn.jquery")
  return 'JQuery version: ' .. version
end

--Splash Response: "JQuery version: 2.1.3"