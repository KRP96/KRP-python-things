class Vacancy():
    def __init__(self, accountant_vacancy, software_developer_vacancy, manager_vacancy, director_vacancy):

        #job_vacancy values added to their self.jab_vacancy
        self.accountant = accountant_vacancy
        self.software_developer = software_developer_vacancy
        self.manager = manager_vacancy
        self.director = director_vacancy

        #create lists for appliers' names
        self.accountant_appliers = []
        self.software_developer_appliers = []
        self.manager_appliers = []
        self.director_appliers = []

    #create add appliers functions
    def add_accountant_appliers(self, name):
        self.accountant_appliers.append(name)

    def add_software_developer_appliers(self, name):
        self.software_developer_appliers.append(name)

    def add_manager_appliers(self, name):
        self.manager_appliers.append(name)

    def add_director_appliers(self, name):
        self.director_appliers.append(name)


    #how many vacancies left in jobs


vacancy = Vacancy(4, 2, 1, 3)
        