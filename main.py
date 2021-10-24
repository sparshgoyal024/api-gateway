
# [START endpoints_email_api_imports]
import endpoints
from endpoints import message_types
from endpoints import messages
from endpoints import remote
# [END endpoints_email_api_imports]

class EmailRequest(messages.Message):
    message = messages.StringField(1)


class EmailResponse(messages.Message):
    message = messages.StringField(1)


# [START endpoints_email_api_class]
@endpoints.api(name='email', version='v1')
class EmailApi(remote.Service):
    
    @endpoints.method(
        # This method takes an empty request body.
        message_types.VoidMessage,
        # This method returns an Email message.
        EmailResponse,
        path='get/email',
        http_method='GET',
        # Require auth tokens to have the following scopes to access this API.
        scopes=[endpoints.EMAIL_SCOPE],
        # OAuth2 audiences allowed in incoming tokens.
        audiences=['500140982586-hlo5gg22uaduqqd7f07csns5hg0brh85.apps.googleusercontent.com'],
        allowed_client_ids=['500140982586-hlo5gg22uaduqqd7f07csns5hg0brh85.apps.googleusercontent.com'])
    def get_user_email(self, request):
        user = endpoints.get_current_user()
        # If there's no user defined, the request was unauthenticated, so we
        # raise 401 Unauthorized.
        if not user:
            raise endpoints.UnauthorizedException
        return EmailResponse(message=user.email())
# [END endpoints_email_api_class]


# [START endpoints_api_server]
api = endpoints.api_server([EmailApi])
# [END endpoints_api_server]
