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
        if not self.open_accountant_vacancies():
            return False
        self.accountant_appliers.append(name)
        return True

    def add_software_developer_appliers(self, name):
        if not self.open_software_developer_vacancies():
            return False
        self.software_developer_appliers.append(name)
        return True

    def add_manager_appliers(self, name):
        if not self.open_manager_vacancies():
            return False
        self.manager_appliers.append(name)
        return True

    def add_director_appliers(self, name):
        if not self.opne_director_vacancies():
            return False
        self.director_appliers.append(name)
        return True


    #how many vacancies left in jobs
    


vacancy = Vacancy(4, 2, 1, 3)
        