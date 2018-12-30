function main(splash, args)
assert(splash:go("https://www.baidu.com"))
assert(splash:wait(0.5))
local title = splash:evaljs("document.title")
return {
title = title
}
end

--    Success
    --- -Splash Response: Object
    ----title: "百度一下，你就知道"