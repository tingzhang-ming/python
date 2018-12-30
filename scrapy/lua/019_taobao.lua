function main(splash)
    args = {
        url="https://s.taobao.com",
        wait=5,
        page=5
    }
    splash.images_enable = false
    assert(splash:go(args.url))
    assert(splash:wait(args.wait))
    input = splash:select("#q")
    input:send_text('iPad')
    submit = splash:select('#button.btn-search')
    submit:mouse_click()
    splash:wait(3)
    return {
        png = splash:png(),
        html = splash:html(),
    }
end