import subprocess

if __name__ == '__main__':

    rs = subprocess.run('cd .. ; behave --no-capture -f allure_behave.formatter:AllureFormatter -o reports/allure ; allure serve reports/allure', shell=True)

