from search_engine.lda.search_engine import LdaEngine
from search_engine.tfidf.search_engine import TfidfEngine
from search_engine.doc2vec.search_engine import D2VEngine


class AggregateSearch(object):

    def __init__(self, *engines):
        self.engines = engines

    def search(self, query):
        dict_results = [engine.dict_search(query, results=50) for engine in self.engines]
        results = dict_results[0].keys()

        weighted_results = [(url, self.weighted_res(url, dict_results)) for url in results]
        return sorted(weighted_results, key=lambda x: -x[1])

    def weighted_res(self, url, dict_results):
        return sum([res[url] for res in dict_results if url in res]) / len(self.engines)


if __name__ == '__main__':

    search = AggregateSearch(LdaEngine.with_loaded_model(), TfidfEngine.with_loaded_model(),
                             D2VEngine.with_loaded_model())

    inp = ""

    while inp != 'q':
        inp = input("Enter query: ")
        print(search.search(inp)[:3])
