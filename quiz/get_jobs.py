import requests
from bs4 import BeautifulSoup


def get_jobs(**kwargs):
    print(kwargs)
    url = "https://www.jobkorea.co.kr/Search/?"

    params = {
        'stext': kwargs["keyword"],
        'careerType': kwargs["careerType"],
        "careerMin": kwargs["careerMin"],
        "careerMax": kwargs["careerMax"],
        "edu": kwargs["edu"],
        "cotype": kwargs["cotype"],
        "jobtype": kwargs["jobtype"],
        "payMin": kwargs["payMin"],
        "payMax": kwargs["payMax"],
        "Page_No": kwargs["Page_No"],
    }
    for p in params:
        if params[p] != "none":
            url += f"{p}={params[p]}&"
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    num_of_results = soup.find("strong", {
        "class": "dev_tot"
    }).string.replace(',', '')
    containers = soup.find_all("li", {"class": "list-post"})
    results = {"total": int(num_of_results), "data": []}
    for i in containers:
        try:
            options = ""
            etc = ""
            company = i.find("div", {
                "class": "post-list-corp"
            }).find("a").string
            info = i.find("div", {"class": "post-list-info"})
            title = info.find("a")['title']

            temp_options = info.find('p', {"class": "option"}).find_all("span")
            for option in temp_options:
                try:
                    if "short" not in option['class']:
                        options += (option.string) + "/"
                except:
                    options += (option.string) + "/"

            etcs = info.find('p', {"class": "etc"}).contents
            for ee in etcs:
                try:
                    etc += ee.string
                except:
                    etc += ee
            results["data"].append({
                "title": title,
                "company": company,
                "options": options[:-1],
                "etc": etc
            })
        except:
            pass

    print(url)
    return results