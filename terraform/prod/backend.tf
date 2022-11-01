terraform {

  backend "s3" {
    endpoint   = "storage.yandexcloud.net"
    bucket     = "storage-backet-moiseevpa"
    region     = "ru-central1-a"
    key        = "terraform.tfstate"
    access_key = "YCAJEu1ZyLsw5kaDYsV9eG8qi"
    secret_key = "YCPvt9r_uCZ0lIZnkDl7Eqxg5biEHf6IZB5VTcKe"

    skip_region_validation      = true
    skip_credentials_validation = true
  }
}