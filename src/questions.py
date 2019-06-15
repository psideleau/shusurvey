class Question:
    def __init__(self, prompt, choices):
          self.prompt = prompt
          self.choices = choices

    def ask(self):
        return '''
            {}<br />
           {} 
        '''.format(self.prompt, self.get_options())

    def get_options(self):
        output = []
        for choice in self.choices:
            output.append('<input type="radio" name="choice" value="{}">{}<br />'.format(choice, choice))

        return ''.join(output)
            

questions = [
    Question('What is your favorite type of food?', ['Asian', 'Italian', 'American', 'British']),
    Question('Where in the world would you want to travel to?', ['South Korea', 'England', 'Japan', 'Germany']),
    Question('What dog would you want?', ['Yorkie', 'Husky', 'Australian Shepherd', 'I want a cat']),
    Question('What is your favorite sport to watch?', ['Football', 'Soccer', 'Tennis', 'Tae Kwon Do']),
    Question('What type of music do you like?', ['Rock and Roll', 'Country', 'K-Pop', 'Classical', 'Post Rock']),
]
