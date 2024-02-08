terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.15.0"
    }
  }
}

provider "google" {
  project = ""
  region  = ""
}

resource "google_storage_bucket" "demo-bucket" {
  name          = ""
  location      = ""
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 7
    }
    action {
      type = "Delete"
    }
  }
}