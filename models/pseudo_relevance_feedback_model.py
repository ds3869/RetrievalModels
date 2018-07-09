class PseudoRelevanceFeedbackModel(object):
    """Pseudo relevance feedback
    The general algorithm is:

    1. Retrieve the top k documents using one of the above retrieval models.
    2. Identify terms in these documents which are distinctive to the documents.
    3. Add the terms to the query, and re-run the retrieval process. Return the final results.
    """
    k = 0

    def query(self, keywords):
        results = search(keywords)
        """
        """
    def __init__(self, k = 10):
        self.k = k
