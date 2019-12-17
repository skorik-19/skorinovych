import requests
import json
import logging
import time

logging.basicConfig(
    filename="server.log",
    filemode='a',
    level=logging.INFO,
    format='{levelname} {asctime} {name} : {message}',
    style='{'
)
log = logging.getLogger(__name__)


def main(url):
		try:
			r = requests.get(url)
			r.raise_for_status()
		except HTTPError as http_err:
			logging.error("HTTP помилка: %s", http_err)
		except Exception as err:
			logging.error("Інша помилка: %s", err)
		else:
			if r.status_code == 200:
				logging.info("======================================")
				logging.info("Сервер доступний. Статуст код = %s", r.status_code)
				data = json.loads(r.content)
				logging.info("Сервер доступний. Час на сервері: %s", data['date'])
				logging.info("======================================")
				logging.info("Запитувана сторінка: : %s", data['current_page'])
				logging.info("Сервер: %s", data['server_info'])
				logging.info("Кієнт: %s", data['client_info'])
			elif r.status_code == 404:
				logging.warn("Cторінку не знайдено %s", r.status_code)
			else:
				logging.error("Сервер недоступний!!!")


if __name__ == '__main__':
	main("http://localhost:8000/health")
