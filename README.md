## Bot Outrun Platformer!
Created by Timofey-code.
Welcome to Bot Outrun Simulator, where you have to collect items to build a PC! Traverse 3 levels with different terrain.
This is a fun little game that you can play when bored, and try to get the lowest time possible. The sprites and decoration are very simple, however the gameplay itself is very addicting, and the more you play, the better you get!


BUT... it isn't that easy...

There are 3 AI robots on each level that are programmed to hunt you down at all costs! However, there is 1 extra boomer on level 3, making 4 robots on the hardest level.

There are many types of them - stalkers, sweepers, boomers, shovers, runners... the lists goes on. They each have unique mechanics which makes the game so much more challenging!

Do not worry, for if your system is corrupted, or files deleted by the AIs, you will respawn by being cloned on the same level. 

Are you ready to play? You might want to read further first.

## How to use?

Usable on VS code - make sure you have installed the official Python library, and press the "play" button.

Launch via terminal (python run) - 1. Download or save the code into a file named platformer.py inside your preferred folder.

2. Open your terminal/command prompt and navigate (cd) to that folder.

3. Launch the game by typing:
```bash
python platformer.py
```
(Note: Depending on your system installation, you might need to type python3 platformer.py instead).


## Startup

Before starting, you will need to run an install.
For windows:
```bash
pip install pygame
```

For Mac/Linux:
```bash
pip3 install pygame
```

## Gameplay Features
*   **3 Unique Levels:** From basic floor structures to a highly vertical, complex platform grid.
*   **Specialized AI Enemy Archetypes:**
    *   `Runner` (ChatGPT & DeepSeek): Fast, direct ground pursuers.
    *   `Stalker` (Gemini & Claude): Levitating bots that track your altitude.
    *   `Shover` (Grok, Qwen, & OpenAI): Heavy, tank-like obstacles.
    *   `Boomer` (Perplexity & Gemma): Patrolling proximity bots that pulse and sprint when you get close.
    *   `Sweeper` (Copilot): High-speed, level 3 exclusive platform hazard.
*   **PC Building Progression:** Collect vital components (`RAM`, `Mouse`, `Keyboard`, `CPU`, `GPU`, `SSD`) to hit your target quota and unlock the next stage.
*   **Dynamic Visuals:** Procedural leg animations for the player, color-coded AI tags, and dedicated matrix-style overlay screens for "System Failures" and "Humanity Preserved" victories.


## Controls
*   **`A`** — Move Left
*   **`D`** — Move Right
*   **`W`** — Jump
*   **`ENTER`** — Start Game / Restart Game after Ultimate Victory
*   **`SPACEBAR`** — Respawn & retry current level after a System Failure (game over)

 ## Mechanics (For Developers)
 
 **State Matrix Router:** Level transitions dynamically hot-swap platform layouts, item quotas, and AI robot configurations seamlessly without reloading resources.
 
**Collisions:** Custom axis-aligned bounding box collision routines handle platform grounding, vertical ceiling blocks, and pixel-precise coordinate resets.

**Difficulty Scaling:** As you progress to higher levels, enemy jumping thresholds are lowered and boss velocities are adjusted to drastically increase tracking efficiency.





## Платформер побега от роботов!
Добро пожаловать в  платформер побега от роботов (Bot Outrun Simulator), где вам предстоит собирать 
предметы, чтобы собрать компьютер! Пройдите 3 уровня чтобы победить.
Это забавная небольшая игра, в которую можно поиграть, когда стало скучно; попробуйте пройти её за минимально возможное время. Спрайты и оформление здесь очень простые, однако сам игровой процесс невероятно затягивает — чем больше играешь, тем лучше начинаешь справляться!

НО... все не так просто...

На каждом уровне вас ждут 3 ИИ-робота, запрограммированных выследить вас любой ценой! Однако на 3-м уровне появляется 1 дополнительный робот-бумер, так что на самом сложном этапе против вас выступят уже 4 машины.

Здесь много разных типов врагов: преследователи, зачищики, бумеры, толкатели, бегуны... и этот список можно продолжить. Каждый из них обладает уникальной механикой, что делает игру гораздо более сложной и увлекательной!

Не волнуйтесь: если ваша система будет повреждена или ИИ удалит файлы, вы возродитесь на том же уровне в виде клона.

Готовы к игре? Возможно, сначала стоит прочитать руководство ниже.

## Как запустить?

Запуск через VS Code — убедитесь, что у вас установлено официальное расширение Python, и нажмите кнопку «Play» (Запуск)  в верхнем правом углу.

Запуск через терминал — 1. Скачайте или сохраните код в файл с именем platformer.py в выбранную вами папку.

2. Откройте терминал/командную строку и перейдите (`cd`) в эту папку.

3. Запустите игру, введя команду:
```bash
python platformer.py
```
*(Примечание: в зависимости от настроек вашей системы, вместо этого может потребоваться ввести `python3 platformer.py`).*

## Подготовка к запуску

Перед началом игры необходимо установить зависимость.
Для Windows:
```bash
pip install pygame
```

Для Mac/Linux:
```bash
pip3 install pygame
```

## Особенности игрового процесса
*   **3 уникальных уровня:** от базовых напольных платформ до сложной вертикальной сетки.
*   **Специализированные архетипы ИИ-врагов:**
    *   `Runner` / Бегун (ChatGPT и DeepSeek): быстрые наземные преследователи, движущиеся напролом.
    *   `Stalker` / Преследователь (Gemini и Claude): парящие роботы, отслеживающие вашу высоту.
    *   `Shover` / Толкатель (Grok, Qwen и OpenAI): тяжелые роботы-танки, служащие препятствием.
    *   `Boomer` / Бумер (Perplexity и Gemma): патрульные роботы, которые начинают пульсировать и ускоряться при вашем приближении.
    *   `Sweeper` / Зачищик (Copilot): высокоскоростная угроза, уникальная для 3-го уровня.
*   **Сборка ПК:** собирайте ключевые компоненты (`RAM`, `Mouse`, `Keyboard`, `CPU`, `GPU`, `SSD`), чтобы выполнить норму и открыть следующий этап.
*   **Динамическая графика:** процедурная анимация ног игрока, цветовая кодировка названий ИИ и стилизованные под «Матрицу» экраны для системных сбоев («System Failure») и победы человечества («Humanity Preserved»).

## Управление
*   **`A`** — Движение влево
*   **`D`** — Движение вправо
*   **`W`** — Прыжок
*   **`ENTER`** — Начать игру / Перезапустить игру после абсолютной победы
*   **`SPACEBAR` (Пробел)** — Возродиться и переиграть текущий уровень после системного сбоя (Game Over)

## Механики (Для разработчиков)
 
**Маршрутизатор матрицы состояний (State Matrix Router):** переходы между уровнями динамически и бесшовно меняют схемы платформ, нормы предметов и конфигурации ИИ-роботов без перезагрузки ресурсов.
 
**Коллизии AABB:** кастомные алгоритмы столкновения по оси (axis-aligned bounding box) отвечают за приземление на платформы, вертикальные блоки потолка и сброс координат с пиксельной точностью.

**Динамическое масштабирование сложности:** по мере продвижения на более высокие уровни порог прыжков врагов снижается, а скорость боссов корректируется, что значительно повышает эффективность их слежки за игроком.

