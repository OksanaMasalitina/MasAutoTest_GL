#### Kурсовий проект, створений в рамках навчання на курсі 
### "Тестувальник QA Auto" 
###### від GlobalLogic та Prometheus

Проект написаний мовою Python з використанням платформи Pytest та містить практичні завдання з автоматизації тестування, зокрема з тестування API, баз даних та ui тестування. 
Проект має індивідуальні творчі завдання, виконані з використанням інформації з додаткових джерел, а також обов'язкові завдання з відповідних тем, зроблені під час навчання на курсі. 
#   
##### Структура проекту:
1. modules
	- api/clients
		- [github.py](https://github.com/OksanaMasalitina/MasAutoTest_GL/blob/main/modules/api/clients/github.py "github.py"): API-клієнт та методи для запитів до відкритого API GitHub 
	- common
		- [database.py](https://github.com/OksanaMasalitina/MasAutoTest_GL/blob/main/modules/common/database.py "database.py"): методи для підключення до DB (SQLite), SQL-запитів до бази даних - розширення бази даних та отримання інформації з неї
	- ui/page_objects
		- [base_page.py](https://github.com/OksanaMasalitina/MasAutoTest_GL/blob/main/modules/ui/page_objects/base_page.py "base_page.py"):
		- [sign_in_page.py](https://github.com/OksanaMasalitina/MasAutoTest_GL/blob/main/modules/ui/page_objects/sign_in_page.py "sign_in_page.py"): 
2. tests
	- api
		- [test_github_api.py](https://github.com/OksanaMasalitina/MasAutoTest_GL/blob/main/tests/api/test_github_api.py "test_github_api.py"): тести відкритого API GitHub з використанням методів, описаних у [github.py](https://github.com/OksanaMasalitina/MasAutoTest_GL/blob/main/modules/api/clients/github.py "github.py") та фікстур з [conftest.py](https://github.com/OksanaMasalitina/MasAutoTest_GL/blob/main/conftest.py "conftest.py")
		- [test_http.py](https://github.com/OksanaMasalitina/MasAutoTest_GL/blob/main/tests/api/test_http.py "test_http.py"): тести HTTP запитів до GitHub
		- [test_fixtures.py](https://github.com/OksanaMasalitina/MasAutoTest_GL/blob/main/tests/api/test_fixtures.py "test_fixtures.py"): перші тести з використанням фікстур 
	- database
		- [test_database.py](https://github.com/OksanaMasalitina/MasAutoTest_GL/blob/main/tests/database/test_database.py "test_database.py"): тестування розширеної бази даних на основі методів з [database.py](https://github.com/OksanaMasalitina/MasAutoTest_GL/blob/main/modules/common/database.py "database.py")
	- ui
		- [test_ui.py](https://github.com/OksanaMasalitina/MasAutoTest_GL/blob/main/tests/ui/test_ui.py "test_ui.py"): тести user interface (Selenium), тестування флоу по пошуку товару, додаванню його в кошик та переходу на чекаут
		- [test_ui_page_object.py](https://github.com/OksanaMasalitina/MasAutoTest_GL/blob/main/tests/ui/test_ui_page_object.py "test_ui_page_object.py"): 
3. [conftest.py](https://github.com/OksanaMasalitina/MasAutoTest_GL/blob/main/conftest.py "conftest.py"): фікстури, які використовуються в тестах 
4. [pytest.ini](https://github.com/OksanaMasalitina/MasAutoTest_GL/blob/main/pytest.ini "pytest.ini"): мітки груп тестів для організації та управління процесом тестування 