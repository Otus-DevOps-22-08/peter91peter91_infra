resource "yandex_compute_instance" "db" {
  name     = "reddit-db"
  hostname = "reddit-db.internal"

  labels = {
    tags = "reddit-db"
  }

  resources {
    cores         = 2
    core_fraction = 20
    memory        = 2
  }

  boot_disk {
    initialize_params {
      image_id = var.db_disk_image
    }
  }

  network_interface {
    subnet_id = var.subnet_id
    nat = true
  }

  metadata = {
  ssh-keys = "ubuntu:${file(var.public_key_path)}"
  }

#  connection {
#    type  = "ssh"
#    host  = yandex_compute_instance.db.network_interface[0].nat_ip_address
#    user  = "ubuntu"
#    agent = false
#    private_key = file(var.private_key_path)
#  }

#  provisioner "file" {
#    content     = templatefile("${path.module}/files/mongod.conf", { db_url = yandex_compute_instance.db.network_interface.0.ip_address})
#    destination = "/tmp/mongod.conf"
#  }
#  provisioner "remote-exec" {
#    script = "${path.module}/files/deploy.sh"
#  }
}
