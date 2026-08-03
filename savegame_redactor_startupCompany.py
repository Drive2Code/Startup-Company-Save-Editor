import json
import os
import shutil
import sys
import tkinter as tk
from tkinter import ttk, messagebox, filedialog

# ---------- ФУНКЦИЯ ДЛЯ ПУТЕЙ К РЕСУРСАМ ----------
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)

# ---------- УСТАНОВКА ИКОНКИ ----------
def set_window_icon(window, icon_name='icon2.ico'):
    icon_path = resource_path(icon_name)
    if os.path.exists(icon_path):
        try:
            window.iconbitmap(icon_path)
        except:
            pass
        try:
            from PIL import Image, ImageTk
            img = Image.open(icon_path)
            photo = ImageTk.PhotoImage(img)
            window.iconphoto(True, photo)
            setattr(window, '_icon_photo', photo)
        except:
            pass

# ---------- ЛОКАЛИЗАЦИЯ ----------
LANG = {
    'ru': {
        'app_title': "Редактор сохранений",
        'no_file': "Файл не загружен. Нажмите '📂 Открыть файл' для выбора.",
        'open_file': "📂 Открыть файл",
        'save': "💾 Сохранить",
        'refresh': "🔄 Обновить",
        'balance': "💰 Баланс",
        'research': "🔬 Очки исследований",
        'apply': "Применить",
        'copy': "📋 Копировать",
        'paste': "📝 Вставить",
        'salary': "Зарплата:",
        'set': "Установить",
        'change_percent': "Изменить на %:",
        'percent': "%",
        'speed': "Скорость:",
        'set_all': "Установить всем",
        'mood': "Настроение:",
        'set_mood': "Установить настроение",
        'mood_range_error': "Настроение должно быть от 1 до 100.",
        'employees_tab': "👥 Сотрудники",
        'inventory_tab': "📦 Инвентарь",
        'transactions_tab': "💰 Транзакции",
        'general_tab': "📊 Общее",
        'plan': "План:",
        'search': "🔍 Поиск:",
        'bulk_change': "Изменить все для колонки:",
        'bulk_apply': "Применить ко всем",
        'value': "Значение:",
        'paste_not_supported': "Вставка в транзакции не поддерживается.",
        'schedule_edit': "Для редактирования графика используйте двойной клик.",
        'select_cell': "Сначала выберите ячейку (кликните по ней).",
        'no_number': "Буфер обмена не содержит числа.",
        'employee_not_found': "Сотрудник не найден.",
        'enter_number': "Введите число.",
        'enter_integer': "Введите целое число.",
        'file_loaded_title': "Файл загружен",
        'file_loaded': "Файл '{filename}' загружен.",
        'file_saved_title': "Сохранено",
        'file_saved': "Файл сохранён.\nРезервная копия: {backup}",
        'save_first': "Сначала загрузите файл.",
        'error': "Ошибка",
        'load_error': "Не удалось загрузить файл:\n{error}",
        'file_not_found': "Файл не найден.",
        'schedule_editor': "Редактирование графика",
        'start_hour': "Начало (час):",
        'end_hour': "Конец (час):",
        'days_off': "Выходные дни:",
        'schedule_updated': "График обновлён.",
        'schedule_save': "Сохранить",
        'cancel': "Отмена",
        'no_plan_edit': "Выберите конкретный план для редактирования.",
        'bulk_plan_error': "Нельзя изменить план для режима 'Все компоненты (склад)'. Выберите конкретный план.",
        'bulk_done_title': "Готово",
        'bulk_done_body': "Для всех компонентов установлено {value} в колонке '{col}'.",
        'bulk_success_title': "Готово",
        'bulk_success_body': "{action} для {count} сотрудников/кандидатов.",
        'plan_not_found': "План не найден.",
        'enter_valid_number': "Введите число.",
        'date': "Дата",
        'version': "Версия",
        'employees_count': "Сотрудников",
        'transactions_count': "Транзакций",
        'all_components': "Все компоненты (склад)",
        'switch_lang': "🌐 English",
        'donate': "🙏 Поддержать",
        'donate_title': "Поддержать автора",
        'donate_text': "Если вам понравилась программа и вы хотите сказать спасибо, вы можете отправить любую сумму на один из следующих кошельков. Спасибо! ❤️",
        'copy_address': "📋 Копировать",
        'copied': "Скопировано!",
        'close': "Закрыть",
        'col_id': "ID",
        'col_name': "Имя",
        'col_position': "Должность",
        'col_schedule': "График",
        'col_speed': "Скорость",
        'col_max': "Макс",
        'col_salary': "Зарплата",
        'col_mood': "Настроение",
        'col_component': "Компонент",
        'col_plan': "План",
        'col_warehouse': "Склад",
        'col_day': "День",
        'col_hour': "Час",
        'col_amount': "Сумма",
        'col_description': "Описание"
    },
    'en': {
        'app_title': "Save Editor",
        'no_file': "No file loaded. Click '📂 Open File' to select.",
        'open_file': "📂 Open File",
        'save': "💾 Save",
        'refresh': "🔄 Refresh",
        'balance': "💰 Balance",
        'research': "🔬 Research Points",
        'apply': "Apply",
        'copy': "📋 Copy",
        'paste': "📝 Paste",
        'salary': "Salary:",
        'set': "Set",
        'change_percent': "Change by %:",
        'percent': "%",
        'speed': "Speed:",
        'set_all': "Set all",
        'mood': "Mood:",
        'set_mood': "Set mood",
        'mood_range_error': "Mood must be between 1 and 100.",
        'employees_tab': "👥 Employees",
        'inventory_tab': "📦 Inventory",
        'transactions_tab': "💰 Transactions",
        'general_tab': "📊 General",
        'plan': "Plan:",
        'search': "🔍 Search:",
        'bulk_change': "Change all in column:",
        'bulk_apply': "Apply to all",
        'value': "Value:",
        'paste_not_supported': "Pasting into transactions is not supported.",
        'schedule_edit': "Double-click to edit schedule.",
        'select_cell': "Select a cell first (click on it).",
        'no_number': "Clipboard does not contain a number.",
        'employee_not_found': "Employee not found.",
        'enter_number': "Enter a number.",
        'enter_integer': "Enter an integer.",
        'file_loaded_title': "File loaded",
        'file_loaded': "File '{filename}' loaded.",
        'file_saved_title': "Saved",
        'file_saved': "File saved.\nBackup: {backup}",
        'save_first': "Load a file first.",
        'error': "Error",
        'load_error': "Failed to load file:\n{error}",
        'file_not_found': "File not found.",
        'schedule_editor': "Edit Schedule",
        'start_hour': "Start (hour):",
        'end_hour': "End (hour):",
        'days_off': "Days off:",
        'schedule_updated': "Schedule updated.",
        'schedule_save': "Save",
        'cancel': "Cancel",
        'no_plan_edit': "Select a specific plan to edit.",
        'bulk_plan_error': "Cannot edit plan in 'All components (warehouse)' mode. Select a specific plan.",
        'bulk_done_title': "Done",
        'bulk_done_body': "Set {value} in column '{col}' for all components.",
        'bulk_success_title': "Done",
        'bulk_success_body': "{action} for {count} employees/candidates.",
        'plan_not_found': "Plan not found.",
        'enter_valid_number': "Enter a valid number.",
        'date': "Date",
        'version': "Version",
        'employees_count': "Employees",
        'transactions_count': "Transactions",
        'all_components': "All components (warehouse)",
        'switch_lang': "🌐 Русский",
        'donate': "🙏 Donate",
        'donate_title': "Support the author",
        'donate_text': "If you like the program and want to say thank you, you can send any amount to one of the following wallets. Thank you! ❤️",
        'copy_address': "📋 Copy",
        'copied': "Copied!",
        'close': "Close",
        'col_id': "ID",
        'col_name': "Name",
        'col_position': "Position",
        'col_schedule': "Schedule",
        'col_speed': "Speed",
        'col_max': "Max",
        'col_salary': "Salary",
        'col_mood': "Mood",
        'col_component': "Component",
        'col_plan': "Plan",
        'col_warehouse': "Warehouse",
        'col_day': "Day",
        'col_hour': "Hour",
        'col_amount': "Amount",
        'col_description': "Description"
    },
    'uk': {
        'app_title': "Редактор збережень",
        'no_file': "Файл не завантажено. Натисніть '📂 Відкрити файл' для вибору.",
        'open_file': "📂 Відкрити файл",
        'save': "💾 Зберегти",
        'refresh': "🔄 Оновити",
        'balance': "💰 Баланс",
        'research': "🔬 Очки досліджень",
        'apply': "Застосувати",
        'copy': "📋 Копіювати",
        'paste': "📝 Вставити",
        'salary': "Зарплата:",
        'set': "Встановити",
        'change_percent': "Змінити на %:",
        'percent': "%",
        'speed': "Швидкість:",
        'set_all': "Встановити всім",
        'mood': "Настрій:",
        'set_mood': "Встановити настрій",
        'mood_range_error': "Настрій має бути від 1 до 100.",
        'employees_tab': "👥 Співробітники",
        'inventory_tab': "📦 Інвентар",
        'transactions_tab': "💰 Транзакції",
        'general_tab': "📊 Загальне",
        'plan': "План:",
        'search': "🔍 Пошук:",
        'bulk_change': "Змінити всі в колонці:",
        'bulk_apply': "Застосувати до всіх",
        'value': "Значення:",
        'paste_not_supported': "Вставка в транзакції не підтримується.",
        'schedule_edit': "Для редагування графіка використовуйте подвійний клік.",
        'select_cell': "Спочатку виберіть комірку (клацніть по ній).",
        'no_number': "Буфер обміну не містить числа.",
        'employee_not_found': "Співробітника не знайдено.",
        'enter_number': "Введіть число.",
        'enter_integer': "Введіть ціле число.",
        'file_loaded_title': "Файл завантажено",
        'file_loaded': "Файл '{filename}' завантажено.",
        'file_saved_title': "Збережено",
        'file_saved': "Файл збережено.\nРезервна копія: {backup}",
        'save_first': "Спочатку завантажте файл.",
        'error': "Помилка",
        'load_error': "Не вдалося завантажити файл:\n{error}",
        'file_not_found': "Файл не знайдено.",
        'schedule_editor': "Редагування графіка",
        'start_hour': "Початок (година):",
        'end_hour': "Кінець (година):",
        'days_off': "Вихідні дні:",
        'schedule_updated': "Графік оновлено.",
        'schedule_save': "Зберегти",
        'cancel': "Скасувати",
        'no_plan_edit': "Виберіть конкретний план для редагування.",
        'bulk_plan_error': "Не можна змінити план у режимі 'Всі компоненти (склад)'. Виберіть конкретний план.",
        'bulk_done_title': "Готово",
        'bulk_done_body': "Для всіх компонентів встановлено {value} в колонці '{col}'.",
        'bulk_success_title': "Готово",
        'bulk_success_body': "{action} для {count} співробітників/кандидатів.",
        'plan_not_found': "План не знайдено.",
        'enter_valid_number': "Введіть число.",
        'date': "Дата",
        'version': "Версія",
        'employees_count': "Співробітників",
        'transactions_count': "Транзакцій",
        'all_components': "Всі компоненти (склад)",
        'switch_lang': "🌐 English",
        'donate': "🙏 Підтримати",
        'donate_title': "Підтримати автора",
        'donate_text': "Якщо вам сподобалася програма і ви хочете сказати спасибі, ви можете надіслати будь-яку суму на один із наступних гаманців. Дякую! ❤️",
        'copy_address': "📋 Копіювати",
        'copied': "Скопійовано!",
        'close': "Закрити",
        'col_id': "ID",
        'col_name': "Ім'я",
        'col_position': "Посада",
        'col_schedule': "Графік",
        'col_speed': "Швидкість",
        'col_max': "Макс",
        'col_salary': "Зарплата",
        'col_mood': "Настрій",
        'col_component': "Компонент",
        'col_plan': "План",
        'col_warehouse': "Склад",
        'col_day': "День",
        'col_hour': "Година",
        'col_amount': "Сума",
        'col_description': "Опис"
    },
    'fr': {
        'app_title': "Éditeur de sauvegarde",
        'no_file': "Aucun fichier chargé. Cliquez sur '📂 Ouvrir un fichier' pour sélectionner.",
        'open_file': "📂 Ouvrir un fichier",
        'save': "💾 Sauvegarder",
        'refresh': "🔄 Actualiser",
        'balance': "💰 Solde",
        'research': "🔬 Points de recherche",
        'apply': "Appliquer",
        'copy': "📋 Copier",
        'paste': "📝 Coller",
        'salary': "Salaire :",
        'set': "Définir",
        'change_percent': "Changer de % :",
        'percent': "%",
        'speed': "Vitesse :",
        'set_all': "Tout définir",
        'mood': "Humeur :",
        'set_mood': "Définir l'humeur",
        'mood_range_error': "L'humeur doit être comprise entre 1 et 100.",
        'employees_tab': "👥 Employés",
        'inventory_tab': "📦 Inventaire",
        'transactions_tab': "💰 Transactions",
        'general_tab': "📊 Général",
        'plan': "Plan :",
        'search': "🔍 Rechercher :",
        'bulk_change': "Tout modifier dans la colonne :",
        'bulk_apply': "Appliquer à tous",
        'value': "Valeur :",
        'paste_not_supported': "Le collage dans les transactions n'est pas pris en charge.",
        'schedule_edit': "Double-cliquez pour modifier l'emploi du temps.",
        'select_cell': "Sélectionnez d'abord une cellule (cliquez dessus).",
        'no_number': "Le presse-papiers ne contient pas de nombre.",
        'employee_not_found': "Employé non trouvé.",
        'enter_number': "Entrez un nombre.",
        'enter_integer': "Entrez un entier.",
        'file_loaded_title': "Fichier chargé",
        'file_loaded': "Fichier '{filename}' chargé.",
        'file_saved_title': "Sauvegardé",
        'file_saved': "Fichier sauvegardé.\nSauvegarde : {backup}",
        'save_first': "Chargez d'abord un fichier.",
        'error': "Erreur",
        'load_error': "Échec du chargement du fichier :\n{error}",
        'file_not_found': "Fichier non trouvé.",
        'schedule_editor': "Modifier l'emploi du temps",
        'start_hour': "Début (heure) :",
        'end_hour': "Fin (heure) :",
        'days_off': "Jours de congé :",
        'schedule_updated': "Emploi du temps mis à jour.",
        'schedule_save': "Enregistrer",
        'cancel': "Annuler",
        'no_plan_edit': "Sélectionnez un plan spécifique à modifier.",
        'bulk_plan_error': "Impossible de modifier le plan en mode 'Tous les composants (entrepôt)'. Sélectionnez un plan spécifique.",
        'bulk_done_title': "Terminé",
        'bulk_done_body': "Défini {value} dans la colonne '{col}' pour tous les composants.",
        'bulk_success_title': "Terminé",
        'bulk_success_body': "{action} pour {count} employés/candidats.",
        'plan_not_found': "Plan non trouvé.",
        'enter_valid_number': "Entrez un nombre valide.",
        'date': "Date",
        'version': "Version",
        'employees_count': "Employés",
        'transactions_count': "Transactions",
        'all_components': "Tous les composants (entrepôt)",
        'switch_lang': "🌐 English",
        'donate': "🙏 Faire un don",
        'donate_title': "Soutenir l'auteur",
        'donate_text': "Si vous aimez le programme et souhaitez remercier l'auteur, vous pouvez envoyer n'importe quel montant à l'un des portefeuilles suivants. Merci ! ❤️",
        'copy_address': "📋 Copier",
        'copied': "Copié !",
        'close': "Fermer",
        'col_id': "ID",
        'col_name': "Nom",
        'col_position': "Poste",
        'col_schedule': "Horaire",
        'col_speed': "Vitesse",
        'col_max': "Max",
        'col_salary': "Salaire",
        'col_mood': "Humeur",
        'col_component': "Composant",
        'col_plan': "Plan",
        'col_warehouse': "Entrepôt",
        'col_day': "Jour",
        'col_hour': "Heure",
        'col_amount': "Montant",
        'col_description': "Description"
    },
    'es': {
        'app_title': "Editor de guardado",
        'no_file': "No hay archivo cargado. Haga clic en '📂 Abrir archivo' para seleccionar.",
        'open_file': "📂 Abrir archivo",
        'save': "💾 Guardar",
        'refresh': "🔄 Actualizar",
        'balance': "💰 Saldo",
        'research': "🔬 Puntos de investigación",
        'apply': "Aplicar",
        'copy': "📋 Copiar",
        'paste': "📝 Pegar",
        'salary': "Salario:",
        'set': "Establecer",
        'change_percent': "Cambiar en %:",
        'percent': "%",
        'speed': "Velocidad:",
        'set_all': "Establecer todo",
        'mood': "Estado:",
        'set_mood': "Establecer estado",
        'mood_range_error': "El estado debe estar entre 1 y 100.",
        'employees_tab': "👥 Empleados",
        'inventory_tab': "📦 Inventario",
        'transactions_tab': "💰 Transacciones",
        'general_tab': "📊 General",
        'plan': "Plan:",
        'search': "🔍 Buscar:",
        'bulk_change': "Cambiar todo en columna:",
        'bulk_apply': "Aplicar a todos",
        'value': "Valor:",
        'paste_not_supported': "No se admite pegar en transacciones.",
        'schedule_edit': "Haga doble clic para editar el horario.",
        'select_cell': "Primero seleccione una celda (haga clic en ella).",
        'no_number': "El portapapeles no contiene un número.",
        'employee_not_found': "Empleado no encontrado.",
        'enter_number': "Introduzca un número.",
        'enter_integer': "Introduzca un número entero.",
        'file_loaded_title': "Archivo cargado",
        'file_loaded': "Archivo '{filename}' cargado.",
        'file_saved_title': "Guardado",
        'file_saved': "Archivo guardado.\nCopia de seguridad: {backup}",
        'save_first': "Primero cargue un archivo.",
        'error': "Error",
        'load_error': "Error al cargar el archivo:\n{error}",
        'file_not_found': "Archivo no encontrado.",
        'schedule_editor': "Editar horario",
        'start_hour': "Inicio (hora):",
        'end_hour': "Fin (hora):",
        'days_off': "Días libres:",
        'schedule_updated': "Horario actualizado.",
        'schedule_save': "Guardar",
        'cancel': "Cancelar",
        'no_plan_edit': "Seleccione un plan específico para editar.",
        'bulk_plan_error': "No se puede editar el plan en modo 'Todos los componentes (almacén)'. Seleccione un plan específico.",
        'bulk_done_title': "Hecho",
        'bulk_done_body': "Se estableció {value} en la columna '{col}' para todos los componentes.",
        'bulk_success_title': "Hecho",
        'bulk_success_body': "{action} para {count} empleados/candidatos.",
        'plan_not_found': "Plan no encontrado.",
        'enter_valid_number': "Introduzca un número válido.",
        'date': "Fecha",
        'version': "Versión",
        'employees_count': "Empleados",
        'transactions_count': "Transacciones",
        'all_components': "Todos los componentes (almacén)",
        'switch_lang': "🌐 English",
        'donate': "🙏 Donar",
        'donate_title': "Apoyar al autor",
        'donate_text': "Si te gusta el programa y quieres agradecer al autor, puedes enviar cualquier cantidad a una de las siguientes billeteras. ¡Gracias! ❤️",
        'copy_address': "📋 Copiar",
        'copied': "¡Copiado!",
        'close': "Cerrar",
        'col_id': "ID",
        'col_name': "Nombre",
        'col_position': "Puesto",
        'col_schedule': "Horario",
        'col_speed': "Velocidad",
        'col_max': "Máx",
        'col_salary': "Salario",
        'col_mood': "Estado",
        'col_component': "Componente",
        'col_plan': "Plan",
        'col_warehouse': "Almacén",
        'col_day': "Día",
        'col_hour': "Hora",
        'col_amount': "Cantidad",
        'col_description': "Descripción"
    },
    'ko': {
        'app_title': "세이브 에디터",
        'no_file': "파일이 로드되지 않았습니다. '📂 파일 열기'를 클릭하여 선택하세요.",
        'open_file': "📂 파일 열기",
        'save': "💾 저장",
        'refresh': "🔄 새로 고침",
        'balance': "💰 잔액",
        'research': "🔬 연구 포인트",
        'apply': "적용",
        'copy': "📋 복사",
        'paste': "📝 붙여넣기",
        'salary': "급여:",
        'set': "설정",
        'change_percent': "% 만큼 변경:",
        'percent': "%",
        'speed': "속도:",
        'set_all': "모두 설정",
        'mood': "기분:",
        'set_mood': "기분 설정",
        'mood_range_error': "기분은 1에서 100 사이여야 합니다.",
        'employees_tab': "👥 직원",
        'inventory_tab': "📦 인벤토리",
        'transactions_tab': "💰 거래 내역",
        'general_tab': "📊 일반",
        'plan': "계획:",
        'search': "🔍 검색:",
        'bulk_change': "컬럼의 모든 값을 변경:",
        'bulk_apply': "모두 적용",
        'value': "값:",
        'paste_not_supported': "거래 내역에 붙여넣기는 지원되지 않습니다.",
        'schedule_edit': "더블 클릭하여 일정을 편집하세요.",
        'select_cell': "먼저 셀을 선택하세요 (클릭).",
        'no_number': "클립보드에 숫자가 없습니다.",
        'employee_not_found': "직원을 찾을 수 없습니다.",
        'enter_number': "숫자를 입력하세요.",
        'enter_integer': "정수를 입력하세요.",
        'file_loaded_title': "파일 로드됨",
        'file_loaded': "파일 '{filename}'이(가) 로드되었습니다.",
        'file_saved_title': "저장됨",
        'file_saved': "파일이 저장되었습니다.\n백업: {backup}",
        'save_first': "먼저 파일을 로드하세요.",
        'error': "오류",
        'load_error': "파일 로드 실패:\n{error}",
        'file_not_found': "파일을 찾을 수 없습니다.",
        'schedule_editor': "일정 편집",
        'start_hour': "시작 (시):",
        'end_hour': "종료 (시):",
        'days_off': "휴무일:",
        'schedule_updated': "일정이 업데이트되었습니다.",
        'schedule_save': "저장",
        'cancel': "취소",
        'no_plan_edit': "편집할 특정 계획을 선택하세요.",
        'bulk_plan_error': "'모든 구성 요소 (창고)' 모드에서는 계획을 편집할 수 없습니다. 특정 계획을 선택하세요.",
        'bulk_done_title': "완료",
        'bulk_done_body': "모든 구성 요소에 대해 '{col}' 컬럼에 {value}을(를) 설정했습니다.",
        'bulk_success_title': "완료",
        'bulk_success_body': "{action} (직원/후보 {count}명).",
        'plan_not_found': "계획을 찾을 수 없습니다.",
        'enter_valid_number': "유효한 숫자를 입력하세요.",
        'date': "날짜",
        'version': "버전",
        'employees_count': "직원 수",
        'transactions_count': "거래 내역 수",
        'all_components': "모든 구성 요소 (창고)",
        'switch_lang': "🌐 English",
        'donate': "🙏 후원",
        'donate_title': "저자 지원",
        'donate_text': "프로그램이 마음에 들고 감사를 표하고 싶다면 다음 지갑 중 하나로 금액을 보내주세요. 감사합니다! ❤️",
        'copy_address': "📋 복사",
        'copied': "복사됨!",
        'close': "닫기",
        'col_id': "ID",
        'col_name': "이름",
        'col_position': "직책",
        'col_schedule': "일정",
        'col_speed': "속도",
        'col_max': "최대",
        'col_salary': "급여",
        'col_mood': "기분",
        'col_component': "구성 요소",
        'col_plan': "계획",
        'col_warehouse': "창고",
        'col_day': "일",
        'col_hour': "시간",
        'col_amount': "금액",
        'col_description': "설명"
    },
    'zh': {
        'app_title': "存档编辑器",
        'no_file': "未加载文件。请点击 '📂 打开文件' 选择。",
        'open_file': "📂 打开文件",
        'save': "💾 保存",
        'refresh': "🔄 刷新",
        'balance': "💰 余额",
        'research': "🔬 研究点数",
        'apply': "应用",
        'copy': "📋 复制",
        'paste': "📝 粘贴",
        'salary': "工资:",
        'set': "设置",
        'change_percent': "按 % 更改:",
        'percent': "%",
        'speed': "速度:",
        'set_all': "全部设置",
        'mood': "心情:",
        'set_mood': "设置心情",
        'mood_range_error': "心情必须在 1 到 100 之间。",
        'employees_tab': "👥 员工",
        'inventory_tab': "📦 库存",
        'transactions_tab': "💰 交易记录",
        'general_tab': "📊 常规",
        'plan': "计划:",
        'search': "🔍 搜索:",
        'bulk_change': "批量更改列中的值:",
        'bulk_apply': "全部应用",
        'value': "值:",
        'paste_not_supported': "交易记录不支持粘贴。",
        'schedule_edit': "双击编辑日程。",
        'select_cell': "请先选择单元格（点击它）。",
        'no_number': "剪贴板中不包含数字。",
        'employee_not_found': "未找到员工。",
        'enter_number': "请输入数字。",
        'enter_integer': "请输入整数。",
        'file_loaded_title': "文件已加载",
        'file_loaded': "文件 '{filename}' 已加载。",
        'file_saved_title': "已保存",
        'file_saved': "文件已保存。\n备份: {backup}",
        'save_first': "请先加载文件。",
        'error': "错误",
        'load_error': "无法加载文件:\n{error}",
        'file_not_found': "文件未找到。",
        'schedule_editor': "编辑日程",
        'start_hour': "开始 (小时):",
        'end_hour': "结束 (小时):",
        'days_off': "休息日:",
        'schedule_updated': "日程已更新。",
        'schedule_save': "保存",
        'cancel': "取消",
        'no_plan_edit': "请选择要编辑的具体计划。",
        'bulk_plan_error': "无法在“所有组件（仓库）”模式下编辑计划。请选择具体计划。",
        'bulk_done_title': "完成",
        'bulk_done_body': "为所有组件在 '{col}' 列中设置了 {value}。",
        'bulk_success_title': "完成",
        'bulk_success_body': "{action}，共 {count} 名员工/候选人。",
        'plan_not_found': "未找到计划。",
        'enter_valid_number': "请输入有效数字。",
        'date': "日期",
        'version': "版本",
        'employees_count': "员工数",
        'transactions_count': "交易数",
        'all_components': "所有组件（仓库）",
        'switch_lang': "🌐 English",
        'donate': "🙏 赞助",
        'donate_title': "支持作者",
        'donate_text': "如果您喜欢这个程序并想感谢作者，您可以向以下钱包发送任意金额。谢谢！❤️",
        'copy_address': "📋 复制",
        'copied': "已复制！",
        'close': "关闭",
        'col_id': "ID",
        'col_name': "名称",
        'col_position': "职位",
        'col_schedule': "日程",
        'col_speed': "速度",
        'col_max': "最大",
        'col_salary': "工资",
        'col_mood': "心情",
        'col_component': "组件",
        'col_plan': "计划",
        'col_warehouse': "仓库",
        'col_day': "天",
        'col_hour': "小时",
        'col_amount': "金额",
        'col_description': "描述"
    }
}

