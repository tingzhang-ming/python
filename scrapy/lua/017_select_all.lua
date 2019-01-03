function main(splash)
  local treat = require('treat')
  assert(splash:go("https://www.zhihu.com"))
  assert(splash:wait(1))
  local texts = splash:select_all('.ContentLayout-mainColumn .ContentItem-title')
  local results = {}
  for index, text in ipairs(texts) do
    results[index] = text.node.textContent
  end
  return treat.as_array(results)
end