function main(splash, args)
  assert(splash:go('https://www.toutiao.com'))
  splash.scroll_position={y=400}
  return {
    png = splash:png()
  }
end

--#它会向下滚动400像素来获取图片