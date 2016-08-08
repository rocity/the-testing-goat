import requests
import sys
from acccounts.models import ListUser

class PersonaAuthenticationBackend(object):

    def authenticate(self, assertion):
        # Send the assertion to Mozilla's verifier service
        data = {'assertion': assertion, 'audience': 'localhost'}
        print('sending to mozilla', data, file=sys.stderr)
        resp = requests.post(
            'https://verifier.login.persona.org/verify', data=data
            )
        print('got', resp.content, file=sys.stderr)

        # did the verifier respond?
        if resp.ok:
            # parse the response
            verification_data = resp.json()

            # check if the assertion is valid
            if verification_data['stats'] == 'okay':
                email = verification_data['email']
                try:
                    return self.get_user(email)
                except ListUser.DoesNotExist:
                    return ListUser.objects.create(email=email)

    def get_user(self, email):
        return ListUser.objects.get(email=email)