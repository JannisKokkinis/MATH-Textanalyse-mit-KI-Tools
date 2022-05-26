import boto3
import json
from BasicSettings import *

comprehend = boto3.client(service_name='comprehend', region_name=awsregion)
text = content
print('Calling DetectSyntax')
print(json.dumps(comprehend.detect_syntax(Text=text, LanguageCode=lang), sort_keys=True,
indent=4))

print('End of DetectSyntax\n')