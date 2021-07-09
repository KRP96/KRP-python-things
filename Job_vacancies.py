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
        if not self.open_director_vacancies():
            return False
        self.director_appliers.append(name)
        return True


    #how many vacancies left in jobs
    def open_accountant_vacancies(self):
        return self.accountant - len(self.accountant_appliers)

    def open_software_developer_vacancies(self):
        return self.software_developer - len(self.software_developer_appliers)

    def open_manager_vacancies(self):
        return self.manager - len(self.manager_appliers)

    def open_director_vacancies(self):
        return self.director - len(self.director_appliers)


vacancy = Vacancy(4, 2, 1, 3)

accountant_appliers = ["Name1", "Name2", "Name3", "Name4","Name5", "Name6"]
for applier in accountant_appliers:
    if vacancy.add_accountant_appliers(applier):
        print(f"{applier}, you pass the interview.")
    else:
        print(f"{applier}, you fail the interview. Good luck for your future.")


software_developer_appliers = ["Name7", "Name8", "Name9", "Name10", "Name11"]
for applier in software_developer_appliers:
    if vacancy.add_software_developer_appliers(applier):
        print(f"{applier}, you pass the interview.")
    else:
        print(f"{applier}, you fail the interview. Good luck for your future.")

manager_appliers = ["Name12", "Name13", "Name14", "Name15", "Name16"]
for applier in manager_appliers:
    if vacancy.add_manager_appliers(applier):
        print(f"{applier}, you pass the interview.")
    else:
        print(f"{applier}, you fail the interview. Good luck for your future.")

director_appliers = ["Name17", "Name18", "Name19", "Name20"]   
for applier in director_appliers:
    if vacancy.add_director_appliers(applier):
        print(f"{applier}, you pass the interview.")
    else:
        print(f"{applier}, you fail the interview. Good luck for your future.")

