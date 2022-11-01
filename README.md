#peter91peter91_infra

#HW-07 (lesson-09).

Сделали:
Задали IP для инстанса с приложением в виде внешнего ресурса. Для этого определим ресурсы yandex_vpc_network и yandex_vpc_subnet в конфигурационном файле main.tf.
Посмотрели как создаются ресурсы,вау

Вынесли БД и приложение в отдельные инстансы, 
попробовали построение конфигурации терраформом

Создали файл vpc.tf, в который вынесем кофигурацию сети и подсети, которое применимо для всех инстансов нашей сети,
попробовали построение конфигурации терраформом

Разбили конфигурацию на 3 модуля. Настроили output переменные из модул.  Добавили модули командой ГЕТ.
попробовали построение конфигурации терраформом


Создали инфраструктуру для двух окружений (stage и prod), используя созданные модули.
попробовали построение конфигурации терраформом


__________________________
Настроили хранение стейт файла в удаленном бекенде (remote backends) для окружений stage и prod
Попробовали запустить применение конфигурации одновременно, чтобы проверить работу блокировок
__________________________

Добавили необходимые provisioner в модули для деплоя и работы приложения.

Опционально реализовали отключение provisioner в зависимости от значения переменной
resource "null_resource" "app" {
  count = var.prov ? 1 : 0
  triggers = {
    cluster_instance_ids = yandex_compute_instance.app.id
  }

Получили Баг:


Error: Provider produced invalid plan

Provider "null" planned an invalid value for
module.db.null_resource.db[0].triggers: planned value
cty.UnknownVal(cty.Map(cty.String)) does not match config value
cty.MapVal(map[string]cty.Value{"cluster_instance_ids":cty.UnknownVal(cty.String)}).

This is a bug in the provider, which should be reported in the provider's own
issue tracker.
