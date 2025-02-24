class Question_data():
    '''
        Данные из JSON файла
    '''
    id_question:int
    question:str
    answers:list
    right_answers:list
    choosen_var:list = []
    answer_result:bool = False

    def __init__(self, id_question, data):
        self.id_question = id_question
        self.answers = data["answers"]
        self.right_answers = data["right_answers"]
        self.question = data["question"]
        if 'choosen_var' in data:
            self.choosen_var = data['choosen_var']
