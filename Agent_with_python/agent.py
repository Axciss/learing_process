class Agent:
    def __init__(self, client, llm, system: str = "") -> None:
        self.client = client
        self.system = system
        self.llm = llm
        self.messages: list = []
        if self.system:
            self.messages.append({"role": "system", "content": system})

    def __call__(self, message=""):
        if message:
            self.messages.append({"role": "user", "content": message})
        result = self.execute()
        self.messages.append({"role": "assistant", "content": result})
        return result

    def execute(self):
        completion = self.client.chat.completions.create(
            model=self.llm, messages=self.messages
        )
        return completion.choices[0].message.content