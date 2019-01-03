function main(splash, args)
  local get_div_count = splash:jsfunc([[
  function () {
    var body = document.body;
    var divs = body.getElementsByTagName('div');
    return divs.length;
  }
  ]])
  splash:go("https://www.baidu.com")
  return ("There are %s DIVs"):format(
    get_div_count())
end

--Splash Response: "There are 22 DIVs"