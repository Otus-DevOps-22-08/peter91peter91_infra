
resource "yandex_lb_target_group" "app" {
  name      = "app-target-group"
  region_id = "ru-central1"
  #folder_id = var.folder_id
  target {
    subnet_id = yandex_compute_instance.app.network_interface.0.subnet_id
    address   = yandex_compute_instance.app.network_interface.0.ip_address
  }

}


resource "yandex_lb_network_load_balancer" "app" {
name = "app-network-load-balancer"
folder_id = var.folder_id
  listener {
    name = "app-listener"
    port = 8080
    target_port = 9292
    external_address_spec {
      ip_version = "ipv4"
    }
  }

  attached_target_group {
    target_group_id = yandex_lb_target_group.app.id
    healthcheck {
     name = "http"
      http_options {
        port = 9292
        path = "/"
      }
    }
  }
}