LANG_NAMES = ['ru', 'en', 'uk', 'fr', 'es', 'ko', 'zh']
LANG_DISPLAY = {
    'ru': "Русский",
    'en': "English",
    'uk': "Українська",
    'fr': "Français",
    'es': "Español",
    'ko': "한국어",
    'zh': "简体中文"
}

# ---------- НАСТРОЙКА СТИЛЯ ----------
def setup_styles():
    style = ttk.Style()
    style.theme_use('clam')
    BG = "#f0f4f8"
    FG = "#1a1a2e"
    SELECT_BG = "#4a90d9"
    SELECT_FG = "white"
    BUTTON_BG = "#4a90d9"
    BUTTON_FG = "white"
    HOVER_BG = "#357abd"

    style.configure('.', background=BG, foreground=FG, font=('Segoe UI', 10))
    style.configure('TLabel', background=BG, foreground=FG)
    style.configure('TFrame', background=BG)
    style.configure('TNotebook', background=BG, borderwidth=0)
    style.configure('TNotebook.Tab', background=BG, padding=[12, 4], font=('Segoe UI', 10, 'bold'))
    style.map('TNotebook.Tab', background=[('selected', '#4a90d9'), ('active', '#d4e2f7')],
              foreground=[('selected', 'white'), ('active', 'black')])
    style.configure('TButton', background=BUTTON_BG, foreground=BUTTON_FG, borderwidth=0,
                    focuscolor='none', font=('Segoe UI', 9, 'bold'), padding=6)
    style.map('TButton', background=[('active', HOVER_BG), ('pressed', '#2a6bb0')])
    style.configure('TEntry', fieldbackground='white', borderwidth=1, relief='solid')
    style.configure('Treeview', background='white', foreground='#1a1a2e', rowheight=28,
                    font=('Segoe UI', 9), fieldbackground='white')
    style.map('Treeview', background=[('selected', SELECT_BG)], foreground=[('selected', SELECT_FG)])
    style.configure('Treeview.Heading', background='#d4e2f7', foreground='#1a1a2e',
                    font=('Segoe UI', 9, 'bold'), borderwidth=0)
    style.map('Treeview.Heading', background=[('active', '#b8cfe0')])
    style.configure('TScrollbar', background=BG, troughcolor='#e0e7ee', arrowcolor='#4a90d9')
    style.map('TScrollbar', background=[('active', '#4a90d9')])
    style.configure('TLabelframe', background=BG, foreground=FG, borderwidth=1, relief='solid')
    style.configure('TLabelframe.Label', background=BG, foreground=FG, font=('Segoe UI', 10, 'bold'))
    return style

