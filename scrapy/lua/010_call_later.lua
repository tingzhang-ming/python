function main(splash, args)
  local snapshots = {}
  local timer = splash:call_later(function()
    snapshots["a"] = splash:png()
    splash.scroll_position={y=500}
    splash:wait(1.0)
    snapshots["b"] = splash:png()
  end, 2)
  splash:go("https://www.toutiao.com")
  splash:wait(3.0)
  return snapshots
end