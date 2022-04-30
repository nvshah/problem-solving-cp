# https://leetcode.com/problems/unique-email-addresses/

import re
from typing import List

# def funCleanEmail(email):
#     email = email.replace('.', '')
#     regex = r"^([a-z]+)(?:\+[a-z]*)?@([a-z]+)([a-z]+)$"
#     subst = r"\1\2\3"

#     result = re.sub(regex, subst, email)
#     print(result)
#     return result

# def numUniqueEmails(emails: List[str]) -> int:
#     ans = set(map(funCleanEmail, emails))
#     print(ans)
#     return len(ans)


def numUniqueEmails(emails: List[str]) -> int:
    s = {}
    for e in emails:
        local, domain = e.split('@')  # seperate local & domain
        local = local.split('+')[0]  # Get local before `+`
        local = local.replace('.', '') # ignore all `.` in {local}
        s.add((local, domain))

    return len(s)




emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
print(numUniqueEmails(emails))