from app.py import json_data as jp

image="![enter image description here](https://secureops1.com/wp-content/uploads/2018/06/logo-2.png)"

switcher = {
    "Brute-force": image+"""\n\n\nOn {0} the alert {1} was triggered after the {2} request was logged towards {3} with return code {4}\n\n\n
Event Details:
{0}
{1}
{2}
{3}""".format(jp.get("timestamp"),jp.get("rule_name"),jp.get("verb"),jp.get("referrer"),jp.get("response"))),
  
    "Port-scan": image+"""\n\n\nOn {0} the alert {1} was triggered after the IP {2} generated traffic towards the destination {3} in {4} unique ports\n\n\n
Event Details:
{0}
{1}
{2}
{3}""".format(jp.get("timestamp"),jp.get("rule_name"),jp.get("src_ip"),jp.get("dst_ip"),jp.get("count"))),
    }


