from ..models import SpamAnalysisResult
from ..models import MailosaurException

class AnalysisOperations(object):
    """AnalysisOperations operations.
    """

    def __init__(self, session, base_url):
        self.session = session
        self.base_url = base_url

    def spam(self, email):
        """Perform a spam test.

        Perform spam testing on the specified email.

        :param email: The identifier of the email to be analyzed.
        :type email: str        
        :return: SpamAnalysisResult
        :rtype: ~mailosaur.models.SpamAnalysisResult
        :raises:
         :class:`MailosaurException<mailosaur.models.MailosaurException>`
        """
        url = "%sapi/analysis/spam/%s" % (self.base_url, email)
        response = self.session.get(url)
        
        if response.status_code not in [200]:
            raise MailosaurException(response)

        data = response.json()

        return SpamAnalysisResult(data)
