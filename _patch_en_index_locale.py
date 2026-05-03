"""One-off locale fix: replace Russian UI strings in en/index.html with English."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent
PATH = ROOT / "en" / "index.html"


def main() -> None:
    t = PATH.read_text(encoding="utf-8")
    pairs: list[tuple[str, str]] = [
        ('alt="Интерфейс Sendy в телефоне"', 'alt="Sendy interface on a phone"'),
        ('<p><b class="font-bold">Фраза:</b> ищу квартиру</p>', '<p><b class="font-bold">Phrase:</b> looking for an apartment</p>'),
        ('<span class="fi fi-kz mr-1 rounded-[2px]"></span>Казахстан</p>', '<span class="fi fi-kz mr-1 rounded-[2px]"></span>Kazakhstan</p>'),
        ('<p><b class="font-bold">Сообщение:</b> Ищу квартиру в Алматы<br>на длительный срок...</p>', '<p><b class="font-bold">Message:</b> Looking for an apartment in Almaty<br>long-term lease...</p>'),
        ('<b class="font-semibold text-[#555C70]">Chat:</b> публичная группа</p>', '<b class="font-semibold text-[#555C70]">Chat:</b> public group</p>'),
        ('<p><b class="font-bold">Фраза:</b> нужен дизайнер</p>', '<p><b class="font-bold">Phrase:</b> need a designer</p>'),
        ('<span class="fi fi-ua mr-1 rounded-[2px]"></span>Украина</p>', '<span class="fi fi-ua mr-1 rounded-[2px]"></span>Ukraine</p>'),
        ('<p><b class="font-bold">Сообщение:</b> Нужен дизайнер для<br>лендинга. Бюджет обсуждаем.</p>', '<p><b class="font-bold">Message:</b> Need a designer for<br>a landing page. Budget TBD.</p>'),
        ('<b class="font-semibold text-[#555C70]">Chat:</b> Telegram-чат</p>', '<b class="font-semibold text-[#555C70]">Chat:</b> Telegram chat</p>'),
        ('<p><b class="font-bold">Фраза:</b> ищу разработчика React</p>', '<p><b class="font-bold">Phrase:</b> looking for a React developer</p>'),
        ('<span class="fi fi-us mr-1 rounded-[2px]"></span>США</p>', '<span class="fi fi-us mr-1 rounded-[2px]"></span>United States</p>'),
        ('<p><b class="font-bold">Сообщение:</b> Ищу разработчика React<br>на удалёнку, срочно.</p>', '<p><b class="font-bold">Message:</b> Looking for a React developer<br>remote, urgent.</p>'),
        ('<b class="font-semibold text-[#555C70]">Chat:</b> группа стартапов</p>', '<b class="font-semibold text-[#555C70]">Chat:</b> startup group</p>'),
        ('<p><b class="font-bold">Фраза:</b> нужен юрист</p>', '<p><b class="font-bold">Phrase:</b> need a lawyer</p>'),
        ('<span class="fi fi-ru mr-1 rounded-[2px]"></span>Россия</p>', '<span class="fi fi-ru mr-1 rounded-[2px]"></span>Russia</p>'),
        ('<p><b class="font-bold">Сообщение:</b> Нужен юрист для консультации<br>по договору. Москва.</p>', '<p><b class="font-bold">Message:</b> Need a lawyer for contract<br>advice. Moscow.</p>'),
        ('>Реальные совпадения<br>сразу после появления</h3>', '>Real matches<br>the moment they appear</h3>'),
        ('>Не нужно искать вручную — Sendy присылает новые сообщения по вашим фразам.</p>', '>No manual digging — Sendy delivers new messages that match your phrases.</p>'),
        ('>Работа по регионам</h3>', '>Coverage by region</h3>'),
        ('>Получайте релевантные сообщения из выбранной страны или рынка.</p>', '>Get relevant messages from the country or market you select.</p>'),
        ('>Public и Private чаты</h3>', '>Public and private chats</h3>'),
        ('>Используйте общие Telegram-чаты или подключайте свои чаты в Private modeе.</p>', '>Use public Telegram chats or connect your own chats in Private mode.</p>'),
        ('>Фокус на Telegram</p>', '>Telegram-first</p>'),
        ('>Что вы получаете с Sendy</h2>', '>What you get with Sendy</h2>'),
        ('Добавьте слова и фразы, подключайте чаты при необходимости — совпадения приходят в Telegram-бот в выбранном регионе.', 'Add words and phrases, connect chats if needed — matches arrive in the Telegram bot for your selected region.'),
        ('>Поиск в Telegram в реальном времени</p>', '>Real-time Telegram search</p>'),
        ('>Поиск по регионам</p>', '>Search by region</p>'),
        ('>Private-чаты</p>', '>Private chats</p>'),
        ('>Мгновенные совпадения</p>', '>Instant matches</p>'),
        ('>Лиды, бренды и конкуренты</p>', '>Leads, brands and competitors</p>'),
        ('Поиск в Telegram в реальном времени · Поиск по регионам · Private-чаты · Мгновенная доставка · Лиды, бренды и конкуренты', 'Real-time Telegram search · Regional coverage · Private chats · Instant delivery · Leads, brands and competitors'),
        ('>Что<br />делает<br />Sendy</h2>', '>What<br />Sendy<br />does</h2>'),
        ('>18&nbsp;732 участников</p>', '>18,732 members</p>'),
        ('font-bold text-white">И</span>', 'font-bold text-white">I</span>'),
        ('Ищу квартиру в Нью Йорке на долгий срок', 'Looking for an apartment in NYC long-term'),
        ('>Добрый день…</div>', '>Good morning…</div>'),
        ('После запуска бота вы выбираете язык и регион, добавляете фразы и получаете совпадения в Telegram.', 'After you start the bot, pick language and region, add phrases, and receive matches in Telegram.'),
        ('>ШАГ 01</p>', '>STEP 01</p>'),
        ('>Запустите Sendy</h3>', '>Launch Sendy</h3>'),
        ('Запустите Sendy', 'Launch Sendy'),
        ('Добавьте<br class="hidden md:block" />\n                фразы', 'Add<br class="hidden md:block" />\n                phrases'),
        ('Выберите регионы', 'Pick regions'),
        ('Получайте<br />\n                совпадения', 'Get<br />\n                matches'),
        ('Тот же порядок, что в Telegram-боте: язык → регион → слова → совпадения → при необходимости свои чаты.', 'Same flow as in the Telegram bot: language → region → words → matches → your own chats when needed.'),
        ('>Откройте Telegram-бота и выберите язык.</p>', '>Open the Telegram bot and choose a language.</p>'),
        ('>ШАГ 02</p>', '>STEP 02</p>'),
        ('>Выберите регион</h3>', '>Choose a region</h3>'),
        ('>Россия, Казахстан, Украина, United States, Deutschland и другие регионы.</p>', '>Russia, Kazakhstan, Ukraine, United States, Germany and other regions.</p>'),
        ('>ШАГ 03</p>', '>STEP 03</p>'),
        ('>Добавьте слова или фразы</h3>', '>Add words or phrases</h3>'),
        ('Например: «ищу квартиру», «нужен дизайнер», «rent apartment», «looking for smm».', 'For example: “looking for an apartment”, “need a designer”, “rent apartment”, “looking for smm”.'),
        ('>ШАГ 04</p>', '>STEP 04</p>'),
        ('>Получайте совпадения</h3>', '>Receive matches</h3>'),
        ('>Sendy присылает новые релевантные сообщения прямо в Telegram.</p>', '>Sendy sends new relevant messages straight to Telegram.</p>'),
        ('>ШАГ 05</p>', '>STEP 05</p>'),
        ('>Подключайте свои чаты</h3>', '>Connect your chats</h3>'),
        ('>В Private modeе можно добавить свои публичные или приватные Telegram-чаты.</p>', '>In Private mode you can add your public or private Telegram chats.</p>'),
        ('Используется<br />\n            в любых <span', 'Used<br />\n            in any <span'),
        ('>нишах</span>', '>niche</span>'),
        ('>Поиск клиентов</h3>', '>Customer acquisition</h3>'),
        ('>Находите сообщения от людей, которые уже выражают потребность в Telegram.</p>', '>Find messages from people already expressing intent on Telegram.</p>'),
        ('>Мониторинг рынка</h3>', '>Market monitoring</h3>'),
        ('>Следите за спросом, обсуждениями, жалобами и трендами в своей нише.</p>', '>Track demand, discussions, complaints and trends in your niche.</p>'),
        ('>Найм специалистов</h3>', '>Hiring signals</h3>'),
        ('>Отслеживайте сообщения от людей, которые ищут работу, специалистов или подрядчиков.</p>', '>Watch for people looking for jobs, specialists or contractors.</p>'),
        ('>B2B-продажи</h3>', '>B2B sales</h3>'),
        ('>Находите запросы на поставщиков, подрядчиков, интеграторов и услуги.</p>', '>Surface requests for vendors, contractors, integrators and services.</p>'),
        ('>Мониторинг и сигналы</p>', '>Monitoring and signals</p>'),
        ('>Не только лиды</h2>', '>Not just leads</h2>'),
        ('Sendy можно использовать не только для поиска клиентов, но и для мониторинга брендов, отзывов, конкурентов и рыночных сигналов в Telegram.', 'Sendy is not only for finding customers — use it to monitor brands, reviews, competitors and market signals on Telegram.'),
        ('>Лиды и спрос</h3>', '>Leads and demand</h3>'),
        ('>Ловите запросы вроде «ищу», «нужен», «кто может», «looking for» в момент появления.</p>', '>Catch prompts like “looking for”, “need”, “who can”, “wanted” as soon as they appear.</p>'),
        ('>Упоминания бренда</h3>', '>Brand mentions</h3>'),
        ('>Следите за обсуждениями компании, продуктов и кампаний в чатах и группах.</p>', '>Follow conversations about your company, products and campaigns in chats and groups.</p>'),
        ('>Отзывы и жалобы</h3>', '>Reviews and complaints</h3>'),
        ('>Видите негатив и вопросы пользователей раньше, чем они разрастутся в публичный скандал.</p>', '>See friction and user questions before they escalate.</p>'),
        ('>Конкуренты и рынок</h3>', '>Competitors and market</h3>'),
        ('>Отслеживайте активность конкурентов, цены, найм и тренды в вашей нише.</p>', '>Track competitor activity, pricing, hiring and trends in your space.</p>'),
        ('>Пример совпадения</p>', '>Sample match</p>'),
        ('>Пример выдачи Sendy</h2>', '>Example Sendy notification</h2>'),
        ('>В уведомлении видно фразу, регион, текст сообщения и действия — открыть автора или чат.</p>', '>The notification shows phrase, region, message text and actions — open the author or chat.</p>'),
        ('<p><b class="font-bold">Сообщение:</b> «Ищу квартиру в Алматы на длительный срок…»</p>', '<p><b class="font-bold">Message:</b> “Looking for an apartment in Almaty long-term…”</p>'),
        ('>Иллюстрация интерфейса</p>', '>Interface illustration</p>'),
        ('>Как выглядит работа Sendy</h2>', '>How Sendy looks in practice</h2>'),
        ('Ниже — демонстрация процесса (меню бота, слова, чаты, совпадения). Это визуальная иллюстрация, а не отдельный веб-кабинет: в первой версии вы работаете через Telegram-бота.', 'Below is a walkthrough (bot menu, words, chats, matches). This is a visual demo, not a separate web dashboard — v1 runs through the Telegram bot.'),
        ('Интерактивный пример: сообщения в чате превращаются в карточки совпадений справа.', 'Interactive demo: chat messages become match cards on the right.'),
        ('>Поиск</span>', '>Search</span>'),
        ('>Дизайн-чат</p>', '>Design chat</p>'),
        ('>23 участника · 10 в сети</p>', '>23 members · 10 online</p>'),
        ('placeholder="Напишите сообщение…"', 'placeholder="Type a message…"'),
        ('>Новые совпадения</p>', '>New matches</p>'),
        ('Макет экрана показывает логику работы для презентации; основной продукт — Telegram-бот Sendy.', 'This mock explains the flow for presentation; the live product is the Sendy Telegram bot.'),
        ('>Без Sendy</p>', '>Without Sendy</p>'),
        ('>Ручной поиск</h3>', '>Manual search</h3>'),
        ('>❌ Нужно вручную проверять десятки чатов</li>', '>❌ Manually checking dozens of chats</li>'),
        ('>❌ Легко пропустить сообщение</li>', '>❌ Easy to miss a message</li>'),
        ('>❌ Нет фильтрации по региону и фразам</li>', '>❌ No filtering by region and phrases</li>'),
        ('>❌ Новые запросы приходится искать самому</li>', '>❌ You chase every new request yourself</li>'),
        ('>С Sendy</p>', '>With Sendy</p>'),
        ('>Авто-совпадения</h3>', '>Auto matches</h3>'),
        ('>✅ Sendy отслеживает новые сообщения автоматически</li>', '>✅ Sendy watches new messages automatically</li>'),
        ('>✅ Вы получаете совпадения прямо в Telegram</li>', '>✅ You get matches inside Telegram</li>'),
        ('>✅ Фразы и регионы помогают убрать лишний шум</li>', '>✅ Phrases and regions cut the noise</li>'),
        ('>✅ Public и Private чаты в одном инструменте</li>', '>✅ Public and private chats in one tool</li>'),
        ('>Private mode для своих чатов</h2>', '>Private mode for your chats</h2>'),
        ('Подключайте свои публичные и приватные Telegram-чаты и получайте отдельную выдачу только для себя или своей команды.', 'Connect your public and private Telegram chats and get a separate feed for you or your team.'),
        ('>• свои Telegram-чаты</li>', '>• your Telegram chats</li>'),
        ('>• приватная выдача только вам</li>', '>• private feed for your eyes only</li>'),
        ('>• public/private режим для подключённых чатов</li>', '>• public/private modes for connected chats</li>'),
        ('>• отправка совпадений в личный бот или рабочий чат</li>', '>• deliver matches to DM bot or team chat</li>'),
        ('>• подходит для команд, агентств и компаний</li>', '>• built for teams, agencies and companies</li>'),
        ('>• новые чаты проходят проверку перед добавлением в систему</li>', '>• new chats are reviewed before joining the network</li>'),
        ('Смотреть тариф Private', 'See Private plan'),
        ('Для владельцев чатов', 'For chat owners'),
        ('Подключайте чаты и получайте<br/>', 'Connect chats and reach<br/>'),
        ('>релевантную аудиторию</span>', '>a relevant audience</span>'),
        ('Если публичный чат подключён к Sendy, его сообщения могут попадать в релевантную выдачу. Пользователи видят чат, где найдено совпадение, и могут перейти туда, если сообщение им полезно.', 'When a public chat is connected to Sendy, its messages may appear in relevant results. Users see which chat produced the match and can jump in when it helps them.'),
        ('>Добавьте Sendy в чат</h3>', '>Add Sendy to your chat</h3>'),
        (
            '<p class="mt-2 text-[13px] leading-[1.55] text-[#6E7380]">Добавьте Sendy в свой Telegram-чат. Если у вас есть право добавлять ботов или участников, этого достаточно. После проверки чат сможет использоваться как источник совпадений.</p>',
            '<p class="mt-2 text-[13px] leading-[1.55] text-[#6E7380]">Add Sendy to your Telegram chat. If you can add bots or members, that is enough. After review the chat can be used as a match source.</p>',
        ),
        (
            '<h3 class="text-[17px] font-extrabold text-[#0B1220]">Чат становится источником совпадений</h3>',
            '<h3 class="text-[17px] font-extrabold text-[#0B1220]">Your chat becomes a match source</h3>',
        ),
        (
            '<p class="mt-2 text-[13px] leading-[1.55] text-[#6E7380]">После проверки сообщения из чата могут участвовать в поиске Sendy.</p>',
            '<p class="mt-2 text-[13px] leading-[1.55] text-[#6E7380]">After approval, messages from the chat can feed Sendy matching.</p>',
        ),
        (
            '<h3 class="text-[17px] font-extrabold text-[#0B1220]">Получайте целевой трафик</h3>',
            '<h3 class="text-[17px] font-extrabold text-[#0B1220]">Get targeted traffic</h3>',
        ),
        (
            '<p class="mt-2 text-[13px] leading-[1.55] text-[#6E7380]">Пользователи видят релевантные сообщения и могут перейти в чат.</p>',
            '<p class="mt-2 text-[13px] leading-[1.55] text-[#6E7380]">Users see relevant messages and can jump into the chat.</p>',
        ),
        (
            '<h3 class="text-[17px] font-extrabold text-[#0B1220]">Проверка перед добавлением</h3>',
            '<h3 class="text-[17px] font-extrabold text-[#0B1220]">Review before onboarding</h3>',
        ),
        (
            '<p class="mt-2 text-[13px] leading-[1.55] text-[#6E7380]">Новые чаты проходят модерацию, чтобы поддерживать качество системы.</p>',
            '<p class="mt-2 text-[13px] leading-[1.55] text-[#6E7380]">New chats are moderated to keep the network quality high.</p>',
        ),
        ('\n            Подключить чат\n          </a>', '\n            Connect your chat\n          </a>'),
        ('<li class="flex items-center gap-2"><span class="flex h-5 w-5 items-center justify-center rounded-full bg-[#ECFDF3] text-[10px] text-[#027A48]">✓</span>1 регион</li>', '<li class="flex items-center gap-2"><span class="flex h-5 w-5 items-center justify-center rounded-full bg-[#ECFDF3] text-[10px] text-[#027A48]">✓</span>1 region</li>'),
        (
            '<li class="flex items-center gap-2"><span class="flex h-5 w-5 items-center justify-center rounded-full bg-[#ECFDF3] text-[10px] text-[#027A48]">✓</span>совпадения из публичных Telegram-чатов</li>',
            '<li class="flex items-center gap-2"><span class="flex h-5 w-5 items-center justify-center rounded-full bg-[#ECFDF3] text-[10px] text-[#027A48]">✓</span>Matches from public Telegram chats</li>',
        ),
        (
            '<li class="flex items-center gap-2"><span class="flex h-5 w-5 items-center justify-center rounded-full bg-[#ECFDF3] text-[10px] text-[#027A48]">✓</span>выдача прямо в Telegram-бот</li>',
            '<li class="flex items-center gap-2"><span class="flex h-5 w-5 items-center justify-center rounded-full bg-[#ECFDF3] text-[10px] text-[#027A48]">✓</span>Delivered in your Telegram bot</li>',
        ),
        ('<li class="flex items-center gap-2"><span class="flex h-5 w-5 items-center justify-center rounded-full bg-[#ECFDF3] text-[10px] text-[#027A48]">✓</span>30 дней доступа</li>', '<li class="flex items-center gap-2"><span class="flex h-5 w-5 items-center justify-center rounded-full bg-[#ECFDF3] text-[10px] text-[#027A48]">✓</span>30 days access</li>'),
        ('<li class="flex items-center gap-2"><span class="flex h-5 w-5 items-center justify-center rounded-full bg-[#ECFDF3] text-[10px] text-[#027A48]">✓</span>слова и фразы без ограничений</li>', '<li class="flex items-center gap-2"><span class="flex h-5 w-5 items-center justify-center rounded-full bg-[#ECFDF3] text-[10px] text-[#027A48]">✓</span>Unlimited words and phrases</li>'),
        ('<li class="flex items-center gap-2"><span class="flex h-5 w-5 items-center justify-center rounded-full bg-[#ECFDF3] text-[10px] text-[#027A48]">✓</span>совпадения в Telegram в реальном времени</li>', '<li class="flex items-center gap-2"><span class="flex h-5 w-5 items-center justify-center rounded-full bg-[#ECFDF3] text-[10px] text-[#027A48]">✓</span>Real-time Telegram matches</li>'),
        ('<li class="flex items-center gap-2"><span class="flex h-5 w-5 items-center justify-center rounded-full bg-[#ECFDF3] text-[10px] text-[#027A48]">✓</span>подходит для регулярного поиска</li>', '<li class="flex items-center gap-2"><span class="flex h-5 w-5 items-center justify-center rounded-full bg-[#ECFDF3] text-[10px] text-[#027A48]">✓</span>Ideal for ongoing searches</li>'),
        ('<li class="flex items-center gap-2"><span class="flex h-5 w-5 items-center justify-center rounded-full bg-[#ECFDF3] text-[10px] text-[#027A48]">✓</span>всё из Pro</li>', '<li class="flex items-center gap-2"><span class="flex h-5 w-5 items-center justify-center rounded-full bg-[#ECFDF3] text-[10px] text-[#027A48]">✓</span>Everything in Pro</li>'),
        ('<li class="flex items-center gap-2"><span class="flex h-5 w-5 items-center justify-center rounded-full bg-[#ECFDF3] text-[10px] text-[#027A48]">✓</span>подключение своих публичных и приватных чатов</li>', '<li class="flex items-center gap-2"><span class="flex h-5 w-5 items-center justify-center rounded-full bg-[#ECFDF3] text-[10px] text-[#027A48]">✓</span>Connect your public and private chats</li>'),
        ('<li class="flex items-center gap-2"><span class="flex h-5 w-5 items-center justify-center rounded-full bg-[#ECFDF3] text-[10px] text-[#027A48]">✓</span>private-выдача только вам</li>', '<li class="flex items-center gap-2"><span class="flex h-5 w-5 items-center justify-center rounded-full bg-[#ECFDF3] text-[10px] text-[#027A48]">✓</span>Private feed for you only</li>'),
        ('<li class="flex items-center gap-2"><span class="flex h-5 w-5 items-center justify-center rounded-full bg-[#ECFDF3] text-[10px] text-[#027A48]">✓</span>public/private режим подключённых чатов</li>', '<li class="flex items-center gap-2"><span class="flex h-5 w-5 items-center justify-center rounded-full bg-[#ECFDF3] text-[10px] text-[#027A48]">✓</span>Public/private modes for connected chats</li>'),
        ('<li class="flex items-center gap-2"><span class="flex h-5 w-5 items-center justify-center rounded-full bg-[#ECFDF3] text-[10px] text-[#027A48]">✓</span>подходит для команд и агентств</li>', '<li class="flex items-center gap-2"><span class="flex h-5 w-5 items-center justify-center rounded-full bg-[#ECFDF3] text-[10px] text-[#027A48]">✓</span>Built for teams and agencies</li>'),
        ('<p class="mt-3 max-w-[260px] text-[13px] leading-[1.6] text-[#6E7380]">Слова, фразы и совпадения в Telegram в реальном времени.</p>', '<p class="mt-3 max-w-[260px] text-[13px] leading-[1.6] text-[#6E7380]">Words, phrases and Telegram matches in real time.</p>'),
        ('<li><a href="#audience" class="transition hover:text-violet">Поиск клиентов</a></li>', '<li><a href="#audience" class="transition hover:text-violet">Customer acquisition</a></li>'),
        ('<li><a href="#audience" class="transition hover:text-violet">Мониторинг бренда</a></li>', '<li><a href="#audience" class="transition hover:text-violet">Brand monitoring</a></li>'),
        ('<li><a href="#audience" class="transition hover:text-violet">Конкуренты</a></li>', '<li><a href="#audience" class="transition hover:text-violet">Competitors</a></li>'),
        ('<li><a href="#audience" class="transition hover:text-violet">B2B-продажи</a></li>', '<li><a href="#audience" class="transition hover:text-violet">B2B sales</a></li>'),
        ('<h3 class="text-2xl font-black tracking-[-.04em]">Как работает Sendy</h3>', '<h3 class="text-2xl font-black tracking-[-.04em]">How Sendy works</h3>'),
        ('<p class="mt-2 text-sm leading-6 text-muted">Вы запускаете Telegram-бота, выбираете язык и регион, добавляете слова и фразы — совпадения приходят в бот. При необходимости подключаете свои чаты или оформляете подписку.</p>', '<p class="mt-2 text-sm leading-6 text-muted">Open the Telegram bot, choose language and region, add words and phrases — matches arrive in the bot. Connect your own chats or upgrade when you need Private mode.</p>'),
        ('<div class="rounded-2xl bg-[#F7F7FF] p-4">1. Запустите бота и выберите язык.</div>', '<div class="rounded-2xl bg-[#F7F7FF] p-4">1. Launch the bot and pick a language.</div>'),
        ('<div class="rounded-2xl bg-[#F7F7FF] p-4">2. Выберите регион.</div>', '<div class="rounded-2xl bg-[#F7F7FF] p-4">2. Choose a region.</div>'),
        ('<div class="rounded-2xl bg-[#F7F7FF] p-4">3. Добавьте слова или фразы.</div>', '<div class="rounded-2xl bg-[#F7F7FF] p-4">3. Add words or phrases.</div>'),
        ('<div class="rounded-2xl bg-[#F7F7FF] p-4">4. Получайте совпадения в Telegram.</div>', '<div class="rounded-2xl bg-[#F7F7FF] p-4">4. Receive matches in Telegram.</div>'),
        ('<div class="rounded-2xl bg-[#F7F7FF] p-4">5. При необходимости подключите свои чаты (Private) или тариф.</div>', '<div class="rounded-2xl bg-[#F7F7FF] p-4">5. Connect your chats (Private) or choose a plan when needed.</div>'),
    ]

    faq_en = '''        <div class="space-y-3">
          <article class="faq-item glass overflow-hidden rounded-[14px]">
            <button class="faq-trigger flex w-full items-center justify-between p-4 text-left font-bold">What is Sendy?<span>+</span></button>
            <div class="faq-content hidden px-4 pb-4 text-[14px] text-[#6E7380]">Sendy is a Telegram service that finds messages by words, phrases and regions and delivers matches in real time.</div>
          </article>
          <article class="faq-item glass overflow-hidden rounded-[14px]">
            <button class="faq-trigger flex w-full items-center justify-between p-4 text-left font-bold">Where do I receive matches?<span>+</span></button>
            <div class="faq-content hidden px-4 pb-4 text-[14px] text-[#6E7380]">In Telegram — in your Sendy bot DM. In some setups matches can also go to a team chat.</div>
          </article>
          <article class="faq-item glass overflow-hidden rounded-[14px]">
            <button class="faq-trigger flex w-full items-center justify-between p-4 text-left font-bold">Can I monitor my own chats?<span>+</span></button>
            <div class="faq-content hidden px-4 pb-4 text-[14px] text-[#6E7380]">Yes. Private mode lets you connect your public and private Telegram chats.</div>
          </article>
          <article class="faq-item glass overflow-hidden rounded-[14px]">
            <button class="faq-trigger flex w-full items-center justify-between p-4 text-left font-bold">How is public mode different from private?<span>+</span></button>
            <div class="faq-content hidden px-4 pb-4 text-[14px] text-[#6E7380]">In public mode a chat may feed the shared matching pool. In private mode matches from that chat are only for you.</div>
          </article>
          <article class="faq-item glass overflow-hidden rounded-[14px]">
            <button class="faq-trigger flex w-full items-center justify-between p-4 text-left font-bold">Can I track brands, reviews and competitors?<span>+</span></button>
            <div class="faq-content hidden px-4 pb-4 text-[14px] text-[#6E7380]">Yes — add a brand, product, competitor name or any phrase you need.</div>
          </article>
          <article class="faq-item glass overflow-hidden rounded-[14px]">
            <button class="faq-trigger flex w-full items-center justify-between p-4 text-left font-bold">How does billing work?<span>+</span></button>
            <div class="faq-content hidden px-4 pb-4 text-[14px] text-[#6E7380]">You pick a plan and region, pay for the subscription, and access activates automatically.</div>
          </article>
          <article class="faq-item glass overflow-hidden rounded-[14px]">
            <button class="faq-trigger flex w-full items-center justify-between p-4 text-left font-bold">Do I pay for the trial?<span>+</span></button>
            <div class="faq-content hidden px-4 pb-4 text-[14px] text-[#6E7380]">No — you can start the trial without payment.</div>
          </article>
          <article class="faq-item glass overflow-hidden rounded-[14px]">
            <button class="faq-trigger flex w-full items-center justify-between p-4 text-left font-bold">How fast is setup?<span>+</span></button>
            <div class="faq-content hidden px-4 pb-4 text-[14px] text-[#6E7380]">Usually pick a region and add your first phrase — about a minute.</div>
          </article>
          <article class="faq-item glass overflow-hidden rounded-[14px]">
            <button class="faq-trigger flex w-full items-center justify-between p-4 text-left font-bold">Which sources does Sendy support?<span>+</span></button>
            <div class="faq-content hidden px-4 pb-4 text-[14px] text-[#6E7380]">Telegram chats and groups. Private mode supports your public and private chats.</div>
          </article>
          <article class="faq-item glass overflow-hidden rounded-[14px]">
            <button class="faq-trigger flex w-full items-center justify-between p-4 text-left font-bold">How many keywords can I add?<span>+</span></button>
            <div class="faq-content hidden px-4 pb-4 text-[14px] text-[#6E7380]">Limits depend on your plan — we show current limits before you subscribe.</div>
          </article>
          <article class="faq-item glass overflow-hidden rounded-[14px]">
            <button class="faq-trigger flex w-full items-center justify-between p-4 text-left font-bold">Is Sendy GDPR-aligned?<span>+</span></button>
            <div class="faq-content hidden px-4 pb-4 text-[14px] text-[#6E7380]">Sendy is built with GDPR principles: data minimisation, user-controlled configuration, restricted access and temporary technical processing of Telegram content. For group content processed per user settings, Sendy typically acts as processor and the configuring user acts as controller.</div>
          </article>
          <article class="faq-item glass overflow-hidden rounded-[14px]">
            <button class="faq-trigger flex w-full items-center justify-between p-4 text-left font-bold">Does Sendy store Telegram messages forever?<span>+</span></button>
            <div class="faq-content hidden px-4 pb-4 text-[14px] text-[#6E7380]">No — Sendy is not meant to archive full chats. Content is processed temporarily to detect matches and deliver notifications.</div>
          </article>
          <article class="faq-item glass overflow-hidden rounded-[14px]">
            <button class="faq-trigger flex w-full items-center justify-between p-4 text-left font-bold">Who is responsible for connected chats?<span>+</span></button>
            <div class="faq-content hidden px-4 pb-4 text-[14px] text-[#6E7380]">The user who connects a chat or configures monitoring is responsible for rights, permissions and lawful basis.</div>
          </article>
          <article class="faq-item glass overflow-hidden rounded-[14px]">
            <button class="faq-trigger flex w-full items-center justify-between p-4 text-left font-bold">Can I request deletion of my data?<span>+</span></button>
            <div class="faq-content hidden px-4 pb-4 text-[14px] text-[#6E7380]">Yes — email <a href="mailto:legal@sendy.direct" class="font-medium text-violet hover:underline">legal@sendy.direct</a> or <a href="mailto:support@sendy.direct" class="font-medium text-violet hover:underline">support@sendy.direct</a> to ask for account or monitoring data deletion, subject to legal, tax, billing and security requirements.</div>
          </article>
          <article class="faq-item glass overflow-hidden rounded-[14px]">
            <button class="faq-trigger flex w-full items-center justify-between p-4 text-left font-bold">Does the number of matches depend on settings?<span>+</span></button>
            <div class="faq-content hidden px-4 pb-4 text-[14px] text-[#6E7380]">Yes — volume depends on region, phrases and available sources. We do not guarantee a fixed number of results.</div>
          </article>
          <article class="faq-item glass overflow-hidden rounded-[14px]">
            <button class="faq-trigger flex w-full items-center justify-between p-4 text-left font-bold">How are payments processed?<span>+</span></button>
            <div class="faq-content hidden px-4 pb-4 text-[14px] text-[#6E7380]">Payments are processed by third-party providers (including NOWPayments where applicable). Sendy does not store full card credentials. Provider and network fees may apply separately.</div>
          </article>
          <article class="faq-item glass overflow-hidden rounded-[14px]">
            <button class="faq-trigger flex w-full items-center justify-between p-4 text-left font-bold">How do I report illegal content or abuse?<span>+</span></button>
            <div class="faq-content hidden px-4 pb-4 text-[14px] text-[#6E7380]">Use the <a href="/en/report-abuse.html" class="font-medium text-violet hover:underline">report abuse</a> page or email <a href="mailto:legal@sendy.direct" class="font-medium text-violet hover:underline">legal@sendy.direct</a>. See Legal &amp; Compliance for more.</div>
          </article>
          <article class="faq-item glass overflow-hidden rounded-[14px]">
            <button class="faq-trigger flex w-full items-center justify-between p-4 text-left font-bold">Is there a trial?<span>+</span></button>
            <div class="faq-content hidden px-4 pb-4 text-[14px] text-[#6E7380]">Yes — a free 3-day trial without a card.</div>
          </article>'''

    faq_anchor = t.find('id="faq"')
    if faq_anchor == -1:
        raise SystemExit('faq section id missing')
    faq_open = t.find('<div class="space-y-3">', faq_anchor)
    if faq_open == -1:
        raise SystemExit('faq space-y-3 block not found')
    faq_section_inner_end = t.find('\n        </div>\n      </div>\n    </section>', faq_open)
    if faq_section_inner_end == -1:
        raise SystemExit('faq section end pattern missing')

    prefix = t[: faq_open]
    suffix = t[faq_section_inner_end:]
    t = prefix + faq_en + suffix

    for old, new in pairs:
        if old not in t:
            print('WARN missing substring:', old[:70])
        t = t.replace(old, new)

    PATH.write_text(t, encoding="utf-8")
    print('Patched', PATH)


if __name__ == '__main__':
    main()
