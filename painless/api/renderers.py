from rest_framework.renderers import JSONRenderer
from rest_framework.utils.serializer_helpers import ReturnList


class DataStatusMessage_Renderer(JSONRenderer):

    def render(self, data, accepted_media_type=None, renderer_context=None):

        status_code = renderer_context['response'].status_code
        response = dict()

        # import pdb ; pdb.set_trace()
        if str(status_code).startswith('2'):
            response['detail'] = None

            results_sign = data.get('results', {})
            if type(results_sign) == ReturnList:
                response['results'] = data['results']
                response['count'] = data['count']
                response['next'] = data['next']
                response['previous'] = data['previous']
            else:
                response['results'] = data

        elif str(status_code).startswith('4'):
            response = data

        elif str(status_code).startswith('5'):
            response['detail'] = "Server Error"
            response['data'] = None

        else:
            response['detail'] = "Message do not handle correctly."
            response['data'] = data

        return super(DataStatusMessage_Renderer, self).render(response, accepted_media_type, renderer_context)
