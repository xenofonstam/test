def apply_template(jp):
    image="![enter image description here](https://secureops.com/wp-content/uploads/2018/06/logo-2.png)"
    templ= ""
    switcher = {
        "Malicious-Get-Request": image+"""\n\n\nOn {0} the alert {1} was triggered after the {2} request was logged towards {3} with return code {4}\n\n\n
        Event Details:
        time:{0}
        Rule Name: {1}
        Method: {2}
        Request: {3}""".format(jp.get("timestamp"),jp.get("rule_name"),jp.get("verb"),jp.get("referrer"),jp.get("response")),

        "Brute-force": image+"""\n\n\nOn {0} the alert {1} was triggered after the IP {2} generated traffic towards the destination {3} in {4} unique ports\n\n\n
        Event Details:
        time:{0}
        Rule Name: {1}
        Source IP:{2}
        Count: {3}""".format(jp.get("timestamp"),jp.get("rule_name"),jp.get("src_ip"),jp.get("dst_ip"),jp.get("count")),
        }
    templ=switcher.get(jp.get("rule_name"),"No template found")
    return templ
