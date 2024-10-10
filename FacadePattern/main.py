from get_members import SQL_PROVIDER, ORACLE_PROVIDER
from get_members.facade_factory import FacadeFacory

# main can use SQL_PROVIDER, ORACLE_PROVIDER and return the records relevant for each

def main():
    facade = FacadeFacory.create_module(SQL_PROVIDER)
    facade.get_employees()

if __name__ == '__main__':
    main()