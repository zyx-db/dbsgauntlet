import requests

class graphqlClient:
    def __init__(self):
        self.endpoint = 'https://leetcode.com/graphql/'

    def _get_random_problem(self, difficulty, tags):
        graphql_endpoint = 'https://leetcode.com/graphql/'
        query = '''
            query randomQuestion($categorySlug: String, $filters: QuestionListFilterInput) {
              randomQuestion(categorySlug: $categorySlug, filters: $filters) {
                titleSlug
              }
            }
'''

        variables = {
                'categorySlug': 'all-code-essentials'
                }
        if difficulty and len(tags) > 0:
            variables['filters'] = {
                    'difficulty': difficulty,
                    'tags': tags
                    }
        elif difficulty:
            variables['filters'] = {
                    'difficulty': difficulty
                    }
        elif len(tags) > 0:
            variables['filters'] = {
                    'tags': tags
                    }
        else:
            variables['filters'] = {}

        response = requests.post(graphql_endpoint, json={'query': query, 'variables': variables})
        if 'errors' in response.json().keys():
            return None
        return response.json()['data']['randomQuestion']['titleSlug']

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
        status = response
        if 'errors' in response.json().keys():
            return ''
        return response.json()['data']['question']['status']

    def get_match_problem(self, cookie_a, cookie_b, difficulty, tags):
        while True:
            possible = self._get_random_problem(difficulty, tags)

            # we need a problem neither contest has solved
            status_a = self.get_problem_status(possible, cookie_a)
            # status_b = self.get_problem_status(possible, cookie_b)

            if status_a != 'ac' :# and status_b != 'ac':
                return possible
