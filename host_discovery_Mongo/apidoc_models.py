from flask_restx import Api, fields


class ApiModels:

    host_fields = None
    hosts_response = None

    @staticmethod
    def set_api_models(api: Api):

        ApiModels.host_fields = api.model(
            "Host Fields",
            {
                "ip_address": fields.String(example="192.168.254.14"),
                "mac_address": fields.String(example="00:27:02:15:5c:d5"),
                "hostname": fields.String(example="RokuStreamingStick.home"),
                "last_heard": fields.String(example="2021-04-19 14:42:15.185"),
                "availability": fields.String(example="true"),
                "response_time": fields.String(example="0.005"),
                "open_tcp_ports": fields.String(example="[22, 80]")
            },
        )
        ApiModels.hosts_response = api.model(
            "Hosts Response",
            {
                "hostname": fields.Nested(ApiModels.host_fields)
            }
        )
