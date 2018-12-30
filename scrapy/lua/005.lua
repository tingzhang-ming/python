function main(splash, args)
  splash:go("https://www.toutiao.com")
  local ok reason = splash:wait(1)
  return {
    ok=ok,
    reason=reason
  }
end