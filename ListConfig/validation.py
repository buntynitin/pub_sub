from marshmallow import Schema, fields


class ListConfigSchema(Schema):
    """ /list_config - POST

    Parameters:
     - topic_name (str)
     - key (str)
     - data (str)
    """

    topic_name = fields.Str(required=True)
    key = fields.Str(required=True)
    data = fields.Str(required=True)
