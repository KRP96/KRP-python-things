class Vacancy():
    def __init__(self, accountant_vacancy, software_developer_vacancy, manager_vacancy, director_vacancy):
        self.accountant = accountant_vacancy
        self.software_developer = software_developer_vacancy
        self.manager = manager_vacancy
        self.director = director_vacancy
        self.accountant_appliers = []
        self.software_developer_appliers = []
        self.manager_appliers = []
        self.director_appliers = []

    def add_accountant_appliers(self, name):
        self.accountant_appliers.append(name)


vacancy = Vacancy(4, 2, 1, 3)
        