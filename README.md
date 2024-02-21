# Автопостинг картинок в телеграм и VK
1. Скачайте проект:<br>
```bash
git clone https://github.com/VeronikaChirkova/Autoposting_VK_Telegram.git
```
2. Создайте вртуальное окружение:<br>
```bash
python -m venv venv
```
3. Активируйте виртуальное окружение:<br>
```bash
.\venv\Scripts\activate
```
4. Установите зависимости:<br>
```bash
pip install -r requirements.txt
```
## Телеграм
1. Создать телеграм бота в [@BotFather](https://t.me/BotFather).<br>
2. Создайте телеграм канал (добавить телеграм-бота в качестве администратора).<br>
3. id канала `CHANNEL_ID` можно узнать, переслав любое сообщение в [@LeadConverterToolkitBot](https://t.me/LeadConverterToolkitBot).<br>
4. Создайте документ `.env` и сохраните в нем токен телеграм-бота `TOKEN_BOT` и id канала `CHANNEL_ID`.<br>

## Вконтакте
1. Создайте сообщество в Вконтакте.<br>
2. id сообщества `GROUP_ID` взять из адресной строки браузера и сохранить в файл `.env`.<br>
3. На [dev.vk.com](https://dev.vk.com/) создать `Standelone-приложение` (платформа Web).<br>
4. id приложения `CLIENT_ID` сохранить в файл `.env`.<br>
5. В приложении во вкладке **Доступы** заполнить паспортные данные и отправить на проверку. После проверки запросить расширенные доступы: *Стена, Сообщества, Фотографии*.<br>
6. Для получения токена доступа к API ВК вставьте `CLIENT_ID` в URL:
```text
https://oauth.vk.com/authorize?client_id=CLIENT_ID&redirect_uri=https://oauth.vk.com/blank.html&scope=offline,wall,photos,groups&response_type=token
```
В ответном URL будет указан `ACCESS_TOKEN`, сохранить в `.env`.<br>

### Файл .env:
Переменные, необходимые для работы:<br>
```text
TOKEN_BOT=your_telegram_bot_token
CHANNEL_ID=your_channel_id
DEV=True/False
CLIENT_ID=your_app_id
ACCESS_TOKEN=your_access_token
GROUP_ID=your_group_id

```
`DEV` - отвечает за уровень логирования. В ручную выставить значение True/False.<br>
`DEV=True` - в файл debug.log будут записываться логи с уровнем DEBUG и выше.<br>
`DEV=False` - в файл debug.log будут записываться логи с уровнем WARNING и выше.<br>