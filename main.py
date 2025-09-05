from application import salary
from application.db import people
from datetime import datetime
import pygame as pg

# Инициализация Pygame
class Window:
    def __init__(self, employee_name, employee_salary):
        pg.init()
        self.employee_name = employee_name
        self.employee_salary = employee_salary
        self.width, self.height = 800, 600
        self.screen = pg.display.set_mode((self.width, self.height))
        pg.display.set_caption("Информация о сотруднике")
        self.run()

    def run(self):
        # Цвета
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        BLUE = (0, 120, 215)
        GREEN = (0, 128, 0)
        DARK_GRAY = (64, 64, 64)

        # Загрузка шрифта
        try:
            font_large = pg.font.Font(None, 48)
            font_medium = pg.font.Font(None, 36)
        except:
            font_large = pg.font.SysFont("Arial", 48)
            font_medium = pg.font.SysFont("Arial", 36)

        # Основной цикл
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        running = False

            # Получение текущей даты и времени
            current_datetime = datetime.now()
            date_str = current_datetime.strftime("%d.%m.%Y")
            time_str = current_datetime.strftime("%H:%M:%S")

            # Очистка экрана
            self.screen.fill(WHITE)

            # Рендеринг текста
            employee_text = font_medium.render(f"Сотрудник: {self.employee_name}", True, BLUE)
            salary_text = font_medium.render(f"Зарплата: {self.employee_salary}$", True, GREEN)
            date_text = font_large.render(date_str, True, BLACK)
            time_text = font_medium.render(time_str, True, DARK_GRAY)

            # Позиционирование текста
            self.screen.blit(employee_text, (50, 50))
            self.screen.blit(salary_text, (50, 100))
            self.screen.blit(date_text, (self.width//2 - date_text.get_width()//2, self.height//2 - 50))
            self.screen.blit(time_text, (self.width//2 - time_text.get_width()//2, self.height//2 + 10))

            # Обновление экрана
            pg.display.flip()

            # Небольшая задержка
            pg.time.delay(100)

        # Завершение работы
        pg.quit()


if __name__ == '__main__':
    employee_name = people.get_employees("Олег")
    employee_salary = salary.calculate_salary(777)
    print(datetime.now())
    window = Window(employee_name=employee_name, employee_salary=employee_salary)