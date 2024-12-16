# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 260_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 1141 bytes
import dnslib

def create_dns_query(domain):
    q = dnslib.DNSRecord.question(domain)
    return q.pack()


def simulate_dns_response(query_id):
    response = dnslib.DNSRecord.answer(q=(dnslib.DNSRecord.parse(create_dns_query("example.com"))),
      a=dnslib.RR(rname="example.com.",
      rtype="A",
      rdata="192.0.2.1",
      ttl=60))
    response.header.id = query_id + 1
    return response.pack()


if __name__ == "__main__":
    domain = "example.com"
    query_id = 12345
    dns_query = create_dns_query(domain)
    print("Sending DNS query...")
    dns_response = simulate_dns_response(query_id)
    print("Received DNS response with mismatched ID.")

# okay decompiling 260_1.pyc
