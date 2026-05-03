[03.05.2026 1:30] Euronews Only: Финальные правки по сайту

1. Сделать RU/EN версии сайта

Нужно добавить переключатель языка RU / EN.

Структура:

/ru  
/en

Для KYB будем отправлять английскую версию:

https://sendy.direct/en

2. Legal pages сделать на русском и английском

Нужны страницы:

/en/terms  
/en/privacy  
/en/refund-policy  
/en/legal-compliance  
/en/report-abuse  

И аналогично на русском:

/ru/terms  
/ru/privacy  
/ru/refund-policy  
/ru/legal-compliance  
/ru/report-abuse  

Фразу “In case of any inconsistency between translations, the English version shall prevail” не добавляем. Просто делаем нормальные RU/EN версии.

3. Добавить disclaimer про Telegram

В footer или Legal & Compliance добавить:

EN:
Sendy is not affiliated with, endorsed by, or officially associated with Telegram. Telegram is a trademark of its respective owner.

RU:
Sendy не является официальным продуктом Telegram и не связан с Telegram. Telegram является товарным знаком соответствующего правообладателя.

4. Убрать неподтверждённый рейтинг

Если на сайте есть “5.0 по отзывам пользователей” — убрать, если нет реальных отзывов.

Вместо этого можно поставить мягкий вариант:

RU:
3 дня бесплатно · Без карты

EN:
3-day free trial · No card required

5. Добавить мягкую формулировку про отсутствие гарантии результата

Не писать жёстко на главной. Добавить мягко в FAQ / Terms:

RU:
Количество совпадений зависит от выбранного региона, фраз и доступных источников.

EN:
The number of matches depends on the selected region, phrases and available sources.

В Terms можно добавить полнее:

EN:
Sendy does not guarantee a specific number of leads, matches, conversions or sales. Results depend on selected regions, keywords, connected sources and user configuration.

6. Проверить блок про платежи

На русской версии уже есть формулировка:

“Платежи проходят через сторонних платёжных провайдеров. Sendy не хранит данные банковских карт.”

Нужно оставить и сделать английскую версию:

Payments are processed by third-party payment providers. Sendy does not store bank card data or full payment credentials.

Если используется NOWPayments, можно добавить в Legal / Refund:

Payments may be processed through NOWPayments and other third-party payment providers. Provider and network fees may apply.

7. Сделать отдельную страницу Report Abuse

Страницы:

/en/report-abuse  
/ru/report-abuse

Текст EN:

Report Abuse or Illegal Content

If you believe that Sendy is being used unlawfully, or that a connected source contains illegal or prohibited content, please contact us at legal@sendy.direct.

Please include:
— your name and contact email;
— description of the issue;
— Telegram chat or message link, if available;
— reason for the report;
— supporting information.

We review reports and may restrict, suspend or remove sources or user configurations where appropriate.

Текст RU:

Сообщить о нарушении или незаконном контенте

Если вы считаете, что Sendy используется незаконно, либо подключённый источник содержит незаконный или запрещённый контент, напишите нам на legal@sendy.direct.

Пожалуйста, укажите:
— ваше имя и контактный email;
— описание проблемы;
— ссылку на Telegram-чат или сообщение, если доступно;
— причину обращения;
— дополнительную информацию, если есть.

Мы рассматриваем обращения и при необходимости можем ограничить, приостановить или удалить источник либо пользовательскую конфигурацию.

8. Проверить, что почты реально работают

Нужно, чтобы эти email принимали письма:

support@sendy.direct  
legal@sendy.direct  
billing@sendy.direct

Можно сделать forwarding на Gmail, главное — чтобы письма доходили.

9. Настроить meta / Open Graph для RU и EN

Для EN:

Title:
Sendy — Real-time Telegram monitoring for leads and market signals

Description:
Track words and phrases by region, receive relevant Telegram matches, and connect your own chats when needed.

Для RU:

Title:
Sendy — находите спрос в Telegram в реальном времени

Description:
Отслеживайте слова и фразы по регионам, получайте совпадения в Telegram и подключайте свои чаты.

10. Проверить preview ссылки
[03.05.2026 1:30] Euronews Only: Нужно проверить, как ссылка выглядит при отправке в:

— Telegram  
— WhatsApp  
— соцсети  

Должен подтягиваться нормальный title, description и OG-картинка 1200×630.

11. Техническая проверка перед KYB

Проверить:

— https://sendy.direct открывается с кодом 200;  
— https://www.sendy.direct либо открывается, либо редиректит на https://sendy.direct;  
— http://sendy.direct редиректит на HTTPS;  
— SSL certificate активен;  
— нет лишних parking DNS-записей Hostinger;  
— DNS-записи только нужные;  
— Open Graph meta есть в <head> и доступны без JS;  
— legal links открываются;  
— CTA “Запустить в Telegram” ведёт в актуального бота.

12. По текстам не использовать публично

Не использовать на сайте:

— scraping;  
— parsing / парсинг;  
— selfbot;  
— сканируем чаты;  
— гарантированные лиды;  
— гарантированные продажи.

Используем формулировки:

— monitoring;  
— отслеживание;  
— user-controlled monitoring;  
— temporary technical processing;  
— no permanent archive;  
— Telegram matches;  
— words and phrases;  
— regions;  
— connected chats.