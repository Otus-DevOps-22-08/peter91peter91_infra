# peter91peter91_infra
LESSON_5

bastion_IP = 178.154.203.97
someinternalhost_IP = 10.128.0.30

задание способ подключения к someinternalhost.
1)подключение в одну команду
  ssh <user_name>@<Внутренний IPv4 целевого ресурса> -o "proxycommand ssh -W %h:%p -i ~/.ssh/id_rsa <user_name>@<Публичный IPv4 бастиона>"
  либо через ssh -J
//////////////////////////////////////////////
2)подключение по алиасу:
пишем в консоли
        nano ~/.ssh/config
// и заполняем
Host someinternalhost
        HostName 10.128.0.30
        User appuser
        IdentityFile ~/.ssh/id_rsa
        Port 22
        StrictHostKeyChecking no
//
Заходим на бастион и вводим
ssh someinternalhost


OPENVPN осуществлено при помощи докера pritunl
//////////////////////////////////////////////
