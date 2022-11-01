variable "zone" {
  type = string
  default = "ru-central1-a"
}

variable "zone_app" {
  type = string
  description = "Zone app"
  # Значение по умолчанию
  default = "ru-central1-a"
}

variable "cloud_id" {
  type = string
}

variable "folder_id" {
  type = string
}

#variable "yc_tocken" {
#  type = string
#}
variable "service_account_key_file" {
  type = string
}

variable "subnet_id" {
  type = string
}

variable "image_id" {
  type = string
}

variable "app_disk_image" {
  description = "Disk image for reddit app"
  default     = "reddit-app-base"
}

variable "db_disk_image" {
  description = "Disk image for reddit db"
  default     = "reddit-db-base"
}

variable "public_key_path" {
  type = string
}

variable "private_key_path" {
  type = string
}

