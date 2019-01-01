function main(splash)
  splash:go("https://account.geekbang.org/signin")
  input = splash:select(".nw-input")
  input:send_text('15201439529')

  input2 = splash:select(".input-wrap > input:nth-child(1)")
  input2:send_text('qq77aa88')
  submit = splash:select('.mybtn')
  submit:mouse_click()
  splash:wait(3)
  return splash:png()
end

