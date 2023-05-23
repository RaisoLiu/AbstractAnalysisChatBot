from revChatGPT.V3 import Chatbot
from PyHackMD import API

class PaperAnalyzer:
    def __init__(self, chatgpt_api_token, hackmd_api_token):
        # 初始化chatbot與hackmdapi並設置查詢條件
        self.chatbot = Chatbot(api_key=chatgpt_api_token)
        self.hackmdapi = API(hackmd_api_token)
        self.queries = [
            {'query': '想解決的問題', 'lim': 'max 50 words', 'lang': '中文'},
            {'query': '使用的方法', 'lim': 'max 100 words', 'lang': '中文'},
            {'query': '最終的成果', 'lim': 'max 100 words', 'lang': '中文'},
            {'query': '關鍵字', 'lim': 'max 5 words', 'lang': '英文'}
        ]
        self.is_send_title_and_abstract = False
        self.title = ""
        self.abstract = ""
        self.answers = []
    
    def _generate_paper_description(self):
        # 產生論文的標題與摘要
        if not self.is_send_title_and_abstract:
            self.is_send_title_and_abstract = True
            return f"以下是一篇論文的標題與摘要。\n標題：{self.title}\n摘要：{self.abstract}\n"
        return ""
            
    def _get_answer(self, query):        
        # 根據查詢條件獲取答案
        for _ in range(5):
            pre_query = self._generate_paper_description() + f"請使用{query['lang']}回答問題。\n"
            query_string = f"{pre_query}{query['query']} ({query['lim']})"
            try:
                return self.chatbot.ask(query_string)
            except:
                pass
        return ""
    
    def _build_markdown(self):
        # 建立Markdown格式的論文分析
        markdown_header = '---\ntags: 論文分析\n---\n\n'
        markdown_title = f"# 論文分析：{self.title}\n\n"
        markdown_abstract = f"# 摘要：\n{self.abstract}\n\n"
        markdown_body = '\n'.join([f"# {query['query']}\n{answer}\n" for query, answer in zip(self.queries, self.answers)])
        return markdown_header + markdown_title + markdown_abstract + markdown_body
    
    def _create_hackmd_page(self, markdown):
        # 在hackmd上建立一個頁面，並返回該頁面的連結
        data = self.hackmdapi.create_note(content=markdown, write_permission='owner')
        return data['publishLink']
    
    def analyze_abstract(self, title, abstract):
        # 分析論文摘要，並返回hackmd頁面的連結
        self.title = title
        self.abstract = abstract
        self.answers = [self._get_answer(query) for query in self.queries]
        markdown = self._build_markdown()
        link = self._create_hackmd_page(markdown)
        return link