# ---------- КОНСТАНТЫ ----------
ALL_COMPONENTS = [
    "BlueprintComponent", "WireframeComponent", "GraphicsComponent", "UiComponent",
    "BackendComponent", "NetworkComponent", "DatabaseComponent", "SemanticComponent",
    "EncryptionComponent", "FilesystemComponent", "VideoComponent", "SmtpComponent",
    "I18nComponent", "SearchAlgorithmComponent", "CompressionComponent", "VirtualHardware",
    "OperatingSystem", "Firewall", "Copywriting", "TextFormat", "ImageFormat",
    "VideoFormat", "AudioFormat", "ContractAgreement", "Survey", "UserFeedback",
    "PhoneInterview", "AnalyticsResearch", "BehaviorObservation", "AbTesting",
    "DocumentationComponent", "ProcessManagement", "ContinuousIntegration", "CronJob",
    "ResearchPoint", "InterfaceModule", "FrontendModule", "BackendModule", "InputModule",
    "StorageModule", "ContentManagementModule", "SeoModule", "AuthenticationModule",
    "PaymentGatewayModule", "VideoPlaybackModule", "EmailModule", "LocalizationModule",
    "SearchModule", "BandwidthCompressionModule", "DatabaseLayer", "NotificationModule",
    "ApiClientModule", "CodeOptimizationModule", "UiElement", "UiSet", "ResponsiveUi",
    "DesignGuidelines", "VirtualContainer", "Cluster", "SwarmManagement"
]
DAY_NAMES = {
    'ru': ["Вс", "Пн", "Вт", "Ср", "Чт", "Пт", "Сб"],
    'en': ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"],
    'uk': ["Нд", "Пн", "Вт", "Ср", "Чт", "Пт", "Сб"],
    'fr': ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"],
    'es': ["Dom", "Lun", "Mar", "Mié", "Jue", "Vie", "Sáb"],
    'ko': ["일", "월", "화", "수", "목", "금", "토"],
    'zh': ["日", "一", "二", "三", "四", "五", "六"]
}

