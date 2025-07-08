# CSS Selectors Cheatsheet

| Тип                   | Пример                      | Описание                                         |
|-----------------------|-----------------------------|--------------------------------------------------|
| По тегу               | `button`                    | Все элементы `<button>`                          |
| По классу             | `.btn`                      | Элементы с классом `btn`                         |
| По ID                 | `#login`                    | Элемент с `id="login"`                           |
| По атрибуту           | `[type="text"]`             | Атрибут `type` равен "text"                      |
| Комбинация            | `input#search.form-control` | `input` с `id="search"` и `class="form-control"` |
| Потомок любого уровня | `form input`                | Все `input` внутри формы                         |
| Прямой потомок        | `div > span`                | Только прямые потомки `<div>`                    |
| Первый элемент        | `ul li:first-child`         | Первый `li` в списке                             |
| Последний элемент     | `ul li:last-child`          | Последний `li` в списке                          |
| N-ый элемент          | `ul li:nth-child(3)`        | Третий `li`                                      |
| Частичное совпадение  | `a[href*="contact"]`        | `href` содержит "contact"                        |
| Начинается с          | `input[name^="user"]`       | Атрибут `name` начинается с "user"               |
| Заканчивается на      | `input[name$="name"]`       | Атрибут `name` заканчивается на "name"           |

📌 Быстрое копирование в DevTools:
ПКМ → Inspect → ПКМ на HTML-элементе → Copy → Copy **Selector**
