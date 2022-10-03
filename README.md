# peter91peter91_infra
# QUEST №4

testapp_IP = 51.250.7.56
testapp_port = 9292

#Дополнительное задание В качестве доп. задания используйте созданные ранее
#скрипты для создания , который будет запускаться при создании инстанса.
#metadata.yml содержит весь код по развертыванию приложения

yc compute instance create `
--name reddit-app `
--hostname reddit-app `
--memory=4 `
--create-boot-disk image-folder-id=standard-images,image-family=ubuntu-1604-lts,size=10GB `
--network-interface subnet-name=default-ru-central1-a,nat-ip-version=ipv4 `
--metadata serial-port-enable=1 `
--metadata-from-file .\user-data=metadata.yml