WALLETS = {
    "LTC": "ltc1q7zr4st8n5mlw6cju6jvz2wfdmz35a742c55vud",
    "BTC": "bc1qyjum9hhtvwjc482ggpu4uvln40qqwee8xeuga4",
    "ETH": "0x9FAAC1d2a2D2ccb6462eB4901f99EF61852B6E8B",
    "USDT": "0x9FAAC1d2a2D2ccb6462eB4901f99EF61852B6E8B",
    "XMR": "3WpcjStRTEQnXBz5C1AX2Xp352hj8PWv5DXihCH8QGww"
}

# ---------- ОСНОВНОЙ КЛАСС ----------
class SaveEditorApp:
    def __init__(self, root):
        self.root = root
        set_window_icon(root, 'icon2.ico')
        self.root.deiconify()
        self.root.title("Редактор сохранений")
        self.root.geometry("1200x750")
        self.root.configure(bg='#f0f4f8')
        setup_styles()

        self.current_lang_index = 0
        self.current_lang = LANG_NAMES[self.current_lang_index]
        self.lang_data = LANG[self.current_lang]

        self.data = None
        self.file_path = None
        self.default_save_folder = self.find_save_folder()

        self.last_cell = {'employees': [None, None], 'inventory': [None, None], 'transactions': [None, None]}
        self.active_table = None

        main_frame = ttk.Frame(self.root, padding=10)
        main_frame.pack(fill=tk.BOTH, expand=True)
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        self.tab_general = ttk.Frame(self.notebook, padding=10)
        self.notebook.add(self.tab_general, text=self.lang_data['general_tab'])
        self.setup_general_tab()

        self.tab_employees = ttk.Frame(self.notebook, padding=10)
        self.notebook.add(self.tab_employees, text=self.lang_data['employees_tab'])
        self.setup_employees_tab()

        self.tab_inventory = ttk.Frame(self.notebook, padding=10)
        self.notebook.add(self.tab_inventory, text=self.lang_data['inventory_tab'])
        self.setup_inventory_tab()

        self.tab_transactions = ttk.Frame(self.notebook, padding=10)
        self.notebook.add(self.tab_transactions, text=self.lang_data['transactions_tab'])
        self.setup_transactions_tab()

        btn_frame = ttk.Frame(main_frame, padding=(0, 10, 0, 0))
        btn_frame.pack(fill=tk.X)
        self.save_btn = ttk.Button(btn_frame, text=self.lang_data['save'], command=self.save_data)
        self.save_btn.pack(side=tk.RIGHT, padx=5)
        self.refresh_btn = ttk.Button(btn_frame, text=self.lang_data['refresh'], command=self.refresh_all)
        self.refresh_btn.pack(side=tk.RIGHT, padx=5)

        self.root.bind('<Control-c>', self.global_copy)
        self.root.bind('<Control-v>', self.global_paste)

        self.show_no_file_message()

    # ---------- ПОИСК ПАПКИ СОХРАНЕНИЙ ----------
    def find_save_folder(self):
        try:
            saved_games = os.path.join(os.environ['USERPROFILE'], 'Saved Games')
            if os.path.exists(saved_games):
                startup_folder = os.path.join(saved_games, 'Startup Company')
                if os.path.exists(startup_folder):
                    for item in os.listdir(startup_folder):
                        full_path = os.path.join(startup_folder, item)
                        if os.path.isdir(full_path) and ('testing' in item.lower() or 'save' in item.lower()):
                            for f in os.listdir(full_path):
                                if f.endswith('.json'):
                                    return full_path
                    return startup_folder
        except Exception:
            pass
        return None

    # ---------- ЗАГРУЗКА ФАЙЛА ----------
    def load_file(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                new_data = json.load(f)
        except Exception as e:
            messagebox.showerror(self.lang_data['error'], self.lang_data['load_error'].format(error=str(e)))
            return
        self.file_path = file_path
        self.data = new_data
        self.root.title(f"{self.lang_data['app_title']} - {os.path.basename(file_path)}")
        self.refresh_all()
        messagebox.showinfo(
            self.lang_data['file_loaded_title'],
            self.lang_data['file_loaded'].format(filename=os.path.basename(file_path))
        )

    # ---------- ПЕРЕКЛЮЧЕНИЕ ЯЗЫКА ----------
    def switch_language(self):
        self.current_lang_index = (self.current_lang_index + 1) % len(LANG_NAMES)
        self.current_lang = LANG_NAMES[self.current_lang_index]
        self.lang_data = LANG[self.current_lang]
        self.update_ui_language()

    def update_ui_language(self):
        if self.file_path:
            self.root.title(f"{self.lang_data['app_title']} - {os.path.basename(self.file_path)}")
        else:
            self.root.title(self.lang_data['app_title'])

        self.notebook.tab(self.tab_general, text=self.lang_data['general_tab'])
        self.notebook.tab(self.tab_employees, text=self.lang_data['employees_tab'])
        self.notebook.tab(self.tab_inventory, text=self.lang_data['inventory_tab'])
        self.notebook.tab(self.tab_transactions, text=self.lang_data['transactions_tab'])

        self.save_btn.config(text=self.lang_data['save'])
        self.refresh_btn.config(text=self.lang_data['refresh'])

        self.update_general_labels()
        self.update_employee_labels()
        self.update_inventory_labels()
        self.update_transaction_labels()
        self.update_column_headers()
        self.refresh_all()

    # ---------- ВСПОМОГАТЕЛЬНЫЕ МЕТОДЫ ----------
    def _get_tree(self, table_name):
        return getattr(self, f"tree_{table_name}", None)

    def _get_last_cell(self, table_name):
        return self.last_cell.get(table_name)

    def _set_active_cell(self, event, table_name):
        tree = event.widget
        region = tree.identify_region(event.x, event.y)
        if region == "cell":
            item = tree.identify_row(event.y)
            column = tree.identify_column(event.x)
            if item and column:
                self.last_cell[table_name] = [item, column]
                self.active_table = table_name

    def _copy_cell(self, table_name):
        if not self.data:
            messagebox.showinfo(self.lang_data['save_first'])
            return
        tree = self._get_tree(table_name)
        last = self._get_last_cell(table_name)
        if not tree or not last or not last[0] or not last[1]:
            messagebox.showinfo(self.lang_data['select_cell'])
            return
        item, col = last
        col_index = int(col[1:]) - 1
        values = list(tree.item(item, 'values'))
        if col_index < len(values):
            value = str(values[col_index])
            self.root.clipboard_clear()
            self.root.clipboard_append(value)
            self.root.update()
            self.root.title(f"{self.lang_data['app_title']} - Скопировано: {value}")

    def _paste_cell(self, table_name):
        if not self.data:
            messagebox.showinfo(self.lang_data['save_first'])
            return
        tree = self._get_tree(table_name)
        last = self._get_last_cell(table_name)
        if not tree or not last or not last[0] or not last[1]:
            messagebox.showinfo(self.lang_data['select_cell'])
            return
        item, col = last
        col_index = int(col[1:]) - 1
        col_name = tree['columns'][col_index]

        # Проверяем по ключам
        if table_name == 'employees' and col_name not in ('col_speed', 'col_max', 'col_salary', 'col_mood'):
            messagebox.showinfo(self.lang_data['paste_not_supported'])
            return
        if table_name == 'inventory' and col_name not in ('col_plan', 'col_warehouse'):
            return
        if table_name == 'transactions':
            messagebox.showinfo(self.lang_data['paste_not_supported'])
            return
        if col_name == 'col_schedule':
            messagebox.showinfo(self.lang_data['schedule_edit'])
            return

        try:
            new_value = float(self.root.clipboard_get().strip())
        except:
            messagebox.showerror(self.lang_data['error'], self.lang_data['no_number'])
            return

        values = list(tree.item(item, 'values'))
        if table_name == 'employees':
            self._update_employee_value(values[0], col_name, new_value)
        elif table_name == 'inventory':
            component = values[0]
            plan_name = self.plan_var.get()
            all_comp = self.lang_data['all_components']
            if col_name == 'col_plan':
                if plan_name == all_comp:
                    messagebox.showinfo(self.lang_data['no_plan_edit'])
                    return
                plans = self.data.get('productionPlans', [])
                for p in plans:
                    if p.get('name') == plan_name:
                        p['production'][component] = new_value
                        break
            elif col_name == 'col_warehouse':
                self.data['inventory'][component] = new_value
            self.update_inventory_table()
        self.last_cell[table_name] = [None, None]
        self.root.title(f"{self.lang_data['app_title']} - {os.path.basename(self.file_path) if self.file_path else ''}")

    def _update_employee_value(self, emp_id_prefix, col_name, new_value):
        if not self.data:
            return
        found = None
        for ws in self.data.get('office', {}).get('workstations', []):
            emp = ws.get('employee')
            if emp and emp.get('id', '').startswith(emp_id_prefix):
                found = emp
                break
        if not found:
            for cand in self.data.get('candidates', []):
                if cand.get('id', '').startswith(emp_id_prefix):
                    found = cand
                    break
        if not found:
            messagebox.showerror(self.lang_data['error'], self.lang_data['employee_not_found'])
            return

        if col_name == 'col_mood':
            if new_value < 1 or new_value > 100:
                messagebox.showerror(self.lang_data['error'], self.lang_data['mood_range_error'])
                return

        if col_name == 'col_speed':
            found['speed'] = new_value
        elif col_name == 'col_max':
            found['maxSpeed'] = new_value
        elif col_name == 'col_salary':
            found['salary'] = new_value
        elif col_name == 'col_mood':
            found['mood'] = new_value
        self.refresh_employees()

    def _update_inventory_value(self, component, col_name, new_value):
        if not self.data:
            return
        plan_name = self.plan_var.get()
        all_comp = self.lang_data['all_components']
        if col_name == 'col_plan':
            if plan_name == all_comp:
                messagebox.showinfo(self.lang_data['no_plan_edit'])
                return
            plans = self.data.get('productionPlans', [])
            for p in plans:
                if p.get('name') == plan_name:
                    p['production'][component] = new_value
                    break
        elif col_name == 'col_warehouse':
            self.data['inventory'][component] = new_value
        self.update_inventory_table()

    def global_copy(self, event):
        if self.active_table:
            self._copy_cell(self.active_table)

    def global_paste(self, event):
        if self.active_table:
            self._paste_cell(self.active_table)

    # ---------- ОБЩИЕ МЕТОДЫ ----------
    def select_and_load_file(self):
        initial_dir = self.default_save_folder if self.default_save_folder else os.path.expanduser("~")
        new_path = filedialog.askopenfilename(
            title=self.lang_data['open_file'],
            initialdir=initial_dir,
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        if not new_path:
            return
        self.load_file(new_path)

    def show_no_file_message(self):
        self.general_info.set(self.lang_data['no_file'])
        self.balance_var.set("")
        self.research_points_var.set("")
        self.tree_employees.delete(*self.tree_employees.get_children())
        self.inv_tree.delete(*self.inv_tree.get_children())
        self.trans_tree.delete(*self.trans_tree.get_children())
        self.root.title(self.lang_data['app_title'])

    def save_data(self):
        if not self.data or not self.file_path:
            messagebox.showinfo(self.lang_data['save_first'])
            return
        backup = self.file_path + ".bak"
        shutil.copy2(self.file_path, backup)
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, indent=2, ensure_ascii=False)
        messagebox.showinfo(
            self.lang_data['file_saved_title'],
            self.lang_data['file_saved'].format(backup=backup)
        )

    def refresh_all(self):
        if not self.data:
            self.show_no_file_message()
            return
        self.refresh_general()
        self.refresh_employees()
        self.refresh_inventory()
        self.refresh_transactions()

    # ---------- ОКНО ДОНАТА ----------
    def open_donate_window(self):
        dialog = tk.Toplevel(self.root)
        dialog.title(self.lang_data['donate_title'])
        dialog.geometry("500x400")
        dialog.transient(self.root)
        dialog.grab_set()
        dialog.configure(bg='#f0f4f8')
        set_window_icon(dialog, 'icon2.ico')

        main_frame = ttk.Frame(dialog, padding=15)
        main_frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(main_frame, text=self.lang_data['donate_text'], wraplength=450,
                  font=('Segoe UI', 10), background='#f0f4f8').pack(pady=(0, 15))

        wallets_frame = ttk.LabelFrame(main_frame, text="💰 " + self.lang_data['donate_title'], padding=10)
        wallets_frame.pack(fill=tk.X, pady=5)

        for currency, address in WALLETS.items():
            row = ttk.Frame(wallets_frame)
            row.pack(fill=tk.X, pady=3)
            ttk.Label(row, text=f"{currency}:", font=('Segoe UI', 9, 'bold'),
                      background='#f0f4f8').pack(side=tk.LEFT, padx=(0, 5))
            addr_label = ttk.Label(row, text=address, font=('Consolas', 9),
                                   background='#f0f4f8', foreground='#1a1a2e')
            addr_label.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
            copy_btn = ttk.Button(row, text=self.lang_data['copy_address'],
                                  command=lambda a=address: self.copy_to_clipboard(a, dialog))
            copy_btn.pack(side=tk.RIGHT, padx=2)

        ttk.Button(main_frame, text=self.lang_data['close'], command=dialog.destroy).pack(pady=15)
        dialog.update_idletasks()
        x = self.root.winfo_x() + (self.root.winfo_width() - dialog.winfo_width()) // 2
        y = self.root.winfo_y() + (self.root.winfo_height() - dialog.winfo_height()) // 2
        dialog.geometry(f"+{x}+{y}")

    def copy_to_clipboard(self, text, dialog):
        self.root.clipboard_clear()
        self.root.clipboard_append(text)
        self.root.update()
        messagebox.showinfo(self.lang_data['copied'], f"{self.lang_data['copied']}\n{text}")

    # ---------- ВКЛАДКА "ОБЩЕЕ" ----------
    def setup_general_tab(self):
        frame = self.tab_general
        top_panel = ttk.Frame(frame)
        top_panel.pack(fill=tk.X, pady=(0, 5))
        self.donate_btn = ttk.Button(top_panel, text=self.lang_data['donate'], command=self.open_donate_window)
        self.donate_btn.pack(side=tk.RIGHT, padx=5)
        self.lang_btn = ttk.Button(top_panel, text="🌐 " + LANG_DISPLAY[self.current_lang], command=self.switch_language)
        self.lang_btn.pack(side=tk.RIGHT, padx=5)
        self.open_btn = ttk.Button(top_panel, text=self.lang_data['open_file'], command=self.select_and_load_file)
        self.open_btn.pack(side=tk.RIGHT, padx=5)

        self.general_info = tk.StringVar()
        self.balance_var = tk.StringVar()
        self.research_points_var = tk.StringVar()

        info_label = ttk.Label(frame, textvariable=self.general_info, font=('Segoe UI', 12, 'bold'),
                               background='#f0f4f8', foreground='#1a1a2e')
        info_label.pack(anchor='w', pady=(0, 15))

        self.balance_frame = ttk.LabelFrame(frame, text=self.lang_data['balance'], padding=10)
        self.balance_frame.pack(fill=tk.X, pady=5)
        self.balance_label = ttk.Label(self.balance_frame, text=self.lang_data['balance'] + ":")
        self.balance_label.grid(row=0, column=0, sticky='w', padx=5, pady=5)
        self.balance_entry = ttk.Entry(self.balance_frame, textvariable=self.balance_var, width=20)
        self.balance_entry.grid(row=0, column=1, padx=5, pady=5)
        self.apply_balance_btn = ttk.Button(self.balance_frame, text=self.lang_data['apply'], command=self.apply_balance)
        self.apply_balance_btn.grid(row=0, column=2, padx=5)

        self.research_frame = ttk.LabelFrame(frame, text=self.lang_data['research'], padding=10)
        self.research_frame.pack(fill=tk.X, pady=5)
        self.research_label = ttk.Label(self.research_frame, text=self.lang_data['research'] + ":")
        self.research_label.grid(row=0, column=0, sticky='w', padx=5, pady=5)
        self.research_entry = ttk.Entry(self.research_frame, textvariable=self.research_points_var, width=20)
        self.research_entry.grid(row=0, column=1, padx=5, pady=5)
        self.apply_research_btn = ttk.Button(self.research_frame, text=self.lang_data['apply'], command=self.apply_research_points)
        self.apply_research_btn.grid(row=0, column=2, padx=5)

    def update_general_labels(self):
        self.open_btn.config(text=self.lang_data['open_file'])
        self.lang_btn.config(text="🌐 " + LANG_DISPLAY[self.current_lang])
        self.donate_btn.config(text=self.lang_data['donate'])
        self.balance_frame.config(text=self.lang_data['balance'])
        self.balance_label.config(text=self.lang_data['balance'] + ":")
        self.apply_balance_btn.config(text=self.lang_data['apply'])
        self.research_frame.config(text=self.lang_data['research'])
        self.research_label.config(text=self.lang_data['research'] + ":")
        self.apply_research_btn.config(text=self.lang_data['apply'])

    def refresh_general(self):
        if not self.data:
            self.show_no_file_message()
            return
        d = self.data
        self.general_info.set(
            f"{self.lang_data['balance']}: {d.get('balance', 0):,.2f}   |   "
            f"{self.lang_data['research']}: {d.get('researchPoints', 0)}   |   "
            f"{self.lang_data['date']}: {d.get('date', 'N/A')}   |   "
            f"{self.lang_data['version']}: {d.get('lastVersion', 'N/A')}\n"
            f"{self.lang_data['employees_count']}: {len(d.get('office', {}).get('workstations', []))}   |   "
            f"{self.lang_data['transactions_count']}: {len(d.get('transactions', []))}"
        )
        self.balance_var.set(str(d.get('balance', 0)))
        self.research_points_var.set(str(d.get('researchPoints', 0)))

    def apply_balance(self):
        if not self.data:
            messagebox.showinfo(self.lang_data['save_first'])
            return
        try:
            self.data['balance'] = float(self.balance_var.get())
            self.refresh_general()
        except ValueError:
            messagebox.showerror(self.lang_data['error'], self.lang_data['enter_number'])

    def apply_research_points(self):
        if not self.data:
            messagebox.showinfo(self.lang_data['save_first'])
            return
        try:
            self.data['researchPoints'] = int(self.research_points_var.get())
            self.refresh_general()
        except ValueError:
            messagebox.showerror(self.lang_data['error'], self.lang_data['enter_integer'])

    # ---------- ВКЛАДКА "СОТРУДНИКИ" ----------
    def setup_employees_tab(self):
        frame = self.tab_employees
        toolbar = ttk.Frame(frame)
        toolbar.pack(fill=tk.X, pady=(0, 5))
        self.emp_copy_btn = ttk.Button(toolbar, text=self.lang_data['copy'], command=lambda: self._copy_cell('employees'))
        self.emp_copy_btn.pack(side=tk.LEFT, padx=2)
        self.emp_paste_btn = ttk.Button(toolbar, text=self.lang_data['paste'], command=lambda: self._paste_cell('employees'))
        self.emp_paste_btn.pack(side=tk.LEFT, padx=2)
        ttk.Separator(toolbar, orient='vertical').pack(side=tk.LEFT, fill=tk.Y, padx=6)

        # Зарплата
        self.salary_label = ttk.Label(toolbar, text=self.lang_data['salary'])
        self.salary_label.pack(side=tk.LEFT, padx=(10, 2))
        self.salary_fixed_var = tk.StringVar()
        ttk.Entry(toolbar, textvariable=self.salary_fixed_var, width=10).pack(side=tk.LEFT, padx=2)
        self.salary_set_btn = ttk.Button(toolbar, text=self.lang_data['set'], command=self.set_all_salaries_fixed)
        self.salary_set_btn.pack(side=tk.LEFT, padx=2)

        # Процент изменения
        self.percent_label = ttk.Label(toolbar, text=self.lang_data['change_percent'])
        self.percent_label.pack(side=tk.LEFT, padx=(10, 2))
        self.salary_percent_var = tk.StringVar()
        ttk.Entry(toolbar, textvariable=self.salary_percent_var, width=6).pack(side=tk.LEFT, padx=2)
        self.percent_sign = ttk.Label(toolbar, text=self.lang_data['percent'])
        self.percent_sign.pack(side=tk.LEFT)
        self.salary_pct_btn = ttk.Button(toolbar, text=self.lang_data['apply'], command=self.apply_salary_percent)
        self.salary_pct_btn.pack(side=tk.LEFT, padx=2)

        ttk.Separator(toolbar, orient='vertical').pack(side=tk.LEFT, fill=tk.Y, padx=6)

        # Скорость
        self.speed_label = ttk.Label(toolbar, text=self.lang_data['speed'])
        self.speed_label.pack(side=tk.LEFT, padx=(10, 2))
        self.speed_value_var = tk.StringVar(value="1200")
        ttk.Entry(toolbar, textvariable=self.speed_value_var, width=8).pack(side=tk.LEFT, padx=2)
        self.speed_set_btn = ttk.Button(toolbar, text=self.lang_data['set_all'], command=self.set_all_speed_custom)
        self.speed_set_btn.pack(side=tk.LEFT, padx=2)

        ttk.Separator(toolbar, orient='vertical').pack(side=tk.LEFT, fill=tk.Y, padx=6)

        # Настроение
        self.mood_label = ttk.Label(toolbar, text=self.lang_data['mood'])
        self.mood_label.pack(side=tk.LEFT, padx=(10, 2))
        self.mood_fixed_var = tk.StringVar()
        ttk.Entry(toolbar, textvariable=self.mood_fixed_var, width=6).pack(side=tk.LEFT, padx=2)
        self.mood_set_btn = ttk.Button(toolbar, text=self.lang_data['set_mood'], command=self.set_all_mood)
        self.mood_set_btn.pack(side=tk.LEFT, padx=2)

        self.emp_columns = ('col_id', 'col_name', 'col_position', 'col_schedule', 'col_speed', 'col_max', 'col_salary', 'col_mood')
        self.tree_employees = self._create_treeview(frame, self.emp_columns,
                                                    {'col_id': 100, 'col_name': 120, 'col_position': 110,
                                                     'col_schedule': 150, 'col_speed': 80, 'col_max': 80,
                                                     'col_salary': 90, 'col_mood': 80})
        self.tree_employees.bind('<Button-1>', lambda e: self._set_active_cell(e, 'employees'))
        self.tree_employees.bind('<Double-1>', self.on_employee_double_click)
        self.edit_entry = None

    def update_employee_labels(self):
        self.emp_copy_btn.config(text=self.lang_data['copy'])
        self.emp_paste_btn.config(text=self.lang_data['paste'])
        self.salary_label.config(text=self.lang_data['salary'])
        self.salary_set_btn.config(text=self.lang_data['set'])
        self.percent_label.config(text=self.lang_data['change_percent'])
        self.percent_sign.config(text=self.lang_data['percent'])
        self.salary_pct_btn.config(text=self.lang_data['apply'])
        self.speed_label.config(text=self.lang_data['speed'])
        self.speed_set_btn.config(text=self.lang_data['set_all'])
        self.mood_label.config(text=self.lang_data['mood'])
        self.mood_set_btn.config(text=self.lang_data['set_mood'])

    # ---------- МАССОВЫЕ ИЗМЕНЕНИЯ ----------
    def _apply_to_all_employees(self, func):
        if not self.data:
            return
        for ws in self.data.get('office', {}).get('workstations', []):
            emp = ws.get('employee')
            if emp:
                func(emp)
        for cand in self.data.get('candidates', []):
            func(cand)

    def set_all_salaries_fixed(self):
        if not self.data:
            messagebox.showinfo(self.lang_data['save_first'])
            return
        try:
            val = float(self.salary_fixed_var.get())
        except ValueError:
            messagebox.showerror(self.lang_data['error'], self.lang_data['enter_number'])
            return
        count = self._apply_to_all_employees_count(lambda emp: emp.update({'salary': val}))
        self.refresh_employees()
        action = f"Установлена зарплата {val}" if self.current_lang == 'ru' else f"Set salary {val}"
        messagebox.showinfo(
            self.lang_data['bulk_success_title'],
            self.lang_data['bulk_success_body'].format(action=action, count=count)
        )

    def apply_salary_percent(self):
        if not self.data:
            messagebox.showinfo(self.lang_data['save_first'])
            return
        try:
            pct = float(self.salary_percent_var.get())
        except ValueError:
            messagebox.showerror(self.lang_data['error'], self.lang_data['enter_number'])
            return
        count = self._apply_to_all_employees_count(lambda emp: emp.update({'salary': emp.get('salary', 0) * (1 + pct/100)}))
        self.refresh_employees()
        action = f"Зарплаты изменены на {pct}%" if self.current_lang == 'ru' else f"Salaries changed by {pct}%"
        messagebox.showinfo(
            self.lang_data['bulk_success_title'],
            self.lang_data['bulk_success_body'].format(action=action, count=count)
        )

    def set_all_speed_custom(self):
        if not self.data:
            messagebox.showinfo(self.lang_data['save_first'])
            return
        try:
            speed = float(self.speed_value_var.get())
        except ValueError:
            messagebox.showerror(self.lang_data['error'], self.lang_data['enter_number'])
            return
        count = self._apply_to_all_employees_count(lambda emp: emp.update({'speed': speed, 'maxSpeed': speed}))
        self.refresh_employees()
        action = f"Установлена скорость {speed}" if self.current_lang == 'ru' else f"Set speed {speed}"
        messagebox.showinfo(
            self.lang_data['bulk_success_title'],
            self.lang_data['bulk_success_body'].format(action=action, count=count)
        )

    def set_all_mood(self):
        if not self.data:
            messagebox.showinfo(self.lang_data['save_first'])
            return
        try:
            val = float(self.mood_fixed_var.get())
        except ValueError:
            messagebox.showerror(self.lang_data['error'], self.lang_data['enter_number'])
            return
        if val < 1 or val > 100:
            messagebox.showerror(self.lang_data['error'], self.lang_data['mood_range_error'])
            return
        count = self._apply_to_all_employees_count(lambda emp: emp.update({'mood': val}))
        self.refresh_employees()
        action = f"Установлено настроение {val}" if self.current_lang == 'ru' else f"Set mood {val}"
        messagebox.showinfo(
            self.lang_data['bulk_success_title'],
            self.lang_data['bulk_success_body'].format(action=action, count=count)
        )

    def _apply_to_all_employees_count(self, func):
        count = 0
        if not self.data:
            return 0
        for ws in self.data.get('office', {}).get('workstations', []):
            emp = ws.get('employee')
            if emp:
                func(emp)
                count += 1
        for cand in self.data.get('candidates', []):
            func(cand)
            count += 1
        return count

    # ---------- ОСТАЛЬНЫЕ МЕТОДЫ ----------
    def _create_treeview(self, parent, col_keys, widths=None):
        tree = ttk.Treeview(parent, columns=col_keys, show='headings', height=20)
        for key in col_keys:
            text = self.lang_data[key]
            tree.heading(key, text=text)
            tree.column(key, width=widths.get(key, 100) if widths else 100)
        vsb = ttk.Scrollbar(parent, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=vsb.set)
        tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        vsb.pack(side=tk.RIGHT, fill=tk.Y)
        return tree

    def update_column_headers(self):
        for key in self.emp_columns:
            self.tree_employees.heading(key, text=self.lang_data[key])
        for key in self.inv_columns:
            self.inv_tree.heading(key, text=self.lang_data[key])
        for key in self.trans_columns:
            self.trans_tree.heading(key, text=self.lang_data[key])

    def refresh_employees(self):
        self.tree_employees.delete(*self.tree_employees.get_children())
        if not self.data:
            return
        day_names = DAY_NAMES[self.current_lang]
        for ws in self.data.get('office', {}).get('workstations', []):
            emp = ws.get('employee')
            if emp:
                self.tree_employees.insert('', 'end', values=(
                    emp.get('id', '')[:8],
                    emp.get('name', 'N/A'),
                    emp.get('employeeTypeName', ''),
                    self.format_schedule(emp, day_names),
                    emp.get('speed', 0),
                    emp.get('maxSpeed', 0),
                    emp.get('salary', 0),
                    emp.get('mood', '')
                ))
        for cand in self.data.get('candidates', []):
            self.tree_employees.insert('', 'end', values=(
                cand.get('id', '')[:8],
                cand.get('name', 'N/A') + (" (кандидат)" if self.current_lang in ['ru', 'uk'] else " (candidate)"),
                cand.get('employeeTypeName', ''),
                self.format_schedule(cand, day_names),
                cand.get('speed', 0),
                cand.get('maxSpeed', 0),
                cand.get('salary', 0),
                cand.get('mood', '')
            ))

    def format_schedule(self, employee, day_names):
        schedule = employee.get('schedule')
        if not schedule:
            return "Нет" if self.current_lang in ['ru', 'uk'] else "None"
        start = schedule.get('start', {})
        end = schedule.get('end', {})
        days_off = schedule.get('daysOff', [])
        time_str = f"{start.get('hour', 0):02d}:{start.get('minute', 0):02d}-{end.get('hour', 8):02d}:{end.get('minute', 0):02d}"
        if days_off:
            days_str = ", ".join(day_names[d] for d in days_off if 0 <= d < 7)
            off_text = "вых: " if self.current_lang in ['ru', 'uk'] else "off: "
            return f"{time_str} ({off_text}{days_str})"
        return time_str

    def on_employee_double_click(self, event):
        self._on_double_click(event, 'employees', self.tree_employees, self._edit_employee_field)

    def _edit_employee_field(self, item, col_name, values):
        if col_name == 'col_schedule':
            emp_id = values[0]
            found = None
            for ws in self.data.get('office', {}).get('workstations', []):
                emp = ws.get('employee')
                if emp and emp.get('id', '').startswith(emp_id):
                    found = emp
                    break
            if not found:
                for cand in self.data.get('candidates', []):
                    if cand.get('id', '').startswith(emp_id):
                        found = cand
                        break
            if found:
                self.edit_schedule(found)
            else:
                messagebox.showerror(self.lang_data['error'], self.lang_data['employee_not_found'])
            return True
        elif col_name in ('col_speed', 'col_max', 'col_salary', 'col_mood'):
            return False
        else:
            return True

    def edit_schedule(self, employee):
        schedule = employee.get('schedule', {})
        start_h = schedule.get('start', {}).get('hour', 8)
        end_h = schedule.get('end', {}).get('hour', 16)
        days_off = set(schedule.get('daysOff', []))

        dialog = tk.Toplevel(self.root)
        dialog.title(self.lang_data['schedule_editor'])
        dialog.geometry("320x280")
        dialog.transient(self.root)
        dialog.grab_set()
        dialog.configure(bg='#f0f4f8')
        set_window_icon(dialog, 'icon2.ico')

        main = ttk.Frame(dialog, padding=10)
        main.pack(fill=tk.BOTH, expand=True)
        ttk.Label(main, text=self.lang_data['start_hour']).grid(row=0, column=0, sticky='w', padx=5, pady=5)
        start_var = tk.IntVar(value=start_h)
        ttk.Spinbox(main, from_=0, to=23, textvariable=start_var, width=5).grid(row=0, column=1, padx=5, pady=5)
        ttk.Label(main, text=self.lang_data['end_hour']).grid(row=1, column=0, sticky='w', padx=5, pady=5)
        end_var = tk.IntVar(value=end_h)
        ttk.Spinbox(main, from_=0, to=23, textvariable=end_var, width=5).grid(row=1, column=1, padx=5, pady=5)
        ttk.Label(main, text=self.lang_data['days_off']).grid(row=2, column=0, columnspan=2, pady=5)

        day_vars = []
        day_names = DAY_NAMES[self.current_lang]
        for i, name in enumerate(day_names):
            var = tk.BooleanVar(value=(i in days_off))
            day_vars.append(var)
            ttk.Checkbutton(main, text=name, variable=var).grid(row=3 + i//4, column=i%4, padx=5, pady=2, sticky='w')

        def save():
            employee['schedule'] = {
                "start": {"hour": start_var.get(), "minute": 0},
                "end": {"hour": end_var.get(), "minute": 0},
                "daysOff": [i for i, v in enumerate(day_vars) if v.get()],
                "trainingDays": schedule.get('trainingDays', [])
            }
            dialog.destroy()
            self.refresh_employees()
            messagebox.showinfo(self.lang_data['schedule_updated'])
        ttk.Button(main, text=self.lang_data['schedule_save'], command=save).grid(row=10, column=0, pady=10)
        ttk.Button(main, text=self.lang_data['cancel'], command=dialog.destroy).grid(row=10, column=1, pady=10)

    def _on_double_click(self, event, table_name, tree, custom_handler):
        if not self.data:
            messagebox.showinfo(self.lang_data['save_first'])
            return

        if hasattr(self, f"edit_entry_{table_name}") and getattr(self, f"edit_entry_{table_name}"):
            return

        item = tree.identify_row(event.y)
        if not item:
            return
        column = tree.identify_column(event.x)
        if not column:
            return
        col_index = int(column[1:]) - 1
        col_name = tree['columns'][col_index]
        values = list(tree.item(item, 'values'))

        if custom_handler(item, col_name, values):
            return

        editable_indices = []
        if table_name == 'employees':
            editable_indices = [4, 5, 6, 7]  # Скорость, Макс, Зарплата, Настроение
        elif table_name == 'inventory':
            editable_indices = [1, 2]
        else:
            return

        if col_index not in editable_indices:
            return

        old_value = values[col_index]
        bbox = tree.bbox(item, column)
        if not bbox:
            return
        x, y, width, height = bbox
        if width == 0 or height == 0:
            return

        entry = ttk.Entry(tree, width=10)
        entry.place(x=x, y=y, width=width, height=height)
        entry.insert(0, str(old_value))
        entry.focus_set()
        entry.select_range(0, tk.END)
        setattr(self, f"edit_entry_{table_name}", entry)

        def save_edit(event=None):
            new_text = entry.get()
            entry.destroy()
            setattr(self, f"edit_entry_{table_name}", None)
            try:
                new_value = float(new_text)
                if table_name == 'employees':
                    self._update_employee_value(values[0], col_name, new_value)
                elif table_name == 'inventory':
                    self._update_inventory_value(values[0], col_name, new_value)
            except ValueError:
                messagebox.showerror(self.lang_data['error'], self.lang_data['enter_number'])
                if table_name == 'employees':
                    self.refresh_employees()
                else:
                    self.update_inventory_table()

        entry.bind('<Return>', save_edit)
        entry.bind('<Escape>', lambda e: entry.destroy())
        entry.bind('<FocusOut>', save_edit)

    # ---------- ВКЛАДКА "ИНВЕНТАРЬ" ----------
    def setup_inventory_tab(self):
        frame = self.tab_inventory
        toolbar = ttk.Frame(frame)
        toolbar.pack(fill=tk.X, pady=(0, 5))
        self.inv_copy_btn = ttk.Button(toolbar, text=self.lang_data['copy'], command=lambda: self._copy_cell('inventory'))
        self.inv_copy_btn.pack(side=tk.LEFT, padx=2)
        self.inv_paste_btn = ttk.Button(toolbar, text=self.lang_data['paste'], command=lambda: self._paste_cell('inventory'))
        self.inv_paste_btn.pack(side=tk.LEFT, padx=2)
        ttk.Separator(toolbar, orient='vertical').pack(side=tk.LEFT, fill=tk.Y, padx=6)

        self.plan_label = ttk.Label(toolbar, text=self.lang_data['plan'])
        self.plan_label.pack(side=tk.LEFT, padx=(10, 2))
        self.plan_var = tk.StringVar()
        self.plan_combo = ttk.Combobox(toolbar, textvariable=self.plan_var, state='readonly', width=20)
        self.plan_combo.pack(side=tk.LEFT, padx=2)
        self.plan_combo.bind('<<ComboboxSelected>>', self.on_plan_selected)

        self.search_label = ttk.Label(toolbar, text=self.lang_data['search'])
        self.search_label.pack(side=tk.LEFT, padx=(10, 2))
        self.search_var = tk.StringVar()
        self.search_var.trace('w', lambda *args: self.update_inventory_table())
        ttk.Entry(toolbar, textvariable=self.search_var, width=15).pack(side=tk.LEFT, padx=2)

        mass_frame = ttk.Frame(frame)
        mass_frame.pack(fill=tk.X, pady=2)
        self.bulk_label = ttk.Label(mass_frame, text=self.lang_data['bulk_change'])
        self.bulk_label.pack(side=tk.LEFT, padx=5)
        self.bulk_column_var = tk.StringVar(value=self.lang_data['col_warehouse'])
        self.bulk_column_combo = ttk.Combobox(mass_frame, textvariable=self.bulk_column_var,
                                              values=(self.lang_data['col_plan'], self.lang_data['col_warehouse']),
                                              state='readonly', width=8)
        self.bulk_column_combo.pack(side=tk.LEFT, padx=2)
        self.value_label = ttk.Label(mass_frame, text=self.lang_data['value'])
        self.value_label.pack(side=tk.LEFT, padx=5)
        self.bulk_value_var = tk.StringVar()
        ttk.Entry(mass_frame, textvariable=self.bulk_value_var, width=12).pack(side=tk.LEFT, padx=2)
        self.bulk_apply_btn = ttk.Button(mass_frame, text=self.lang_data['bulk_apply'], command=self.apply_bulk_to_all)
        self.bulk_apply_btn.pack(side=tk.LEFT, padx=2)

        self.inv_columns = ('col_component', 'col_plan', 'col_warehouse')
        self.inv_tree = self._create_treeview(frame, self.inv_columns, {'col_component': 200, 'col_plan': 150, 'col_warehouse': 150})
        self.inv_tree.bind('<Button-1>', lambda e: self._set_active_cell(e, 'inventory'))
        self.inv_tree.bind('<Double-1>', lambda e: self._on_double_click(e, 'inventory', self.inv_tree, self._edit_inventory_field))
        self.inv_edit_entry = None

    def update_inventory_labels(self):
        self.inv_copy_btn.config(text=self.lang_data['copy'])
        self.inv_paste_btn.config(text=self.lang_data['paste'])
        self.plan_label.config(text=self.lang_data['plan'])
        self.search_label.config(text=self.lang_data['search'])
        self.bulk_label.config(text=self.lang_data['bulk_change'])
        current_val = self.bulk_column_var.get()
        self.bulk_column_combo['values'] = (self.lang_data['col_plan'], self.lang_data['col_warehouse'])
        if current_val in (self.lang_data['col_plan'], self.lang_data['col_warehouse']):
            self.bulk_column_var.set(current_val)
        else:
            self.bulk_column_var.set(self.lang_data['col_warehouse'])
        self.value_label.config(text=self.lang_data['value'])
        self.bulk_apply_btn.config(text=self.lang_data['bulk_apply'])

    def _edit_inventory_field(self, item, col_name, values):
        return False

    def refresh_inventory(self):
        if not self.data:
            self.inv_tree.delete(*self.inv_tree.get_children())
            return
        plans = self.data.get('productionPlans', [])
        plan_names = [p.get('name', 'Без имени') for p in plans]
        all_comp = self.lang_data['all_components']
        combo_values = [all_comp] + plan_names
        self.plan_combo['values'] = combo_values
        self.plan_combo.set(all_comp)
        self.update_inventory_table()

    def on_plan_selected(self, event=None):
        self.update_inventory_table()

    def update_inventory_table(self):
        self.inv_tree.delete(*self.inv_tree.get_children())
        if not self.data:
            return
        plan_name = self.plan_var.get()
        inv = self.data.get('inventory', {})
        search = self.search_var.get().strip().lower()
        plan_prod = {}
        all_comp = self.lang_data['all_components']
        if plan_name != all_comp:
            plans = self.data.get('productionPlans', [])
            plan = next((p for p in plans if p.get('name') == plan_name), None)
            if plan:
                plan_prod = plan.get('production', {})
        for comp in ALL_COMPONENTS:
            if search and search not in comp.lower():
                continue
            self.inv_tree.insert('', 'end', values=(
                comp,
                plan_prod.get(comp, 0),
                inv.get(comp, 0)
            ))

    def apply_bulk_to_all(self):
        if not self.data:
            messagebox.showinfo(self.lang_data['save_first'])
            return
        col = self.bulk_column_var.get()
        try:
            val = float(self.bulk_value_var.get())
        except ValueError:
            messagebox.showerror(self.lang_data['error'], self.lang_data['enter_number'])
            return
        plan_name = self.plan_var.get()
        all_comp = self.lang_data['all_components']
        # Сравниваем с переведёнными названиями
        if col == self.lang_data['col_plan']:
            if plan_name == all_comp:
                messagebox.showerror(self.lang_data['error'], self.lang_data['bulk_plan_error'])
                return
            plans = self.data.get('productionPlans', [])
            plan = next((p for p in plans if p.get('name') == plan_name), None)
            if not plan:
                messagebox.showerror(self.lang_data['error'], self.lang_data['plan_not_found'])
                return
            for comp in ALL_COMPONENTS:
                plan['production'][comp] = val
        else:  # склад
            inv = self.data.get('inventory', {})
            for comp in ALL_COMPONENTS:
                inv[comp] = val
        self.update_inventory_table()
        messagebox.showinfo(
            self.lang_data['bulk_done_title'],
            self.lang_data['bulk_done_body'].format(value=val, col=col)
        )

    # ---------- ВКЛАДКА "ТРАНЗАКЦИИ" ----------
    def setup_transactions_tab(self):
        frame = self.tab_transactions
        toolbar = ttk.Frame(frame)
        toolbar.pack(fill=tk.X, pady=(0, 5))
        self.trans_copy_btn = ttk.Button(toolbar, text=self.lang_data['copy'], command=lambda: self._copy_cell('transactions'))
        self.trans_copy_btn.pack(side=tk.LEFT, padx=2)
        self.trans_paste_label = ttk.Label(toolbar, text="  (" + self.lang_data['paste_not_supported'] + ")")
        self.trans_paste_label.pack(side=tk.LEFT, padx=5)

        self.trans_columns = ('col_day', 'col_hour', 'col_amount', 'col_description')
        self.trans_tree = self._create_treeview(frame, self.trans_columns, {'col_day': 80, 'col_hour': 80, 'col_amount': 120, 'col_description': 400})
        self.trans_tree.bind('<Button-1>', lambda e: self._set_active_cell(e, 'transactions'))

    def update_transaction_labels(self):
        self.trans_copy_btn.config(text=self.lang_data['copy'])
        self.trans_paste_label.config(text="  (" + self.lang_data['paste_not_supported'] + ")")

    def refresh_transactions(self):
        self.trans_tree.delete(*self.trans_tree.get_children())
        if not self.data:
            return
        for t in self.data.get('transactions', [])[-200:]:
            self.trans_tree.insert('', 'end', values=(
                t.get('day', ''),
                f"{t.get('hour', 0)}:{t.get('minute', 0):02d}",
                f"{t.get('amount', 0):,.2f}",
                t.get('label', '')[:60]
            ))

if __name__ == "__main__":
    root = tk.Tk()
    app = SaveEditorApp(root)
    root.mainloop()