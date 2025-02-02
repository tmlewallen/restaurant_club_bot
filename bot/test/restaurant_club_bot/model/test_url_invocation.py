import json
from unittest import TestCase

from restaurant_club_bot.model.url_invocation import UrlInvocation


JSON = """
{
  "version": "2.0",
  "routeKey": "$default",
  "rawPath": "/my/path",
  "rawQueryString": "parameter1=value1&parameter1=value2&parameter2=value",
  "cookies": [
    "cookie1",
    "cookie2"
  ],
  "headers": {
    "header1": "value1",
    "header2": "value1,value2"
  },
  "queryStringParameters": {
    "parameter1": "value1,value2",
    "parameter2": "value"
  },
  "requestContext": {
    "accountId": "123456789012",
    "apiId": "<urlid>",
    "authentication": null,
    "authorizer": {
        "iam": {
                "accessKey": "AKIA...",
                "accountId": "111122223333",
                "callerId": "AIDA...",
                "cognitoIdentity": null,
                "principalOrgId": null,
                "userArn": "arn:aws:iam::111122223333:user/example-user",
                "userId": "AIDA..."
        }
    },
    "domainName": "<url-id>.lambda-url.us-west-2.on.aws",
    "domainPrefix": "<url-id>",
    "http": {
      "method": "POST",
      "path": "/my/path",
      "protocol": "HTTP/1.1",
      "sourceIp": "123.123.123.123",
      "userAgent": "agent"
    },
    "requestId": "id",
    "routeKey": "$default",
    "stage": "$default",
    "time": "12/Mar/2020:19:03:58 +0000",
    "timeEpoch": 1583348638390
  },
  "body": "Hello from client!",
  "pathParameters": null,
  "isBase64Encoded": false,
  "stageVariables": null
}
"""


class TestUrlInvocation(TestCase):

    def test_url_invocation_parses_from_json_str(self):
        url_invocation: UrlInvocation = UrlInvocation.from_json(JSON)
        self.assert_url_invocation_matches_values(url_invocation)

    def test_url_invocation_parses_from_dict(self):
        json_dict = json.loads(JSON)
        url_invocation: UrlInvocation = UrlInvocation.from_dict(json_dict)
        self.assert_url_invocation_matches_values(url_invocation)

    def assert_url_invocation_matches_values(self, url_invocation: UrlInvocation):
        self.assertEqual("Hello from client!", url_invocation.body)
        self.assertDictEqual(
            {"header1": "value1", "header2": "value1,value2"}, url_invocation.headers
        )
        self.assertDictEqual(
            {"parameter1": "value1,value2", "parameter2": "value"},
            url_invocation.query_string_parameters,
        )
        self.assertFalse(url_invocation.is_base_64_encoded)
        self.assertEqual("POST", url_invocation.request_context.http.method)
        self.assertEqual("/my/path", url_invocation.request_context.http.path)
        self.assertEqual("HTTP/1.1", url_invocation.request_context.http.protocol)
        self.assertEqual(
            "123.123.123.123", url_invocation.request_context.http.source_ip
        )
        self.assertEqual("agent", url_invocation.request_context.http.user_agent)
