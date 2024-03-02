import requests

class graphqlClient:
    def __init__(self):
        self.endpoint = 'https://leetcode.com/graphql/'

    def _get_random_problem(self):
        # graphql_endpoint = 'https://leetcode.com/graphql/'
        # query = '''
        #     query randomQuestion($categorySlug: String, $filters: QuestionListFilterInput) {
        #       randomQuestion(categorySlug: $categorySlug, filters: $filters) {
        #         titleSlug
        #       }
        #     }
# '''
        # variables = {
        #         'categorySlug': 'all-code-essentials',
        #         'filters': {
        #             'difficulty': 'MEDIUM',
        #             'tags': ['array']
        #             }
        #         }
        # response = requests.post(graphql_endpoint, json={'query': query, 'variables': variables})
        # if response.status_code == 200:
        #     return jsonify(response.json())
        # else:
        #     return jsonify({'error': 'Failed to fetch GraphQL data'}), response.status_code
        return "two-sum"

    def get_problem_status(self, problem_title, cookie):
        query = '''
            query userQuestionStatus($titleSlug: String!) {
              question(titleSlug: $titleSlug) {
                status
              }
            }
        '''
        variables = {'titleSlug': problem_title}
        response =  requests.post(self.endpoint, json={'query': query, 'variables': variables}, cookies=cookie)
        #TODO parse out AC, etc
        status = response
        return status

    def get_match_problem(self, cookie_a, cookie_b):
        while True:
            possible = self._get_random_problem()

            # we need a problem neither contest has solved
            status_a = self.get_problem_status(possible, cookie_a)
            status_b = self.get_problem_status(possible, cookie_b)

            if status_a != 'ac' and status_b != 'ac':
                return possible
