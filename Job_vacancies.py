class Vacancy():
    def __init__(self, accountant_vacancies, software_developer_vacancies, manager_vacancies, director_vacancies):

        #job_vacancy values added to their self.jab_vacancy
        self.accountant = accountant_vacancies
        self.software_developer = software_developer_vacancies
        self.manager = manager_vacancies
        self.director = director_vacancies

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
    def open_vacancies


vacancy = Vacancy(4, 2, 1, 3)
        