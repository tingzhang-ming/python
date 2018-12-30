function main(splash, args)
  splash:go("https://www.baidu.com")
  splash:runjs("foo = function() { return 'bar' }")
  local result = splash:evaljs("foo()")
  return result
end

--Splash Response: "bar"