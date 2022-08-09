"""
Handler with takes in multipart form data as request input, and json as output. 
"""

from .base import BaseEnvelope
import json
from itertools import chain
from base64 import b64decode

class GcloudEnvelope(BaseEnvelope):
    """
    Implementation. Captures batches in raw, returns in JSON format.
    """

    def parse_input(self, data):
        return data

    def format_output(self, data):
        return [self._to_json(data)]

    def _to_json(self, output):
        """
        Converts the output of the model back into compatible JSON
        """
        out_dict = {
            'predictions': output
        }
        return json.dumps(out_dict)
